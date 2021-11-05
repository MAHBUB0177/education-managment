from rest_framework import serializers
import datetime

from edu.models import *


class Academic_yearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Year
        fields = ('__all__')
#section
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section_Info
        fields = ('__all__')




class Academic_ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Class
        fields = ('__all__')


class ClassgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Class_Group
        fields = ('__all__')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject_Type
        fields = ('__all__')

####
class SubjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject_List
        fields = ('__all__')


#department_info
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department_Info
        fields = ('__all__')

##shift-info
class shifttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift_Info
        fields = ('__all__')


##degree-info
class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree_Info
        fields = ('__all__')

##occupation-info

class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation_Info
        fields = ('__all__')
###institute

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education_Institute
        fields = ('__all__')

## student-info

class Student_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students_Info
        fields = ('__all__')


###addmission
class Student_addnissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Admission
        fields = ('__all__')




class Result_gradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result_Grade
        fields = ('__all__')


class Exam_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam_Type
        fields = ('__all__')


class Exam_SetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam_Setup
        fields = ('__all__')




class Exam_Marks_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam_Marks_Details
        fields = ('__all__')



class Final_Exam_MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam_Marks_Final
        fields = ('__all__')