import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Project(models.Model):
    name = models.CharField("Project Title",max_length=100)
    location = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    owner = models.CharField("Client",max_length=100)
    start_date = models.DateField('Date of Commencement')
    end_date = models.DateField('Date of Completion',blank=True,null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def current_project(self):
        if self.end_date is not None and self.end_date <= datetime.date.today():
            return False
        else:
            return True
    current_project.admin_order_field = 'end_date'
    current_project.boolean = True
    current_project.short_description = 'Ongoing Project?'

class Dealer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Expense(models.Model):
    WAY_OF_PAYMENT = (
        ("CASH","CASH"),
        ("CREDIT","CREDIT"),
    )
    date = models.DateField('Date',blank=True,null=True)
    invoice_no = models.CharField(max_length=20,blank=True,null=True)
    particulars = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    paid_details = models.CharField(max_length=30,blank=True,null=True,choices=WAY_OF_PAYMENT)
    paid_date = models.DateField('Paid Date',blank=True,null=True)
    project_id = models.ForeignKey(Project,blank=True,null=True)
    dealer_id = models.ForeignKey(Dealer,blank=True,null=True)
    category_id = models.ForeignKey(Category,blank=True,null=True)
    remarks = models.CharField(default='',max_length=300,blank=True,null=True)
    

    def __str__(self):              # __unicode__ on Python 2
        return "#"+self.invoice_no+'  | '+self.date.strftime("%d/%m/%Y")+" | Amount => "+format(self.amount)+" | Balance =>"+format(self.balance)+" | "+self.particulars

class Employee(models.Model):
    EMPLOYEE_STATUS = (
        ("ACTIVE","ACTIVE"),
        ("INACTIVE","INACTIVE"),
    )
    name = models.CharField('Name',max_length=100)
    designation = models.CharField('Designation',max_length=100,blank=True,null=True)
    salary = models.IntegerField('Salary',default=0,blank=True,null=True)
    joined_date = models.DateField('Date of Joining',blank=True,null=True)
    status = models.CharField('Status',max_length=30,choices=EMPLOYEE_STATUS,default="ACTIVE")
    outstanding = models.IntegerField('Outstanding',default=0,blank=True,null=True)
    phone_number = models.CharField("Phone Number",max_length=15,blank=True,null=True)
    category_id = models.ForeignKey(Category,blank=True,null=True)

    def __str__(self):
        return self.name

class Contractor(models.Model):
    STATUS = (
        ("ACTIVE","ACTIVE"),
        ("INACTIVE","INACTIVE"),
    )
    name = models.CharField('Name',max_length=100)
    phone_number = models.CharField("Phone Number",max_length=15,blank=True,null=True)
    status = models.CharField('Status',max_length=30,choices=STATUS,default="ACTIVE")
    remarks = models.CharField(default='',max_length=300,blank=True,null=True)

    def __str__(self):
        return self.name
    
class Contract(models.Model):
    contractor = models.ForeignKey(Contractor)
    project = models.ForeignKey(Project)
    cost = models.IntegerField('Cost',default=0,blank=True,null=True)
    start_date = models.DateField('Date of Commencement')
    end_date = models.DateField('Date of Completion',blank=True,null=True)
    remarks = models.CharField(default='',max_length=300,blank=True,null=True)


class ContractPayment(models.Model):
    contractor = models.ForeignKey(Contractor)
    project = models.ForeignKey(Project)
    amount = models.IntegerField('Amount')
    paid_date = models.DateField('Paid Date')
    remarks = models.CharField(default='',max_length=300,blank=True,null=True)

    def __str__(self):
        return ' '+format(self.contractor)+' '+format(self.project)+' '+format(self.amount) 

class Attendance(models.Model):
    date = models.DateField("Date", default= datetime.date.today() - datetime.timedelta(days = 1))
    WORK_SHIFT = (
        (0,"A"),
        (1,"/"),
        (2,"X"),
        (3,"XI"),
        (4,"XX"),
        (5,"XXI"),
        (6,"XXX"),
        (6,"XXXI"),
        (6,"XXXX"),
    )
    shift = models.IntegerField(choices=WORK_SHIFT,default=2)
    employee = models.ForeignKey(Employee)
    project = models.ForeignKey(Project,blank=True,null=True)

    def __str__(self):
            return "%s worked %s shift(s) on %s" % \
                   (self.employee_id , self.shift/2 , self.date)
				   
    def no_of_shifts(self):
        return self.shift/2

class EmployeePayment(models.Model):
    TYPE = (
            ("ADVANCE","ADVANCE"),
            ("SALARY","SALARY"),
            ("TRAVEL","TRAVEL"),
            ("OTHER","OTHER"),
            ("TRANSFERIN","TRANSFERIN"),
            ("TRANSFEROUT","TRANSFEROUT"),
        )
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
    amount = models.IntegerField("Amount",default=0)
    paid_date = models.DateField('Paid Date')
    month = models.IntegerField("For the Month",choices=MONTH,default=1)
    year = models.IntegerField("For the Year",default=2015)
    type = models.CharField('Payment As',max_length=30,choices=TYPE,default="SALARY")
    remarks = models.CharField('Remarks',max_length=300,blank=True,null=True)
    employee = models.ForeignKey(Employee)

class Payment(models.Model):
    WAY_OF_PAYMENT = (
        ("CASH","CASH"),
        ("CHEQUE","CHEQUE"),
        ("RTGS","RTGS"),
    )
    PAYMENT_FROM = (
        ("CLIENT","CLIENT"),
        ("omar & assosciates","omar & assosciates"),
    )
    amount = models.IntegerField(default=0)
    paid_details = models.CharField('Paid By',max_length=30,blank=True,null=True,choices=WAY_OF_PAYMENT)
    paid_date = models.DateField('Date Of Payment',blank=True,null=True)
    payment_from = models.CharField(max_length=30,choices=PAYMENT_FROM,default="CLIENT")
    project_id = models.ForeignKey(Project,blank=True,null=True)
    remarks = models.CharField('Remarks',default='',max_length=300,blank=True,null=True)

class PaymentExpense(models.Model):
    payment = models.ForeignKey(Payment)
    bill = models.ForeignKey(Expense)
