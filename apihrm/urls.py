from django.urls import path

##### For Image Upload
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('apiauth-department-api',departmentApiView.as_view(),name='apiauth-department-api'),
    path('apihrm-designation-api',designationApiView.as_view(),name='apihrm-designation-api'),
    path('apihtm-companyInfo-api',companyInfoApiView.as_view(),name='apihtm-companyInfo-api'),
    path('apihrm-officeInfo-api',OfficeInfoApiView.as_view(),name='apihrm-officeInfo-api'),
    path('apihrm-shiftInfo-api',ShiftInfoApiView.as_view(),name='apihrm-shiftInfo-api'),
    path('apiauth-emp-degree-api',EmployeeDegreeApiView.as_view(),name='apiauth-emp-degree-api'),
    path('apihrm-employeeType-api',EmployeeTypeApiView.as_view(),name='apihrm-employeeType-api'),
    path('apihrm-salaryScaleType-api',SalaryScaleTypeApiView.as_view(),name='apihrm-salaryScaleType-api'),
    path('apihrm-salaryScale-details-api',SalaryScaleDetailasTypeApiView.as_view(),name='apihrm-salaryScale-details-api'),
    path('apihrm-salaryBonus-api',SalaryBonusApiView.as_view(),name='apihrm-salaryBonus-api'),
    path('apihrm-extra-alownace-api',ExtraAlownceApiView.as_view(),name='apihrm-extra-alownace-api'),
    path('apihrm-Bank-api',BankTypeApiView.as_view(),name='apihrm-Bank-api'),
    path('apihrm-employee-api',EmployeeINfoApiView.as_view(),name='apihrm-employee-api')
    ,path('apihrm-employeeExperiance-api',EmployeeExperianceApiView.as_view(),name='apihrm-employeeExperiance-api'),
    path('apihrm-empNominee-api',EmployeeNomineeApiView.as_view(),name='apihrm-empNominee-api'),
    path('apihrm-empDocument-api',EmployeeDocumentApiView.as_view(),name='apihrm-empDocument-api'),
    path('apihrm-documentType-api',DocumentTypeApiView.as_view() ,name='apihrm-documentType-api'),
    path('apihrm-LeaveInfo-api',EmpLeaveInfoApiView.as_view() ,name='apihrm-LeaveInfo-api'),
    path('apihrm-LeaveInfoApplication-api',EmpLeaveApplicationApiView.as_view(),name='apihrm-LeaveInfoApplication-api'),
    path('apihrm-trainingInfo-api',EmpTrainingInfoApiView.as_view(),name='apihrm-trainingInfo-api'),
    path('apihrm-payBill-api',PayBillApiView.as_view(),name='apihrm-payBill-api')
]