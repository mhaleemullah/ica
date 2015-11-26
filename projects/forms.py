from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from django import forms
from projects.models import Attendance,Project,Employee,EmployeePayment,Expense,Payment,Dealer,Contractor,Contract,ContractPayment
from functools import partial
from django.contrib.admin.widgets import FilteredSelectMultiple

class AttendanceForm(forms.ModelForm):
    #employee = forms.ChoiceField(
    #    widget=forms.TextInput(attrs={'readonly':'readonly'})
    #)
    class Meta:
        model = Attendance
        fields = ['employee', 'shift', 'project']

    def clean(self):
        form_data = self.cleaned_data
        if form_data['shift'] != 0 and form_data['project'] is None :
            self._errors["project"] = ["Should fill the project if employee is not absent"]
            del form_data['project']
        return form_data
        
    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'attendance'
        self.helper.add_input(Submit('submit', 'Submit'))
        #self.fields['employee'].widget.attrs['disabled'] = 'true'

class PaymentForm(forms.ModelForm):
    beneficiary = (
            (1,"Invoices"),
            (2,"omar & assosciates")
        )
    payment_towards = forms.ChoiceField(label="Payment Towards",choices=beneficiary,initial=1)

    remaining_amount = forms.CharField(label='Remaining Amount',required=False,initial=0)
    #invoices = forms.ModelMultipleChoiceField(queryset=qs,widget=forms.CheckboxSelectMultiple()) #widget=FilteredSelectMultiple("Invoices",is_stacked=False

    class Meta:
        model = Payment
        exclude = ('project_id',)

    def clean(self):
        form_data = self.cleaned_data
        return form_data
        
    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'payment_form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'payment'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.fields['remaining_amount'].widget.attrs['readonly'] = 'readonly'

        self.fields['paid_date'].widget.attrs['class'] = 'dateinput'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'new_project'
        self.helper.add_input(Submit('submit', 'Submit'))
        super(ProjectForm, self).__init__(*args, **kwargs)
                    
class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'new_employee'
        self.helper.add_input(Submit('submit', 'Submit'))
        super(EmployeeForm, self).__init__(*args, **kwargs)

class DateForm(forms.Form):
    date = forms.DateField(label="Date",widget=forms.DateInput(attrs={'class':'dateinput'}));

    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'uniForm'
        self.helper.form_action = 'attendance'
        self.helper.add_input(Submit('submit', 'Go'))
        super(DateForm, self).__init__(*args, **kwargs)
    
class EmpPaymentForm(forms.ModelForm):
    
    class Meta:
        model = EmployeePayment
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        super(EmpPaymentForm, self).__init__(*args, **kwargs)

class ConPaymentForm(forms.ModelForm):
    
    class Meta:
        model = ContractPayment
        exclude = ()

    def clean(self):
        form_data = self.cleaned_data
        contract = Contract.objects.filter(project=form_data['project'],contractor=form_data['contractor'])
        if not contract.exists():
            self._errors['contractor'] = ["There are no contract between this contractor and the project"]
        return form_data
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        super(ConPaymentForm, self).__init__(*args, **kwargs)

class KnownCalculateForm(forms.Form):
    UNITS = (
            (1,"Feet"),
            (2,"Inches")
        )
    total = forms.IntegerField(label="Measured Units")
    munit = forms.ChoiceField(label="in",choices=UNITS,initial=1)
    unitcost = forms.IntegerField(label="Cost")
    cunit = forms.ChoiceField(label="per",choices=UNITS)
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'uniForm'
        self.helper.form_action = 'approximation'
        self.helper.add_input(Submit('submit', 'Calculate'))
        super(KnownCalculateForm, self).__init__(*args, **kwargs)

class MeasurementForm(forms.Form):
    UNITS = (
            (1,"Feet"),
            (2,"Inches")
        )
    height = forms.IntegerField(label="Height")
    width = forms.IntegerField(label="Width")
    length = forms.IntegerField(label="Length")
    munit = forms.ChoiceField(label="in",choices=UNITS,initial=1)
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'uniForm MeasurementForm'
        self.helper.form_action = 'measureandapprox'
        self.helper.add_input(Submit('submit', 'Calculate'))
        super(MeasurementForm, self).__init__(*args, **kwargs)

class PaySlipForm(forms.Form):
    qs = Employee.objects.exclude(status="INACTIVE")
    MONTH = (
            (1,"January"),
            (2,"Febrauary"),
            (3,"March"),
            (4,"April"),
            (5,"May"),
            (6,"June"),
            (7,"July"),
            (8,"August"),
            (9,"September"),
            (10,"October"),
            (11,"November"),
            (12,"December"),
        )
    employee = forms.ModelChoiceField(queryset=qs)
    month = forms.ChoiceField(choices=MONTH)
    year = forms.IntegerField(initial=2015)
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'uniForm'
        self.helper.form_action = 'attendance'
        self.helper.add_input(Submit('submit', 'Go'))
        super(PaySlipForm, self).__init__(*args, **kwargs)

class SelectContractForm(forms.Form):
    qs = Contractor.objects.all()
    contractor = forms.ModelChoiceField(queryset=qs)
    pqs = Project.objects.all()
    project = forms.ModelChoiceField(queryset=pqs)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'uniForm'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Go'))
        super(SelectContractForm, self).__init__(*args, **kwargs)
    
class SelectProjectForm(forms.Form):
    qs = Project.objects.all()
    project = forms.ModelChoiceField(queryset=qs)
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'uniForm'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Go'))
        super(SelectProjectForm, self).__init__(*args, **kwargs)

class SelectDealerForm(forms.Form):
    qs = Dealer.objects.all()
    dealer = forms.ModelChoiceField(queryset=qs)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'uniForm'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Go'))
        super(SelectDealerForm, self).__init__(*args, **kwargs)

class MaterialForm(forms.ModelForm):

    class Meta:
        model = Expense
        exclude = ('project_id',)
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'material_purchase'
        self.helper.add_input(Submit('submit', 'Submit'))
        super(MaterialForm, self).__init__(*args, **kwargs)

class ContractorForm(forms.ModelForm):

    class Meta:
        model = Contractor
        exclude = ('project_id',)
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'new_contractor'
        self.helper.add_input(Submit('submit', 'Submit'))
        super(ContractorForm, self).__init__(*args, **kwargs)

class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        exclude = ('project_id',)
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'new_contractor'
        self.helper.add_input(Submit('submit', 'Submit'))
        super(ContractForm, self).__init__(*args, **kwargs)
