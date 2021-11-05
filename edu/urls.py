##### For Image Upload
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [

    # path('edu-academic-year-createlist', edu_academic_year_view.as_view(), name='edu-academic-year-createlist'),
    # path('edu-academic-year-insert', edu_acaademic_year_insert, name='edu-academic-year-insert'),
    # path('edu-academic-year-edit/<slug:id>',edu_academic_year_edit, name='edu-academic-year-edit'),
    
    path('edu-academic-year-createlist', edu_academic_year_view.as_view(), name='edu-academic-year-createlist'),
    path('edu-academic-year-insert', edu_acaademic_year_insert, name='edu-academic-year-insert'),
    path('edu-academic-year-edit/<slug:id>',edu_academic_year_edit, name='edu-academic-year-edit'),


    path('edu-section-createlist', edu_section_view.as_view(), name='edu-section-createlist'),
    path('edu-section-insert', edu_section_insert, name='edu-section-insert'),
    path('edu-section-edit/<slug:id>',edu_section_edit, name='edu-section-edit'),

    path('edu-subject-createlist', edu_Subject_Type_view.as_view(), name='edu-subject-createlist'),
    path('edu-subject-insert', edu_Subject_Type_insert, name='edu-subject-insert'),
    path('edu-subject-edit/<slug:id>',edu_Subject_Type_edit, name='edu-subject-edit'),


    


    
    path('edu-academic-class-createlist', edu_academic_class_view.as_view(), name='edu-academic-class-createlist'),
    path('edu-academic-class-insert', edu_academic_class_insert, name='edu-academic-class-insert'),
    path('edu-academic-class-edit/<slug:id>',edu_academic_class_edit, name='edu-academic-class-edit'),


    path('edu-academic-class-group-createlist', edu_academic_class_group_view.as_view(), name='edu-academic-class-group-createlist'),
    path('edu-academic-class-group-insert', edu_academic_class_group_insert, name='edu-academic-class-group-insert'),
    path('edu-academic-class-group-edit/<slug:id>',edu_academic_class_group_edit, name='edu-academic-class-group-edit'),

#####
    path('edu-subject-list-createlist', edu_Subject_List_view.as_view(), name='edu-subject-list-createlist'),
    path('edu-subject-list-insert', edu_Subject_List_insert, name='edu-subject-list-insert'),
    path('edu-subject-list-edit/<slug:id>',edu_Subject_List_edit, name='edu-subject-list-edit'),

 #department_info
   path('edu-department-info-createlist', edu_department_info_view.as_view(), name='edu-department-info-createlist'),
   path('edu-department-info-insert', edu_department_info_insert, name='edu-department-info-insert'),
   path('edu-department-info-edit/<slug:id>',edu_department_info_edit, name='edu-department-info-edit'),
   

   ##shift-info
   path('edu-shift-info-createlist', edu_shift_info_view.as_view(), name='edu-shift-info-createlist'),
   path('edu-shift-info-insert', edu_shift_info_insert, name='edu-shift-info-insert'),
   path('edu-shift-info-edit/<slug:id>',edu_shift_info_edit, name='edu-shift-info-edit'),

   #degree-info
   path('edu-degree-info-createlist', edu_degree_info_view.as_view(), name='edu-degree-info-createlist'),
   path('edu-degree-info-insert', edu_degree_info_insert, name='edu-degree-info-insert'),
   path('edu-degree-info-edit/<slug:id>',edu_degree_info_edit, name='edu-degree-info-edit'),

   ##occupation
   path('edu-occupation-info-createlist', edu_occupation_info_view.as_view(),name='edu-occupation-info-createlist'),
   path('edu-occupation-info-insert', edu_occupation_info_insert, name='edu-occupation-info-insert'),
   path('edu-occupation-info-edit/<slug:id>',edu_occupation_info_edit, name='edu-occupation-info-edit'),

   ###
   
   path('edu-institute-createlist', edu_educaation_inst_view.as_view(), name='edu-institute-createlist'),
   path('edu-institute-insert', edu_educaation_inst_insert, name='edu-institute-insert'),
   path('edu-institute-edit/<slug:id>',edu_educaation_inst_edit, name='edu-institute-edit'),
   

   ###student-info

   path('edu-student-info-createlist', edu_student_info_view.as_view(), name='edu-student-info-createlist'),
   path('edu-student-info-insert', edu_student_info_insert, name='edu-student-info-insert'),
   path('edu-student-info-edit/<slug:id>',edu_student_info_edit, name='edu-student-info-edit'),

   ###
   path('edu-student-addmission-createlist', edu_student_addmission_view.as_view(), name='edu-student-addmission-createlist'),
   path('edu-student-addmission-insert', edu_student_addmission_insert, name='edu-student-addmission-insert'),
   path('edu-student-addmission-edit/<slug:id>',edu_student_addmission_edit, name='edu-student-addmission-edit'),


   ###
   path('edu-result-grade-createlist', edu_result_grade_view.as_view(), name='edu-result-grade-createlist'),
   path('edu-result-grade-insert', edu_result_grade_insert, name='edu-result-grade-insert'),
   path('edu-result-grade-edit/<slug:id>',edu_result_grade_edit, name='edu-result-grade-edit'),
   ###

   path('edu-Exam-Type-createlist', edu_Exam_Type_view.as_view(), name='edu-Exam-Type-createlist'),
   path('edu-Exam-Type-insert', edu_Exam_Type_insert, name='edu-Exam-Type-insert'),
   path('edu-Exam-Type-edit/<slug:id>',edu_Exam_Type_edit, name='edu-Exam-Type-edit'),
   ###

   
   path('edu-Exam-setup-createlist', edu_Exam_Setup_view.as_view(), name='edu-Exam-setup-createlist'),
   path('edu-Exam-setup-insert', edu_Exam_Setup_insert, name='edu-Exam-setup-insert'),
   path('edu-Exam-setup-edit/<slug:id>',edu_Exam_Setup_edit, name='edu-Exam-setup-edit'),



   path('edu-Mark-details-createlist', edu_Marks_Details_view.as_view(), name='edu-Mark-details-createlist'),
   path('edu-Mark-details-insert', edu_Marks_Details_insert, name='edu-Mark-details-insert'),
   path('edu-Mark-details-edit/<slug:id>',edu_Marks_Details_edit, name='edu-Mark-details-edit'),

   path('edu-final-exam-mark-createlist', edu_Exam_Marks_Final_view.as_view(), name='edu-final-exam-mark-createlist'),
   path('edu-final-exam-mark-insert', edu_Exam_Marks_Final_insert, name='edu-final-exam-mark-insert'),
   path('edu-final-exam-mark-edit/<slug:id>',edu_Exam_Marks_Final_edit, name='edu-final-exam-mark-edit'),
   
    # student in with filter
   path('edu-student-info-filterlist', edu_student_info_filter.as_view(), name='edu-student-info-filterlist'),
   path('edu-student-info-filtered', edu_student_info_filter_list, name='edu-student-info-filtered'),
   path('edu-insert-student-mark', edu_insert_student_mark, name='edu-insert-student-mark'),
#    path('indivitual_total_mark',indivitual_total_mark,name="indivitual_total_mark"),
#    path('student_report',student_report.as_view(),name="student_report"),

   path('edu-final-mark-info-filterlist', edu_finalmark_filterview.as_view(), name='edu-final-mark-info-filterlist'),
   path('edu-final-mark-info-filtered', edu_finalmark_filtertable, name='edu-final-mark-info-filtered'),
   path('edu-insert-final-mark', edu_finalmark_show, name='edu-insert-final-mark'),




   path('edu-student-exam-filterlist', edu_student_exam_filter.as_view(), name='edu-student-exam-filterlist'),
   path('edu-student-exam-filtered', edu_student_exam_filter_list, name='edu-student-exam-filtered'),
   
   
]
