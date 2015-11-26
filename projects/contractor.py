from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.core.urlresolvers import reverse
from projects.models import Attendance,Project,Employee,Expense,Category,Dealer,PaymentExpense,Payment,Contractor,Contract
from projects.tables  import ProjectTable,EmployeeTable,ExpenseTable,PaymentTable,ContractorTable,ContractTable
from django_tables2   import RequestConfig
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from projects.forms import AttendanceForm,ProjectForm,EmployeeForm,DateForm,EmpPaymentForm,MaterialForm,PaymentForm,ContractorForm,ContractForm,SelectContractForm,ConPaymentForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
import datetime
from django.utils.dateformat import DateFormat
from django.shortcuts import get_object_or_404

def contractors(request):
    names= ['Create New Contractor','Create New Contract','Pay to Contractor','List Contractor','List Contracts']
    links = [reverse('new_contractor'),reverse('new_contract'),reverse('con_payment'),reverse('contractors'),reverse('contracts')]
    submenus = create_sub(names,links)
    contractors = Contractor.objects.all()
    table = ContractorTable(contractors)
    RequestConfig(request, paginate={"per_page": 15}).configure(table)
    return render(request, "list.html" ,{'submenus':submenus,'table':table,'title':'Contractor' })

def contracts(request):
    names= ['Create New Contractor','Create New Contract','Pay to Contractor','List Contractor','List Contracts']
    links = [reverse('new_contractor'),reverse('new_contract'),reverse('con_payment'),reverse('contractors'),reverse('contracts')]
    submenus = create_sub(names,links)
    contracts = Contract.objects.all()
    table = ContractTable(contracts)
    RequestConfig(request, paginate={"per_page": 15}).configure(table)
    return render(request, "list.html" ,{'submenus':submenus,'table':table,'title':'Contract' })


def new_contractor(request) :
    names= ['Create New Contractor','Create New Contract','Pay to Contractor','List Contractor','List Contracts']
    links = [reverse('new_contractor'),reverse('new_contract'),reverse('con_payment'),reverse('contractors'),reverse('contracts')]
    submenus = create_sub(names,links)
    if len(request.POST) <= 0:
        form = ContractorForm()
        context = {'form':form,'entity':'Contractor','submenus':submenus}
        return render(request , "new.html", context)
    else :
        form = ContractorForm(request.POST)
        if form.is_valid() :
            form.save(commit=True)
            url = reverse('contractors')
            return HttpResponseRedirect("%s?success=1"%(url))
        else :
            context = {'entity':'Contractor','form': form,'errors':'Invalid Entry or required fields not filled'}
            return render(request, "new.html", context )

def new_contract(request) :
    names= ['Create New Contractor','Create New Contract','Pay to Contractor','List Contractor','List Contracts']
    links = [reverse('new_contractor'),reverse('new_contract'),reverse('con_payment'),reverse('contractors'),reverse('contracts')]
    submenus = create_sub(names,links)
    if len(request.POST) <= 0:
        form = ContractForm()
        context = {'form':form,'entity':'Contract','submenus':submenus}
        return render(request , "new.html", context)
    else :
        form = ContractForm(request.POST)
        if form.is_valid() :
            form.save(commit=True)
            url = reverse('contracts')
            return HttpResponseRedirect("%s?success=1"%(url))
        else :
            context = {'entity':'Contract','form': form,'errors':'Invalid Entry or required fields not filled'}
            return render(request, "new.html", context )

def con_payment(request) :
    names= ['Create New Contractor','Create New Contract','Pay to Contractor','List Contractor','List Contracts']
    links = [reverse('new_contractor'),reverse('new_contract'),reverse('con_payment'),reverse('contractors'),reverse('contracts')]
    submenus = create_sub(names,links)
    if len(request.POST) <= 0:
        form = ConPaymentForm()
        context = {'form':form,'title':'Enter the Payment Details','submenus':submenus,'first_time':1}
        return render(request , "contractpayment.html", context)
    else:
        form = ConPaymentForm(request.POST)
        if form.is_valid() :
            cd = form.cleaned_data
            proj = cd['project']
            contractor = cd['contractor']
            amount = cd['amount']
            contract = Contract.objects.filter(project=proj,contractor=contractor)
            if not contract.exists():
                return render(request, "contractpayment.html",{'submenus':submenus,'form':form,'errors':'There are no Contract between this contractor and the project'})
            form.save(commit=True)
            url = reverse('contractors')
            return HttpResponseRedirect("%s?success=3"%(url))
        else:
            return render(request, "emppayment.html",{'submenus':submenus,'form':form,'errors':'Payment Failed. Please correct the following fields'})










def create_sub(names,links):
    submenus = []
    for i in range(len(names)):
        submenus.append({'name':names[i],'url':links[i]})
    return submenus
