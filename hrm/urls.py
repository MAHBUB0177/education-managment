from django.urls import path

##### For Image Upload
from django.conf import settings
from django.conf.urls.static import static

from .views import *
urlpatterns = [
     #company-info
     path('hrm-company-info-view',hrm_company_info_view.as_view(),name='hrm-company-info-view'),
     path('hrm-company-info-insert',hrm_company_info_insert,name='hrm-company-info-insert'),
     path('hrm-company-info-edit/<slug:id>',hrm_company_info_edit,name='hrm-company-info-edit'),

     # office Info
     path('hrm-office-info-view',hrm_office_info.as_view(),name='hrm-office-info-view'),
     path('hrm-office-info-insert',hrm_office_info_insert,name='hrm-office-info-insert'),
     path('hrm-office-info-edit/<slug:id>',hrm_office_info_edit,name='hrm-office-info-edit'),

     # shift Info
     path('hrm-shift-info-view',hrm_office_shift_view.as_view(),name='hrm-shift-info-view'),
     path('hrm-shift-info-insert',hrm_office_shift_info_insert,name='hrm-shift-info-insert'),
     path('hrm-shift-info-edit/<slug:id>',hrm_office_shift_edit,name='hrm-shift-info-edit'),

     # shift Info
     path('hrm-emp-degree-info-view',hrm_employee_education_degree_view.as_view(),name='hrm-emp-degree-info-view'),
     path('hrm-emp-degree-info-insert',hrm_employee_education_degree_info_insert,name='hrm-emp-degree-info-insert'),
     path('hrm-emp-degree-info-edit/<slug:id>',hrm_employee_education_degree_edit,name='hrm-emp-degree-info-edit'),

     # department-info
     path('hrm-department-info/', Department_info_view.as_view(), name='hrm-department-info'),
     path('hrm-department-info-insert/',department_info_insert,name='hrm-department-info-insert'),
     path('hrm-department-info-edit/<slug:id>',department_info_edit,name='hrm-department-info-edit'),

     # HRM Designation Info
     path('hrm-designation-create',hrm_designation_create_view.as_view(),name='hrm-designation-create'),
     path('hrm-designation-info-insert',hrm_designation_info_insert,name='hrm-designation-info-insert'),
     path('hrm-designation-info-edit/<slug:id>',hrm_designation_info_edit,name='hrm-designation-info-edit'),

     # HRM employee type Info
     path('hrm-employee-type-create',hrm_employee_type_info_view.as_view(),name='hrm-employee-type-create'),
     path('hrm-employee-type-info-insert',hrm_employee_type_insert,name='hrm-employee-type-info-insert'),
     path('hrm-employee-type-info-edit/<slug:id>',hrm_employee_type,name='hrm-employee-type-info-edit'),

     # HRM salary scale Info
     path('hrm-employee-salary-scale-create',hrm_employee_salary_scale_info_view.as_view(),name='hrm-employee-salary-scale-create'),
     path('hrm-employee-salary-scale-insert',hrm_employee_salary_scale_info_insert,name='hrm-employee-salary-scale-insert'),
     path('hrm-employee-salary-scale-edit/<slug:id>',hrm_employee_salary_scale_info_edit,name='hrm-employee-salary-scale-edit'),

 # HRM salary scale description Info
     path('hrm-employee-salary-scale-details-create',hrm_salary_Scale_details.as_view(),name='hrm-employee-salary-scale-details-create'),
     path('hrm-employee-salary-scale-details-insert',hrm_salary_Scale_details_insert,name='hrm-employee-salary-scale-details-insert'),
     path('hrm-employee-salary-scale-details-edit/<slug:id>',hrm_salary_scale_details_edit,name='hrm-employee-salary-scale-details-edit'),

#Hrm salary Bonus 
     path('hrm-employee-salary-bonus-create',hrm_salary_bonus_create_view.as_view(),name='hrm-employee-salary-bonus-create'),
     path('hrm-employee-salary-bonus-insert',hrm_salary_bonus_insert,name='hrm-employee-salary-bonus-insert'),
     path('hrm-employee-salary-bonus-edit/<slug:id>',hrm_salary_bonus_details_edit,name='hrm-employee-salary-bonus-edit'),

#Hrm Extra allownce 
     path('hrm-employee-extra-allownce-create',hrm_extra_allownce_create_view.as_view(),name='hrm-employee-extra-allownce-create'),
     path('hrm-employee-extra-allownce-insert',hrm_extra_allownce_create_insert,name='hrm-employee-extra-allownce-insert'),
     path('hrm-employee-extra-allownce-edit/<slug:id>',hrm_extra_allownce_edit,name='hrm-employee-extra-allownce-edit'),

#Hrm bank info 
     path('hrm-bank-info-create',hrm_bank_info_create_view.as_view(),name='hrm-bank-info-create'),
     path('hrm-bank-info-insert',hrm_bank_info_insert,name='hrm-bank-info-insert'),
     path('hrm-bank-info-edit/<slug:id>',hrm_bank_info_edit,name='hrm-bank-info-edit'),

#Hrm employee info 
     path('hrm-employee-info-create',hrm_employee_info_create_view.as_view(),name='hrm-employee-info-create'),
     path('hrm-employee-info-insert',hrm_employee_info_insert,name='hrm-employee-info-insert'),
     path('hrm-employee-info-edit/<slug:id>',hrm_employee_info_edit,name='hrm-employee-info-edit'),

#Hrm employee experiance info 
     path('hrm-employee-experiance-info-create',hrm_employee_experiance_info_create_view.as_view(),name='hrm-employee-experiance-info-create'),
     path('hrm-employee-experiance-info-insert',hrm_employee_experiance_info_insert,name='hrm-employee-experiance-info-insert'),
     path('hrm-employee-experiance-info-edit/<slug:id>',hrm_employee_experiance_info_edit,name='hrm-employee-experiance-info-edit'),

#Hrm employee nomineee info 
     path('hrm-employee-nominee-info-create',hrm_employee_nominee_info_create_view.as_view(),name='hrm-employee-nominee-info-create'),
     path('hrm-employee-nominee-info-insert',hrm_employee_nominee_info_insert,name='hrm-employee-nominee-info-insert'),
     path('hrm-employee-nominee-edit/<slug:id>',hrm_employee_nominee_info_edit,name='hrm-employee-nominee-edit'),

#Hrm  document type 
     path('hrm-document-type-create',hrm_document_type_create_view.as_view(),name='hrm-document-type-create'),
     path('hrm-document-type-insert',hrm_document_type_insert,name='hrm-document-type-insert'),
     path('hrm-document-type-edit/<slug:id>',hrm_document_type_edit,name='hrm-document-type-edit'),

#Hrm employee document info 
     path('hrm-employee-document-info-create',hrm_employee_document_info_create_view.as_view(),name='hrm-employee-document-info-create'),
     path('hrm-employee-document-info-insert',hrm_employee_document_info_insert,name='hrm-employee-document-info-insert'),
     path('hrm-employee-document-edit/<slug:id>',hrm_employee_document_info_edit,name='hrm-employee-document-edit'),

#Hrm employee leave info 
     path('hrm-employee-leave-info-create',hrm_employee_leave_info_create_view.as_view(),name='hrm-employee-leave-info-create'),
     path('hrm-employee-leave-info-insert',hrm_employee_leave_info_insert,name='hrm-employee-leave-info-insert'),
     path('hrm-employee-leave-edit/<slug:id>',hrm_employee_leave_info_edit,name='hrm-employee-leave-edit'),

#Hrm employee leave application 
     path('hrm-employee-leave-application-create',hrm_employee_leave_application_create_view.as_view(),name='hrm-employee-leave-application-create'),
     path('hrm-employee-leave-application-insert',hrm_employee_leave_application_insert,name='hrm-employee-leave-application-insert'),
     path('hrm-employee-leave-application-edit/<slug:id>',hrm_employee_leave_application_edit,name='hrm-employee-leave-application-edit'),
     path('hrm-employee-leave-application-approve/<slug:id>',hrm_employee_leave_application_approve,name='hrm-employee-leave-application-approve'),
    

     


#Hrm employee training 
     path('hrm-employee-training-info-create',hrm_employee_training_info_create_view.as_view(),name='hrm-employee-training-info-create'),
     path('hrm-employee-training-info-insert',hrm_employee_training_info_insert,name='hrm-employee-training-info-insert'),
     path('hrm-employee-training-info-edit/<slug:id>',hrm_employee_training_info_edit,name='hrm-employee-training-info-edit'),
#Hrm Pay bill 
     path('hrm-pay-bill-info-create',hrm_pay_bill_info_create_view.as_view(),name='hrm-pay-bill-info-create'),
     path('hrm-pay-bill-info-insert',hrm_pay_bill_info_insert,name='hrm-pay-bill-info-insert'),
     path('hrm-pay-bill-info-edit/<slug:id>',hrm_pay_bill_info_edit,name='hrm-pay-bill-info-edit'),



]