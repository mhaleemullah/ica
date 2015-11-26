from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.core.urlresolvers import reverse
from projects.models import Attendance,Project,Employee,Expense,Category,Dealer,PaymentExpense,Payment
from projects.tables  import ProjectTable,EmployeeTable,ExpenseTable,PaymentTable,DefaultersTable
from django_tables2   import RequestConfig
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from projects.forms import AttendanceForm,ProjectForm,EmployeeForm,DateForm,EmpPaymentForm,MaterialForm,PaymentForm,KnownCalculateForm,MeasurementForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
import datetime
from django.utils.dateformat import DateFormat
from django.shortcuts import get_object_or_404
from django.db.models import Sum

# Create your views here.
def attendance(request) :
    names= ['Create New Employee','Attendance','Pay to Employee','List Employee']
    links = [reverse('new_employee'),reverse('attendance'),reverse('emp_payments'),reverse('employee')]
    submenus = create_sub(names,links)
    dateform = DateForm()
    if len(request.POST) <= 0:
        #If the page is loaded after a successful submission 
        success = request.GET.get('success')
        date = request.GET.get('date')
        return render(request , "attendance.html", {'title':'Attendance','dateform':dateform,'submenus':submenus,'success':success,'date':date})
    else :
        AttendanceFormSet = formset_factory(AttendanceForm,extra=0)
        dateform = DateForm(request.POST)
        if 'datebutton' in request.POST :
            if dateform.is_valid():
                data = dateform.cleaned_data
                date = data["date"]
                emps = Employee.objects.all()
                initial_data = []
                for emp in emps:
                    try:
                        att = Attendance.objects.filter(employee=emp).get(date=date)
                        initial_data.append({'employee':emp,'shift':att.shift,'project':att.project});
                    except:
                        initial_data.append({'employee':emp});
                formset = AttendanceFormSet(initial = initial_data)    
                return render(request, "attendance.html", {'date':date,'title':'Attendance','formset':formset,'dateform':dateform,'post':request.POST,'submenus':submenus})
            else:
                return render(request , "attendance.html", {'title':'Attendance','dateform':dateform,'submenus':submenus,'post':request.POST})
        else:
            formset = AttendanceFormSet(request.POST)
            mydate= request.POST.get('date')
            date= mydate
            if formset.is_valid():
                for f in formset:
                    cd = f.cleaned_data
                    emp = cd.get('employee')
                    proj = cd.get('project')
                    shift = cd.get('shift')
                    #date = datetime.datetime.strptime(date, '%m/%d/%y').strftime('%Y-%m-%d')
                    try:
                        att = Attendance.objects.filter(employee=emp).get(date=date)
                        att.project = proj
                        att.shift = shift
                        att.save()
                    except:
                        attendance = Attendance(date=date,shift=shift,employee=emp,project=proj)
                        attendance.save()
                    url = reverse('attendance')
                    
                    #return render(request , "attendance.html", {'title':'Attendance','emp':emp,'date':date,'submenus':submenus,'proj':proj})
                return HttpResponseRedirect("%s?success=1&date=%s"%(url,date))
            else:
                return render(request , "attendance.html", {'title':'Attendance','formset':formset,'dateform':dateform,'submenus':submenus,'post':request.POST})
        #form = AttendanceForm(request.POST)
        #if form.is_valid() :
         #   form.save(commit=True)
          #  return HttpResponseRedirect(reverse('attendance'))
        #else :
         #   return render(request, "attendance.html", {'title':'Attendance','dateform':dateform,'form': form,'errors':'Invalid Entry or required fields not filled','submenus':submenus})    

def home(request) :
    current_projects = Project.objects.exclude(end_date__lte=datetime.date.today())
    res = []

    for proj in current_projects:
        dict = {}
        dict['project'] = proj.name
        payments = Payment.objects.filter(project_id=proj,payment_from="CLIENT")
        total_payment = 0
        for payment in payments:
            total_payment+= payment.amount
        expenses = Expense.objects.filter(project_id=proj)
        total_expense = 0
        for exp in expenses:
            total_expense += exp.amount
        employees = Employee.objects.all()
        lab_amount = 0
        for emp in employees:
            a = Attendance.objects.filter(project=proj,employee=emp)
            if a.exists():
                shifts = (a.aggregate(total=Sum('shift'))['total'] or 0)/2
                lab_amount += shifts * emp.salary
        dict['total_payment'] = total_payment
        dict['total_cost'] = total_expense + lab_amount
        thresold_payment = dict['total_cost'] * 0.35 + dict['total_cost']
        thresold_balance = thresold_payment - total_payment
        dict['thresold_payment'] = thresold_payment
        dict['thresold_balance'] = thresold_balance
        if(total_expense >0 and thresold_payment > total_payment):
            res.append(dict)
    table = DefaultersTable(res)
    RequestConfig(request, paginate={"per_page": 15}).configure(table)
    context = {'table':table}
    return render(request, "home.html",context)

def projects(request) :
    names= ['Create New Project','OnGoing Projects','Completed Projects']
    links = [reverse('new_project'),reverse('projects'),reverse('old_projects')]
    submenus = create_sub(names,links)
    context = {'proj_selected':'current'}
    success = request.GET.get('success')
    current_projects = Project.objects.exclude(end_date__lte=datetime.date.today())
    table = ProjectTable(current_projects)
    RequestConfig(request, paginate={"per_page": 15}).configure(table)
    context.update({'table': table,'submenus':submenus,'success':success})
    return render(request, "projects.html" ,context)

def edit_project(request,projectid):
    names= ['Material Purchase','Make Payment','Invoices','Payments']
    links = ['/projects/'+projectid+'/purchases','/projects/'+projectid+'/payments','/projects/'+projectid+'/invoices','/projects/'+projectid+'/allpayments']
    submenus = create_sub(names,links)
    proj = get_object_or_404(Project, pk=projectid)
    context = {'proj_selected':'current'}
    
    if len(request.POST) <= 0:
        data = {'name':proj.name,'location':proj.location,'city':proj.city,'owner':proj.owner,'start_date':proj.start_date,'end_date':proj.end_date}
        form = ProjectForm(data)
        context.update({'title':'Update Project Details','form':form,'submenus':submenus})
        return render(request, "edit.html", context)
    else:
        form = ProjectForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            proj.name = cd.get('name')
            proj.location = cd.get('location')
            proj.city = cd.get('city')
            proj.owner = cd.get('owner')
            proj.start_date = cd.get('start_date')
            proj.end_date = cd.get('end_date')
            proj.save();
            url = reverse('projects')
            return HttpResponseRedirect("%s?success=1"%(url))
        else:
            context.update({'title':'Update Project Details','form':form,'submenus':submenus})
            return render(request, "edit.html",context)

def new_project(request):
    names= ['Create New Project','OnGoing Projects','Completed Projects']
    links = [reverse('new_project'),reverse('projects'),reverse('old_projects')]
    submenus = create_sub(names,links)
    context = {'proj_selected':'current'}
    if len(request.POST) <= 0:
        form = ProjectForm()
        context.update({'form':form,'entity':'Project','submenus':submenus})
        return render(request , "new.html", context)
    else :
        form = ProjectForm(request.POST)
        if form.is_valid() :
            form.save(commit=True)
            url = reverse('projects')
            return HttpResponseRedirect("%s?success=2"%(url))
        else :
            context.update({'title':'Create New Project','form': form,'entity':'Project','errors':'Invalid Entry or required fields not filled'})
            return render(request, "new.html", context )

def old_projects(request) :
    names= ['Create New Project','OnGoing Projects','Completed Projects']
    links = [reverse('new_project'),reverse('projects'),reverse('old_projects')]
    submenus = create_sub(names,links)
    context = {'proj_selected':'current'}
    current_projects = Project.objects.filter(end_date__lte=datetime.date.today())
    table = ProjectTable(current_projects)
    RequestConfig(request, paginate={"per_page": 15}).configure(table)
    context.update({'table': table,'submenus':submenus })
    return render(request, "projects.html" , context)

def employee(request) :
    names= ['Create New Employee','Attendance','Pay to Employee','List Employee']
    links = [reverse('new_employee'),reverse('attendance'),reverse('emp_payments'),reverse('employee')]
    submenus = create_sub(names,links)
    success = request.GET.get('success')
    table = EmployeeTable(Employee.objects.all())
    RequestConfig(request, paginate={"per_page": 15}).configure(table)
    return render(request, "employee.html" ,{'table':table,'submenus':submenus,'success':success })

def new_employee(request) :
    names= ['Create New Employee','Attendance','Pay to Employee','List Employee']
    links = [reverse('new_employee'),reverse('attendance'),reverse('emp_payments'),reverse('employee')]
    submenus = create_sub(names,links)
    if len(request.POST) <= 0:
        form = EmployeeForm()
        return render(request , "new.html", {'form':form,'entity':'Employee','submenus':submenus})
    else :
        form = EmployeeForm(request.POST)
        if form.is_valid() :
            form.save(commit=True)
            url = reverse('employee')
            return HttpResponseRedirect("%s?success=1"%(url))
        else :
            return render(request, "new.html", {'title':'Create New Project','form': form,'entity':'Employee','errors':'Invalid Entry or required fields not filled'})

def edit_employee(request,empid):
    names= ['Create New Employee','Attendance','Pay to Employee','List Employee']
    links = [reverse('new_employee'),reverse('attendance'),reverse('emp_payments'),reverse('employee')]
    submenus = create_sub(names,links)
    emp = get_object_or_404(Employee, pk=empid)
    if len(request.POST) <= 0:
        data = {"name":emp.name,"designation":emp.designation,	"category_id":format(emp.category_id.id),"salary":emp.salary,"phone_number":emp.phone_number,
                "joined_date":emp.joined_date,"status":emp.status,"outstanding":emp.outstanding}
        form = EmployeeForm(data)
        return render(request, "edit.html",{'title':'Update Employee Details','form':form,'submenus':submenus})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for key in cd:
                setattr(emp, key, cd.get(key))
            emp.save();
            url = reverse('employee')
            return HttpResponseRedirect("%s?success=2"%(url))
        else:
            return render(request, "edit.html",{'title':'Update Employee Details','form':form})



def emp_payments(request):
    names= ['Create New Employee','Attendance','Pay to Employee','List Employee']
    links = [reverse('new_employee'),reverse('attendance'),reverse('emp_payments'),reverse('employee')]
    submenus = create_sub(names,links)
    if len(request.POST) <= 0:
        form = EmpPaymentForm()
        return render(request, "emppayment.html",{'submenus':submenus,'form':form})
    else:
        form = EmpPaymentForm(request.POST)
        if form.is_valid() :
            form.save(commit=True)
            url = reverse('employee')
            return HttpResponseRedirect("%s?success=3"%(url))
        else:
            return render(request, "emppayment.html",{'submenus':submenus,'form':form,'errors':'Payment Failed. Please correct the following fields'})

def expense(request) :
    return render(request, "home.html")



def pay_slip(request):
    return render(request,"payslip.html",{"title":"Pay Slip"})

def material_purchase(request,projectid):
    names= ['Material Purchase','Make Payment','Invoices','Payments']
    links = ['/projects/'+projectid+'/purchases','/projects/'+projectid+'/payments','/projects/'+projectid+'/invoices','/projects/'+projectid+'/allpayments']
    submenus = create_sub(names,links)
    proj = Project.objects.get(pk=projectid)
    if len(request.POST) <= 0:
        material_form = MaterialForm()
        #If the page is loaded after a successful submission 
        success = request.GET.get('success')
        return render(request , "material.html", {'proj':proj,'submenus':submenus,'success':success,'form':material_form})
    else :
        material_form = MaterialForm(request.POST)
        if material_form.is_valid():
            obj = material_form.save()
            obj.project_id = proj
            obj.save()
            return HttpResponseRedirect('/projects/'+projectid+'/purchases'+"?success=1")
        else:
            return render(request , "material.html", {'proj':proj,'form':material_form,'submenus':submenus})

def edit_invoice(request,invoiceid):
    inv = get_object_or_404(Expense, pk=invoiceid)
    proj = inv.project_id
    projectid  = format(proj.id)
    names= ['Material Purchase','Make Payment','Invoices','Payments']
    links = ['/projects/'+projectid+'/purchases','/projects/'+projectid+'/payments','/projects/'+projectid+'/invoices','/projects/'+projectid+'/allpayments']
    submenus = create_sub(names,links)
    context = {'proj_selected':'current'}
    if len(request.POST) <= 0:
        data = {"date":inv.date,"invoice_no":inv.invoice_no,"particulars":inv.particulars,"amount":inv.amount,"balance":inv.balance,"paid_details":inv.paid_details,
                "paid_date":inv.paid_date,"project_id":inv.project_id,"dealer_id":format(inv.dealer_id.id),"category_id":format(inv.category_id.id),"remarks":inv.remarks}
        form = MaterialForm(data)
        context.update({'title':'Update Invoice Details','form':form,'submenus':submenus})
        return render(request,"edit.html",context)
    else:
        form = MaterialForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for key in cd:
                setattr(inv,key,cd.get(key))
            inv.save()
            return HttpResponseRedirect("/projects/"+projectid+"/invoices?success=1")
        else:
            context.update({'title':'Update Invoice Details','form':form,'submenus':submenus})
            return render(request, "edit.html",context)

def payments(request,projectid) :
    names= ['Material Purchase','Make Payment','Invoices','Payments']
    links = ['/projects/'+projectid+'/purchases','/projects/'+projectid+'/payments','/projects/'+projectid+'/invoices','/projects/'+projectid+'/allpayments']
    submenus = create_sub(names,links)
    proj = Project.objects.get(pk=projectid)
    invoices = Expense.objects.filter(balance__gt=0).filter(project_id=proj).order_by('date','amount')
    if len(request.POST) <= 0:
        payment_form = PaymentForm()
        success = request.GET.get('success')
        return render(request , "payment.html", {'proj':proj,'submenus':submenus,'success':success,'form':payment_form,'invoices':invoices})
    else:
        payment_form = PaymentForm(request.POST)
        invs = request.POST.getlist('invoices')
        if payment_form.is_valid():
            cd = payment_form.cleaned_data
            rem = cd.get('remaining_amount')
            amount = cd.get('amount')
            paid_details = cd.get('paid_details')
            paid_date = cd.get('paid_date')
            remarks = cd.get('remarks')
            payment = payment_form.save()
            payment.project_id = proj
            payment.save()
            selected = Expense.objects.filter(pk__in = invs).order_by('balance')
            for inv in selected:
                if amount > 0:
                    inv.paid_date = paid_date
                    p = PaymentExpense(bill=inv,payment=payment)
                    p.save()
                    if inv.balance <= amount:
                        amount -= inv.balance
                        inv.balance = 0
                    else:
                        inv.balance -= amount
                        amount = 0
                    inv.save()
            invoices = Expense.objects.filter(balance__gt=0).order_by('date','amount')                    
            #return render(request , "payment.html", {'proj':proj,'submenus':submenus,'form':payment_form,'post':request.POST,'invoices':invoices,'curr':curr,'invs':invs})
            return HttpResponseRedirect('/projects/'+projectid+'/payments'+"?success=1")
        else:
            return render(request , "payment.html", {'proj':proj,'submenus':submenus,'form':payment_form,'invoices':invoices})

def invoices(request,projectid):
    names= ['Material Purchase','Make Payment','Invoices','Payments']
    links = ['/projects/'+projectid+'/purchases','/projects/'+projectid+'/payments','/projects/'+projectid+'/invoices','/projects/'+projectid+'/allpayments']
    submenus = create_sub(names,links)
    context = {'proj_selected':'current'}
    success = request.GET.get('success')
    proj = get_object_or_404(Project, pk=projectid)
    invoices = Expense.objects.filter(project_id = proj)
    table = ExpenseTable(invoices)
    RequestConfig(request, paginate={"per_page": 15}).configure(table)
    context.update({'table': table,'submenus':submenus,'success':success,'title':'Invoice'})
    return render(request,"list.html",context)

def allpayments(request,projectid):
    names= ['Material Purchase','Make Payment','Invoices','Payments']
    links = ['/projects/'+projectid+'/purchases','/projects/'+projectid+'/payments','/projects/'+projectid+'/invoices','/projects/'+projectid+'/allpayments']
    submenus = create_sub(names,links)
    success = request.GET.get('success')
    proj = get_object_or_404(Project, pk=projectid)
    payments = Payment.objects.filter(project_id = proj,payment_from="CLIENT").order_by('paid_date')
    table = PaymentTable(payments)
    RequestConfig(request, paginate={"per_page": 15}).configure(table)
    context = {'proj_selected':'current','table': table,'submenus':submenus,'success':success,'title':'Payment'}
    return render(request,"list.html",context)

def billing(request) :
    return render(request, "home.html")

def measureandapprox(request) :
    names= ['Calculate By Total','Calculate By Measurements']
    links = [reverse('approximation'),reverse('measureandapprox')]
    submenus = create_sub(names,links)
    MeasurementFormSet = formset_factory(MeasurementForm,extra=1)
    formset = MeasurementFormSet()    
    return render(request, "measureandapprox.html", {'title':'Calculate by Measurements','formset':formset,'submenus':submenus})    

def approximation(request):
    names= ['Calculate By Total','Calculate By Measurements']
    links = [reverse('approximation'),reverse('measureandapprox')]
    submenus = create_sub(names,links)
    if len(request.POST) <= 0:
        knownform = KnownCalculateForm()
        return render(request , "approximation.html", {'knownform':knownform,'title':'Calculate by Total','submenus':submenus})
    else:
        knownform = KnownCalculateForm(request.POST)
        if knownform.is_valid():
            cd = knownform.cleaned_data
            total = cd['total']
            munit = cd ['munit']
            unitcost = cd['unitcost']
            cunit = cd['cunit']
            t = total
            if munit == '2':
                t = total / 12
            c = unitcost
            if cunit == '2':
                c = unitcost * 12
            cost = t * c
            return render(request,"approximation.html",{'knownform':knownform,'title':'Approximate Calculation','cost':cost,'munit':munit,'submenus':submenus})    
        else:
            return  render(request , "approximation.html", {'knownform':knownform,'title':'Approximate Calculation','submenus':submenus})
        
def create_sub(names,links):
    submenus = []
    for i in range(len(names)):
        submenus.append({'name':names[i],'url':links[i]})
    return submenus


    
