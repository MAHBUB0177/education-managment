from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Case, CharField, Value, When, F
from rest_framework import generics
from rest_framework.generics import ListAPIView
# Create your views here.

from edu.models import *

from apiedu.serializers import *


class Academic_ClassApiView(generics.ListAPIView):
    serializer_class = Academic_ClassSerializer
    def get_queryset(self):
        class_id = self.request.query_params.get('class_id',None)
        class_name = self.request.query_params.get('class_name',None)

        queryset = Academic_Class.objects.filter().order_by('class_name')

        if class_id:
            queryset = queryset.filter(class_id=class_id)

        return queryset



class Academic_yearApiView(generics.ListAPIView):
    serializer_class = Academic_yearSerializer
    def get_queryset(self):
        academic_year = self.request.query_params.get('academic_year',None)
        # section_name = self.request.query_params.get('section_name',None)

        queryset = Academic_Year.objects.filter().order_by('academic_year')

        if academic_year:
            queryset = queryset.filter(academic_year=academic_year)

        return queryset


# class Academic_yearApiView(generics.ListAPIView):
#     serializer_class = Academic_yearSerializer
#     def get_queryset(self):
#         academic_year = self.request.query_params.get('academic_year',None)
#         # section_name = self.request.query_params.get('section_name',None)

#         queryset = Academic_Year.objects.filter().order_by('academic_year')

#         if academic_year:
#             queryset = queryset.filter(academic_year=academic_year)

#         return queryset
####section

class SectionApiView(generics.ListAPIView):
    serializer_class = SectionSerializer
    def get_queryset(self):
        section_id = self.request.query_params.get('section_id',None)
        section_name = self.request.query_params.get('section_name',None)

        queryset = Section_Info.objects.filter().order_by('section_name')

        if section_id:
            queryset = queryset.filter(section_id=section_id)

        return queryset


class ClassgroupApiView(generics.ListAPIView):
    serializer_class = ClassgroupSerializer
    def get_queryset(self):
        class_group_id = self.request.query_params.get('class_group_id',None)
        class_group_name = self.request.query_params.get('class_group_name',None)

        queryset = Academic_Class_Group.objects.filter().order_by('class_group_name')

        if class_group_id:
            queryset = queryset.filter(class_group_id=class_group_id)

        return queryset

#subject-type
class SubjectApiView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    def get_queryset(self):
        subject_type_id = self.request.query_params.get('subject_type_id',None)
        subject_type_name = self.request.query_params.get('subject_type_name',None)

        queryset = Subject_Type.objects.filter().order_by('subject_type_name')

        if subject_type_id:
            queryset = queryset.filter(subject_type_id=subject_type_id)

        return queryset


####subject-list
class SubjectListApiView(generics.ListAPIView):
    serializer_class = SubjectListSerializer
    def get_queryset(self):
        subject_id = self.request.query_params.get('subject_id',None)
        class_id = self.request.query_params.get('class_id',None)
        class_group_id = self.request.query_params.get('class_group_id',None)

        queryset = Subject_List.objects.filter().order_by('subject_name')

        if subject_id:
            queryset = queryset.filter(subject_id=subject_id)
        if class_id:
            queryset = queryset.filter(class_id=class_id)
        if class_group_id:
            queryset = queryset.filter(class_group_id=class_group_id)

        return queryset


#department-info


class departmentinfoApiView(generics.ListAPIView):
    serializer_class = DepartmentSerializer
    def get_queryset(self):
        department_id = self.request.query_params.get('department_id',None)

        queryset = Department_Info.objects.filter().order_by('department_name')

        if department_id:
            queryset = queryset.filter(department_id=department_id)

        return queryset

####shift-info
class shiftinfoApiView(generics.ListAPIView):
    serializer_class = shifttSerializer
    def get_queryset(self):
        shift_id = self.request.query_params.get('shift_id',None)

        queryset = Shift_Info.objects.filter().order_by('shift_name')

        if shift_id:
            queryset = queryset.filter(shift_id=shift_id)

        return queryset
##degree-info

class DegreeinfoApiView(generics.ListAPIView):
    serializer_class = DegreeSerializer
    def get_queryset(self):
        degree_id = self.request.query_params.get('degree_id',None)

        queryset = Degree_Info.objects.filter().order_by('degree_name')

        if degree_id:
            queryset = queryset.filter(degree_id=degree_id)

        return queryset

##

class OccupationinfoApiView(generics.ListAPIView):
    serializer_class = OccupationSerializer
    def get_queryset(self):
        occupation_id = self.request.query_params.get('occupation_id',None)

        queryset = Occupation_Info.objects.filter().order_by('occupation_name')

        if occupation_id:
            queryset = queryset.filter(occupation_id=occupation_id)

        return queryset

###institute

class InstituteApiView(generics.ListAPIView):
    serializer_class = InstituteSerializer
    def get_queryset(self):
        institute_id = self.request.query_params.get('institute_id',None)

        queryset = Education_Institute.objects.filter().order_by('institute_name')

        if institute_id:
            queryset = queryset.filter(institute_id=institute_id)

        return queryset


###student-info:

class studentApiView(generics.ListAPIView):
    serializer_class = Student_infoSerializer
    def get_queryset(self):
        student_roll = self.request.query_params.get('student_roll',None)

        queryset = Students_Info.objects.filter().order_by('student_name')

        if student_roll:
            queryset = queryset.filter(student_roll=student_roll)

        return queryset
###addmission

class stu_add_ApiView(generics.ListAPIView):
    serializer_class = Student_addnissionSerializer
    def get_queryset(self):
        id = self.request.query_params.get('id',None)

        queryset = Student_Admission.objects.filter().order_by('class_roll')

        if id:
            queryset = queryset.filter(id=id)

        return queryset


class result_gradeiView(generics.ListAPIView):
    serializer_class = Result_gradeSerializer
    def get_queryset(self):
        grade_id = self.request.query_params.get('grade_id',None)

        queryset = Result_Grade.objects.filter().order_by('grade_name')

        if grade_id:
            queryset = queryset.filter(grade_id=grade_id)

        return queryset


class exam_typeiView(generics.ListAPIView):
    serializer_class = Exam_typeSerializer
    def get_queryset(self):
        examtype_id = self.request.query_params.get('examtype_id',None)

        queryset = Exam_Type.objects.filter().order_by('examtype_name')

        if examtype_id:
            queryset = queryset.filter(examtype_id=examtype_id)

        return queryset



class Exam_SetupiView(generics.ListAPIView):
    serializer_class = Exam_SetupSerializer
    def get_queryset(self):
        exam_id = self.request.query_params.get('exam_id',None)

        queryset = Exam_Setup.objects.filter().order_by('exam_name')

        if exam_id:
            queryset = queryset.filter(exam_id=exam_id)

        return queryset




class Exam_Marks_DetailsApiView(generics.ListAPIView):
    serializer_class = Exam_Marks_DetailsSerializer
    def get_queryset(self):
        id = self.request.query_params.get('id',None)

        queryset = Exam_Marks_Details.objects.filter().order_by('id')

        if id:
            queryset = queryset.filter(id=id)

        return queryset


class Final_Exam_MarksApiView(generics.ListAPIView):
    serializer_class = Final_Exam_MarksSerializer
    def get_queryset(self):
        id = self.request.query_params.get('id',None)

        queryset = Exam_Marks_Final.objects.filter().order_by('id')

        if id:
            queryset = queryset.filter(id=id)

        return queryset