from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Project, Expense , Category, Dealer, Employee, Attendance, Payment,EmployeePayment
# Register your models here.



class ExpenseInline(admin.TabularInline):
    model = Expense
    extra = 3
    fieldsets = (
        (None, {
            'fields': ('date','dealer_id','invoice_no','amount','particulars','paid_details','paid_date','project_id','category_id')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('remarks',)
        }),
    )

class AttendanceInline(admin.TabularInline):
    model = Attendance
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','location','city','current_project')
    list_filter = ['owner','city']
    inlines = [ExpenseInline]

        
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date','invoice_no','particulars','amount','paid_details','paid_date','project_id')
    list_filter = ['category_id','project_id','dealer_id']
    fieldsets = (
        (None, {
            'fields': ('date','dealer_id','invoice_no','amount','particulars','paid_details','paid_date','project_id','category_id','remarks')
        }),
    )

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','designation','category_id','salary','phone_number')
    list_filter = ['category_id','designation']
    inlines = [AttendanceInline]

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee_id','date','shift','project')
    list_filter = ['employee_id','date','project']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('paid_date','amount','paid_details','project_id')
    list_filter = ['project_id','amount','paid_date']

AdminSite.site_header = "Omar and Assosciates"

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Dealer)
admin.site.register(Expense,ExpenseAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(EmployeePayment)
