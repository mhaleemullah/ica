from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.core.urlresolvers import reverse
from projects.models import Attendance,Project,Employee,Expense,Category,Dealer,PaymentExpense,Payment
from projects.tables  import DealersWithOutstanding,DefaultersTable
from django_tables2   import RequestConfig
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from projects.forms import SelectDealerForm,SelectContractForm,SelectProjectForm,PaySlipForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
import datetime
from django.utils.dateformat import DateFormat
from django.shortcuts import get_object_or_404
from django.db.models import Sum

def reports(request):
    names= ['Pay Slip','Project Labor Report','Project Material Report','Project Total Cost','Dealer Outstandings','Contract Report']
    links = [reverse('pay_slip'),reverse('labor_report'),reverse('material_cost'),reverse('total_cost'),reverse('dealer_outstanding'),reverse('contract_report')]
    submenus = create_sub(names,links)

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
    context = {'table':table,'submenus':submenus}
    return render(request, "home.html",context)



def pay_slip(request):
    names= ['Pay Slip','Project Labor Report','Project Material Report','Project Total Cost','Dealer Outstandings','Contract Report']
    links = [reverse('pay_slip'),reverse('labor_report'),reverse('material_cost'),reverse('total_cost'),reverse('dealer_outstanding'),reverse('contract_report')]
    submenus = create_sub(names,links)
    return None


def labor_report(request):
    names= ['Pay Slip','Project Labor Report','Project Material Report','Project Total Cost','Dealer Outstandings','Contract Report']
    links = [reverse('pay_slip'),reverse('labor_report'),reverse('material_cost'),reverse('total_cost'),reverse('dealer_outstanding'),reverse('contract_report')]
    submenus = create_sub(names,links)
    return None


def material_cost(request):
    names= ['Pay Slip','Project Labor Report','Project Material Report','Project Total Cost','Dealer Outstandings','Contract Report']
    links = [reverse('pay_slip'),reverse('labor_report'),reverse('material_cost'),reverse('total_cost'),reverse('dealer_outstanding'),reverse('contract_report')]
    submenus = create_sub(names,links)
    return None


def dealer_outstanding(request):
    names= ['Pay Slip','Project Labor Report','Project Material Report','Project Total Cost','Dealer Outstandings','Contract Report']
    links = [reverse('pay_slip'),reverse('labor_report'),reverse('material_cost'),reverse('total_cost'),reverse('dealer_outstanding'),reverse('contract_report')]
    submenus = create_sub(names,links)

    context = {'submenus':submenus,}

    if len(request.POST) <= 0:
        select_dealer_form = SelectDealerForm()
        res = []
        total_outstanding = 0
        dealers = Dealer.objects.all()
        for dealer in dealers:
            invoices = Expense.objects.filter(dealer_id=dealer,balance__gt=0)
            outstanding = invoices.aggregate(total=Sum('balance'))['total'] or 0
            if outstanding > 0:
                total_outstanding += outstanding
                res.append({'dealer_name':dealer.name,'outstanding':outstanding})
        table = DealersWithOutstanding(res)
        RequestConfig(request, paginate={"per_page": 15}).configure(table)
        context.update({'table':table,'total':total_outstanding,'first_time':1,'select_dealer_form':select_dealer_form})
        return render(request,"dealeroutstanding.html",context)
    else:
        select_dealer_form = SelectDealerForm(request.POST)
        if select_dealer_form.is_valid():
            data = select_dealer_form.cleaned_data
            dealer = data['dealer']
            projects = Project.objects.all()
            for proj in projects:
                invoices = Expense.objects.filter(project_id=proj,dealer_id=dealer,balance__gt=0)



    return None


def total_cost(request):
    names= ['Pay Slip','Project Labor Report','Project Material Report','Project Total Cost','Dealer Outstandings','Contract Report']
    links = [reverse('pay_slip'),reverse('labor_report'),reverse('material_cost'),reverse('total_cost'),reverse('dealer_outstanding'),reverse('contract_report')]
    submenus = create_sub(names,links)
    return None


def contract_report(request):
    names= ['Pay Slip','Project Labor Report','Project Material Report','Project Total Cost','Dealer Outstandings','Contract Report']
    links = [reverse('pay_slip'),reverse('labor_report'),reverse('material_cost'),reverse('total_cost'),reverse('dealer_outstanding'),reverse('contract_report')]
    submenus = create_sub(names,links)
    return None

def create_sub(names,links):
    submenus = []
    for i in range(len(names)):
        submenus.append({'name':names[i],'url':links[i]})
    return submenus