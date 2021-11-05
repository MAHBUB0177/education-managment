from django.urls  import path

from .views import *

urlpatterns = [
    path('apiedu-section-api/', SectionApiView.as_view(), name='apiedu-section-api'),
    path('apiedu-subject-api/', SubjectApiView.as_view(), name='apiedu-subject-api'),
    path('apiedu-subject-list-api/', SubjectListApiView.as_view(), name='apiedu-subject-list-api'),
    path('apiedu-department-info-api/', departmentinfoApiView.as_view(), name='apiedu-department-ino-api'),
    path('apiedu-shift-info-api/', shiftinfoApiView.as_view(), name='apiedu-shift-info-api'),
    path('apiedu-degree-info-api/', DegreeinfoApiView.as_view(), name='apiedu-degree-info-api'),
    path('apiedu-occupation-info-api/', OccupationinfoApiView.as_view(), name='apiedu-occupation-info-api'),
    path('apiedu-institute-api/', InstituteApiView.as_view(), name='apiedu-institute-api'),
    path('apiedu-student-info-api/', studentApiView.as_view(), name='apiedu-student-info-api'),
    path('apiedu-student-addmission-api/', stu_add_ApiView.as_view(), name='apiedu-student-addmission-api'),

    path('apiedu-academic-class-group-api/', ClassgroupApiView.as_view(), name='apiedu-academic-class-group-api'),

    
    path('apiedu-academic-class-api/', Academic_ClassApiView.as_view(), name='apiedu-academic-class-api'),

    path('apiedu-academic-year-api/', Academic_yearApiView.as_view(), name='apiedu-academic-year-api'),


    path('apiedu-result-grade-api/', result_gradeiView.as_view(), name='apiedu-result-grade-api'),
    path('apiedu-examtype-api/', exam_typeiView.as_view(), name='apiedu-examtype-api'),

    path('apiedu-exam-setup-api/', Exam_SetupiView.as_view(), name='apiedu-exam-setup-api'),


    path('apiedu-mark-details-api/', Exam_Marks_DetailsApiView.as_view(), name='apiedu-mark-details-api'),

    path('apiedu-final-exam-mark-api/', Final_Exam_MarksApiView.as_view(), name='apiedu-final-exam-mark-api'),

]