from django import forms
from crispy_forms.layout import Field
from django.forms import ModelForm, TextInput, Select, Textarea, IntegerField, ChoiceField, BooleanField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class ChoiceFieldNoValidation(ChoiceField):
    def validate(self, value):
        pass



class Academic_YearForm(forms.ModelForm):
    
    class Meta:
        model = Academic_Year
        fields =['academic_year'  ]
        widgets = {
            'academic_year': DateInput(),
            
        }
    

        labels = {  
                   
                    "academic_year": _("Academic Year"),
                    
                    
                }



class Academic_ClassFrom(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(Academic_ClassFrom, self).__init__(*args, **kwargs)
    #     # self.fields['class_id'].widget.attrs['readonly'] =True
    #     self.fields['class_name'].widget.attrs['readonly'] = False
    #     self.fields['short_name'].required = True
    #     self.fields['subject_list'].required = True

    #     instance = getattr(self, 'instance', None)

    #     if instance and instance.pk:
            
    #         # self.fields['class_id'].widget.attrs['readonly'] = True
    #         self.fields['class_name'].widget.attrs['readonly'] = False
    #         self.fields['short_name'].required = True
    #         self.fields['subject_list'].required = True

    class Meta:
        model = Academic_Class
        fields =['class_name','short_name', 'subject_list',]

        labels = {  
                    "class_name": _("Class Name"),
                    "short_name": _("short name"),
                    "subject_list": _("Subject list"),
                    
                }


class Academic_Class_GroupFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Academic_Class_GroupFrom, self).__init__(*args, **kwargs)
        self.fields['class_id'].widget.attrs['readonly'] = True
        # self.fields['class_group_id'].widget.attrs['readonly'] = True
        self.fields['class_group_name'].required = True
        self.fields['subject_list'].required = True

        instance = getattr(self, 'instance', None)

        if instance and instance.pk:
            
            self.fields['class_id'].widget.attrs['readonly'] = True
            # self.fields['class_group_id'].widget.attrs['readonly'] = True
            self.fields['class_group_name'].required = True
            self.fields['subject_list'].required = True

    class Meta:
        model = Academic_Class_Group
        fields =['class_id','class_group_name', 'subject_list','fees_list',]

        labels = {  
                    "class_group_name": _("Class Group Name"),
                    "class_id": _("Class Id"),

                    
                    "subject_list": _("Subject list"),
                    
                }




class Section_InfoForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(Section_InfoForm, self).__init__(*args, **kwargs)
    #     self.fields['class_id'].widget.attrs['readonly'] = True
    #     self.fields['section_id'].widget.attrs['readonly'] = True
    #     self.fields['section_name'].required = True
    #     self.fields['total_student'].required = True
       

    #     instance = getattr(self, 'instance', None)

    #     if instance and instance.pk:
            
    #         self.fields['class_id'].widget.attrs['readonly'] = True
    #         self.fields['section_id'].widget.attrs['readonly'] = True
    #         self.fields['section_name'].required = True
    #         self.fields['total_student'].required = True
  

    class Meta:
        model = Section_Info
        fields =['section_teacher_id','class_start_time', 'section_name','total_student','class_id','class_group_id', ]

        labels = {  
                    "section_teacher_id": _("Teacher id"),
                    "class_start_time": _("class time"),
                    "section_id": _("Section id"),
                    "section_name": _("Section name"),
                }




####
class Subject_TypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Subject_TypeForm, self).__init__(*args, **kwargs)
        # self.fields['subject_type_id'].widget.attrs['readonly'] = False
        self.fields['subject_type_name'].widget.attrs['readonly'] = False
        
        

        instance = getattr(self, 'instance', None)

        if instance and instance.pk:
            
            # self.fields['subject_type_id'].widget.attrs['readonly'] = False
            self.fields['subject_type_name'].widget.attrs['readonly'] = False
            

    class Meta:
        model = Subject_Type
        fields =['subject_type_name', ]

        labels = {  
                    
                    "subject_type_name": _("Subject  Type Name"),
                    
                    
                }    

####

class Subject_ListForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(Subject_ListForm, self).__init__(*args, **kwargs)
        
    #     self.fields['subject_type_id'].widget.attrs['readonly'] = False
    #     self.fields['subject_name'].widget.attrs['redonly']=False
    #     self.fields['class_duration'].widget.attrs['redonly']=True
        

    #     instance = getattr(self, 'instance', None)

    #     if instance and instance.pk:
            
            
    #         self.fields['subject_type_id'].widget.attrs['readonly'] = False
    #         self.fields['subject_name'].widget.attrs['redonly']=False
    #         self.fields['class_duration'].widget.attrs['redonly']=True
            

    class Meta:
        model = Subject_List
        fields =['subject_type_id','subject_name','class_duration','class_order_no','no_of_class','maximum_marks','minimum_marks','class_id','class_group_id', ]

        labels = {  
                    
                    "subject_type_id": _("Subject Type Name"),
                    "subject_name": _("Subject Name"),
                    "class_duration": _("Class Duration"),
                    "class_order_no": _("Class order NO"),
                    "no_of_class": _("No of Class"),
                    
                }  

####
class Department_InfoForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(Department_InfoForm, self).__init__(*args, **kwargs)
        
    #     self.fields['department_name'].widget.attrs['readonly'] = False
        
        

    #     instance = getattr(self, 'instance', None)

    #     if instance and instance.pk:
            
         
    #         self.fields['department_name'].widget.attrs['readonly'] = False
            

    class Meta:
        model = Department_Info
        fields =['department_name','total_student','total_quota' ]

        labels = {  
                    
                    "department_name": _("Department Name"),
                    
                    
                }


#shift info
class Shift_InfoForm(forms.ModelForm):
    class Meta:
        model = Shift_Info
        fields =['shift_name','shift_start_time','shift_end_time','total_student', ]

        labels = {  
                    
                    "shift_name": _("Shift Name"),
                    "shift_start_time": _("Shift  strat time"),
                    "shift_end_time": _("Shift  end time"),
                    "total_student": _("Total student"),
                   
                    
                }  

#degree info
class Degree_InfoForm(forms.ModelForm):
    class Meta:
        model = Degree_Info
        fields =['degree_name','degree_duration','app_user_id', ]

        labels = {  
                    
                    "degree_name": _("Degree Name"),
                    "degree_duration": _("Degree duration"),
                     "app_user_id": _("App user id"),
                    
                   
                    
                }  

class Occupation_InfoForm(forms.ModelForm):
    class Meta:
        model = Occupation_Info
        fields =['occupation_name','app_user_id', ]

        labels = {  
                    
                    "occupation_name": _("Occupation Name"),
                    
                     "app_user_id": _("App user id"),
                    
                   
                    
                }  

### education institue

class Education_InstituteForm(forms.ModelForm):
    class Meta:
        model = Education_Institute
        fields =['institute_name', ]

        labels = {  
                    
                    "institute_name": _("Institute Name"),
                    
                     
                    
                   
                    
                }  
#####student_info:
class Student_infoForm(forms.ModelForm):
    class Meta:
        model=Students_Info
        fields=['academic_year','branch_code','student_reg','student_name','class_id','class_group_id','shift_id','last_institute_id','student_type','student_father_name','father_occupation_id','father_phone_number','student_mother_name','mother_occupation_id','mother_phone_number','student_gender','student_present_address','student_permanent_address','student_phone','student_date_of_birth']
        widgets = {
            'student_date_of_birth': DateInput(),
            
        }
        labels = {  

                    "student_name": _(" Student Name"),
                    "student_reg": _(" Student Registration"),
                    "student_father_name": _(" Student  Father Name"),
                    "student_mother_name": _(" Student Mother Name"),
                    "student_present_address": _(" Student Present Address"),
                    "student_permanent_address": _(" Student Permanent Address"),
                    
                    
                    

                    
                     
                    
                   
                    
                } 


###Student_Admission:

class Student_AdmissionForm(forms.ModelForm):
    class Meta:
        model = Student_Admission
        fields =['add_id','student_roll','class_roll', ]

        labels = {  
                    "add_id": _("ADDMISSION ID"),
                    "student_roll": _("Student roll"),
                    "class_roll": _("Class Roll"),
        }

####result_grade:
class Result_GradeForm(forms.ModelForm):
    class Meta:
        model = Result_Grade
        fields =['grade_name','result_gpa','lowest_mark','highest_mark', ]

        labels = {  
                    
                    "grade_name": _("Grade Name"),
                    "result_gpa": _("Result GPA"),
                    "lowest_mark": _("Lowest Mark"),
                    "highest_mark": _("Hieghest Mark"),
                   
                    
                }  


class Exam_TypeForm(forms.ModelForm):
    class Meta:
        model = Exam_Type
        fields =('examtype_name', )

        labels = {  
                    
                    "examtype_name": _("ExamType Name"),
                    
                   
                    
                }  



class Exam_SetupForm(forms.ModelForm):
    class Meta:
        model = Exam_Setup
        fields =['exam_name','examtype_id','total_exam_marks','minimum_pass_marks', ]

        labels = {  
                    
                    "exam_name": _("Exam Name"),
                    "examtype_id": _("Examtype Id"),
                    "total_exam_marks": _("total exam Mark"),
                    "minimum_pass_marks": _("minimum pass Mark"),
                   
                    
                }
class Exam_Marks_DetailsForm(forms.ModelForm):
    class Meta:
        model = Exam_Marks_Details
        fields =['exam_id','subject_id','student_roll','total_exam_marks','obtain_marks','result_grade','grade_point_average',]

        labels = {  
                    
                    "exam_id": _("Exam Name"),
                    "subject_id": _("Subject Id"),
                    "student_roll": _("Student Roll"),
                    "total_exam_marks": _("Total exam mark"),

                    "obtain_marks": _("Obtain Mark"),
                    "result_grade": _("Result grade"),
                    "grade_point_average": _("Grade Point Average"),
                    
                   
                    
                } 


class Exam_Marks_FinalForm(forms.ModelForm):
    class Meta:
        model = Exam_Marks_Final
        fields =['student_roll','total_exam_marks','obtain_marks','result_grade','grade_point_average',]

        labels = {  
                    
                    
                    "student_roll": _("Student Roll"),
                    "total_exam_marks": _("Total exam mark"),
                    "obtain_marks": _("Obtain marks"),

                    
                    "result_grade": _("Result grade"),
                    "grade_point_average": _("Grade Point Average"),
                    
                   
                    
                } 

class Student_rollInput(forms.Form):
    student_roll=forms.CharField(max_length=30)
    class meta:
        fields=["student_roll"]
        labels={"student_roll":_("student_roll")}

