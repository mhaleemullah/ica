import django_tables2 as tables
from projects.models import Attendance,Project,Employee,Expense,Contractor,Contract
from django_tables2.utils import A

class ProjectTable(tables.Table):
    location = tables.Column(verbose_name="Location")
    city = tables.Column(verbose_name="City")
    name = tables.LinkColumn('edit_project',args=[A('pk')])
    
    class Meta: 
        model = Project
        sequence = ("name","location","city")
        fields = ("name","location","city","owner","start_date","end_date")
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}

class DefaultersTable(tables.Table):
    project = tables.Column(verbose_name="Project")
    total_cost = tables.Column(verbose_name="Project Cost")
    total_payment = tables.Column(verbose_name="Payment Received")
    thresold_payment = tables.Column(verbose_name="Expected Payment")
    thresold_balance = tables.Column(verbose_name="Thresold Balance")

    class Meta:
        sequence = ("project","total_cost","thresold_payment","total_payment","thresold_balance")
        attrs = {'class':'paleblue'}

class DealersWithOutstanding(tables.Table):
    dealer_name = tables.Column(verbose_name="Dealer")
    outstanding = tables.Column(verbose_name="Outstanding")

    class Meta:
        attrs = {'class':'paleblue'}

class ExpenseTable(tables.Table):
    amount = tables.LinkColumn('edit_invoice',args=[A('pk')])
	
    
    class Meta: 
        model = Expense
        sequence = ("invoice_no","date","amount","balance","particulars","dealer_id","category_id","remarks")
        fields = ("invoice_no","date","amount","balance","particulars","dealer_id","category_id","remarks")
        attrs = {"class": "paleblue invoice_table"}

class PaymentTable(tables.Table):
	

    class Meta:
        model = Expense
        sequence = ("paid_date","amount","paid_details","project_id","remarks")
        fields = ("paid_date","amount","paid_details","project_id","remarks")
        attrs = {"class": "paleblue payment_table"}

class EmployeeTable(tables.Table):
    name = tables.LinkColumn('edit_employee',args=[A('pk')])
    category_id = tables.Column(verbose_name="Category")
    class Meta:
        model = Employee
        sequence = ("name","designation","category_id","salary","phone_number","joined_date"
                    ,"status","outstanding")
        fields = ("name","designation","category_id","salary","phone_number","joined_date"
                    ,"status","outstanding")
        attrs = {"class": "paleblue"}

class ContractorTable(tables.Table):
    
    class Meta:
        model = Contractor
        attrs = {"class": "paleblue"}

class ContractTable(tables.Table):
    
    class Meta:
        model = Contract
        attrs = {"class": "paleblue"}
