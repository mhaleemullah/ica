"""oatest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from projects import admin_custom as admin
from projects import views,reports,contractor

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$',views.home,name='home'),
    url(r'^attendance$', views.attendance, name='attendance'),
	url(r'^approximation$', views.approximation, name='approximation'),
	url(r'^measureandapprox$', views.measureandapprox, name='measureandapprox'),
	url(r'^employee$', views.employee, name='employee'),
	url(r'^employee/([0-9]+)/$', views.edit_employee, name='edit_employee'),
	url(r'^employee/payments$', views.emp_payments, name='emp_payments'),
	url(r'^employee/create$', views.new_employee, name='new_employee'),
	url(r'^reports$', reports.reports, name='reports'),
	url(r'^reports/payslip$', reports.pay_slip, name='pay_slip'),
	url(r'^reports/laborreport$', reports.labor_report, name='labor_report'),
	url(r'^reports/materialcost$', reports.material_cost, name='material_cost'),
	url(r'^reports/dealeroutstanding$', reports.dealer_outstanding, name='dealer_outstanding'),
	url(r'^reports/totalcost$', reports.total_cost, name='total_cost'),
	url(r'^reports/contractpayments$', reports.contract_report, name='contract_report'),
	url(r'^projects$', views.projects, name='projects'),
	url(r'^projects/([0-9]+)/$', views.edit_project,name='edit_project'),
	url(r'^projects/([0-9]+)/purchases$', views.material_purchase,name='material_purchase'),
	url(r'^projects/([0-9]+)/payments$', views.payments, name='payments'),
	url(r'^projects/([0-9]+)/allpayments$', views.allpayments, name='allpayments'),
	url(r'^projects/([0-9]+)/invoices$', views.invoices, name='invoices'),
	url(r'^invoices/([0-9]+)$', views.edit_invoice, name='edit_invoice'),
	url(r'^projects/create$', views.new_project, name='new_project'),
	url(r'^projects/completed$', views.old_projects, name='old_projects'),
	url(r'^contractor$', contractor.contractors, name='contractors'),
	url(r'^contractor/newcontractor$', contractor.new_contractor, name='new_contractor'),
	url(r'^contractor/newcontract$', contractor.new_contract, name='new_contract'),
	url(r'^contractor/conpayment$', contractor.con_payment, name='con_payment'),
	url(r'^contractor/contracts$', contractor.contracts, name='contracts'),
	url(r'^billing$', views.billing, name='billing'),
	url(r'^expense$', views.expense, name='expense'),
]
