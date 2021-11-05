from django.db import models
from appauth.models import Loc_Country, Loc_Division, Loc_District, Loc_Upazila, Branch

# Create your models here.

from appauth.models import STATUS_LIST, BLOOD_GROUP, GENDER_LIST, RELIGION_LIST, MARITAL_STATUS, TRANSACTION_SCREEN, CASH_RECEIVE_PAYMENT, TRAN_DEBIT_CREDIT, FIXED_PERCENT, DAY_MONTH_YEAR, DOCUMENT_TYPES, EDU_LIST, WEEK_DAY_LIST 

class Academic_Year(models.Model):
   
    academic_year = models.CharField(max_length=30,  blank=True)
    app_user_id = models.CharField(max_length=20, null=False, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.academic_year


class Academic_Class(models.Model):
    class_id = models.CharField(max_length=20, blank=True, primary_key=True)
    class_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=False)
    roll_serial = models.CharField(max_length=20, blank=True, null=False)
    subject_list = models.CharField(max_length=500, blank=True, null=True)
    fees_list = models.CharField(max_length=500, blank=True, null=True)
    app_user_id = models.CharField(max_length=20, null=False, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.class_name

class Academic_Class_Group(models.Model):
    class_id = models.ForeignKey(Academic_Class, on_delete=models.CASCADE, null=True, blank=True, db_column='class_id', related_name='cgp_class_id') 
    class_group_id = models.CharField(max_length=20, blank=True, primary_key=True)
    class_group_name = models.CharField(max_length=100)
    subject_list = models.CharField(max_length=500, blank=True, null=True)
    fees_list = models.CharField(max_length=500, blank=True, null=True)
    app_user_id = models.CharField(max_length=20, null=False, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.class_group_name

class Section_Info(models.Model):
    class_id = models.ForeignKey(Academic_Class, on_delete=models.CASCADE, null=True, blank=True, db_column='class_id', related_name='sec_class_id')
    section_id = models.CharField(max_length=20, primary_key=True, blank=True)
    class_group_id=models.ForeignKey(Academic_Class_Group,on_delete=models.CASCADE,null=True,db_column='class_group_id',related_name='sec_class_group_id')
    section_name = models.CharField(max_length=200)
    total_student = models.IntegerField(null=True, blank=True)
    section_teacher_id = models.CharField(max_length=20, blank=True, null=True)
    class_start_time = models.CharField(max_length=20, blank=True, null=True)
    class_end_time = models.CharField(max_length=20, blank=True, null=True)
    app_user_id = models.CharField(max_length=20, null=False, blank=True)
   
    def __str__(self):
        return self.section_name

class Subject_Type(models.Model):
    subject_type_id = models.CharField(max_length=30, primary_key=True, blank=True)
    subject_type_name = models.CharField(max_length=100)
    app_user_id = models.CharField(max_length=20, null=False, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject_type_name

class Subject_List(models.Model):
    class_id = models.ForeignKey(Academic_Class, on_delete=models.CASCADE, null=True, blank=True, db_column='class_id', related_name='cgp_class_id1') 
    class_group_id = models.ForeignKey(Academic_Class_Group, on_delete=models.CASCADE, null=True, blank=True, db_column='class_group_id', related_name='cgp_class_id3')
    subject_id = models.CharField(max_length=20, primary_key=True, blank=True)
    subject_type_id = models.ForeignKey(Subject_Type, on_delete=models.CASCADE, null=True, blank=True, db_column='subject_type_id', related_name='slt_subject_type_id') 
    subject_name = models.CharField(max_length=150)
    class_duration = models.CharField(max_length=100, blank=True, null=True)
    class_order_no = models.IntegerField(null=True, blank=True)
    no_of_class = models.IntegerField(null=True, blank=True)
    maximum_marks = models.IntegerField(null=True, blank=True)
    minimum_marks = models.IntegerField(null=True, blank=True)
    app_user_id = models.CharField(max_length=20, null=False, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject_name

class Department_Info(models.Model):
    department_id = models.CharField(max_length=20, primary_key=True, blank=True)
    department_name = models.CharField(max_length=200, null=False)
    total_student = models.IntegerField(null=True)
    total_quota = models.IntegerField(null=True)
    app_user_id = models.CharField(max_length=20, null=True, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.department_name

class Shift_Info(models.Model):
    shift_id = models.CharField(max_length=20, blank=True, primary_key=True)
    shift_name = models.CharField(max_length=200, null=False)
    shift_start_time = models.CharField(max_length=100)
    shift_end_time = models.CharField(max_length=100)
    total_student = models.IntegerField(null=True)
    total_quota = models.IntegerField(null=True)
    app_user_id = models.CharField(max_length=20, null=True, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.shift_name+" ("+self.shift_start_time+" - "+self.shift_end_time+" )"

class Degree_Info(models.Model):
    degree_id = models.CharField(max_length=20,primary_key=True, blank=True)
    degree_name = models.CharField(max_length=200, null=False)
    degree_duration = models.CharField(max_length=200, null=False)
    app_user_id = models.CharField(max_length=20, null=True, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.degree_name

class Occupation_Info(models.Model):
    occupation_id = models.CharField(max_length=20,primary_key=True, blank=True)
    occupation_name = models.CharField(max_length=200, null=False)
    app_user_id = models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return self.occupation_name

class Education_Institute(models.Model):
    institute_id = models.CharField(max_length=20, primary_key=True, blank=True)
    institute_name = models.CharField(max_length=200, null=False)
    degree_duration = models.CharField(max_length=200, null=False)
    app_user_id = models.CharField(max_length=20, null=True, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.institute_name



class Students_Info(models.Model):
    academic_year=models.ForeignKey(Academic_Year,on_delete=models.CASCADE, null=True, blank=True)
    branch_code = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True, db_column='branch_code', related_name='stu_branch_code') 
    
    student_roll = models.CharField(max_length=30, primary_key=True)
    student_reg = models.CharField(max_length=30,null=True, blank=True)
    student_name = models.CharField(max_length=200)
    student_nick_name = models.CharField(max_length=200)
    class_id = models.ForeignKey(Academic_Class, on_delete=models.CASCADE, null=True, blank=True, db_column='class_id', related_name='stu_class_id')
    class_group_id = models.ForeignKey(Academic_Class_Group, on_delete=models.CASCADE, null=True, blank=True, db_column='class_group_id', related_name='stu_class_group_id')
    shift_id = models.ForeignKey(Shift_Info, on_delete=models.CASCADE, null=True, blank=True, db_column='shift_id', related_name='stu_shift_id')
    last_institute_id = models.ForeignKey(Education_Institute, on_delete=models.CASCADE, null=True, blank=True, db_column='last_institute_id', related_name='stu_last_institute_id')
    student_type = models.CharField(max_length=30,null=True, blank=True)
    student_referred_by = models.CharField(max_length=15,null=True, blank=True)
    student_father_name = models.CharField(max_length=200, blank=True)
    father_occupation_id = models.ForeignKey(Occupation_Info, on_delete=models.CASCADE, null=True, blank=True, db_column='father_occupation_id', related_name='stu_father_occupation_id')
    father_email_address = models.CharField(max_length=200, blank=True)
    father_phone_number = models.CharField(max_length=20, blank=True)
    sms_to_father = models.BooleanField(blank=True,default=False)
    student_mother_name = models.CharField(max_length=200, blank=True)
    mother_occupation_id = models.ForeignKey(Occupation_Info, on_delete=models.CASCADE, null=True, blank=True, db_column='mother_occupation_id', related_name='stu_mother_occupation_id')
    mother_email_address = models.CharField(max_length=200, blank=True)
    mother_phone_number = models.CharField(max_length=20, blank=True)
    sms_to_mother = models.BooleanField(blank=True,default=False)
    student_blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP, default='', blank=True)
    student_gender = models.CharField(max_length=5, choices=GENDER_LIST, default='', blank=True)
    student_religion = models.CharField(max_length=5, choices=RELIGION_LIST, default='', blank=True)
    student_marital_status = models.CharField(max_length=5,null=True, choices=MARITAL_STATUS, default ='S', blank=True)
    student_education= models.CharField(max_length=20, null=True, blank=True)
    student_national_id = models.CharField(max_length=200,null=True, blank=True)
    student_birth_cert = models.CharField(max_length=200,null=True, blank=True)
    student_present_address = models.TextField(null=True, blank=False)
    student_permanent_address = models.TextField(null=True, blank=True)
    student_phone = models.CharField(max_length=15,null=True)
    student_email = models.CharField(max_length=30,null=True, blank=True)
    student_joining_date = models.DateField(null=True, blank=True)
    student_date_of_birth = models.DateField(null=True, blank=True)
    student_status = models.CharField(max_length=5,null=True, choices=STATUS_LIST, default='A', blank=True)
    student_comments = models.CharField(max_length=200,null=True, blank=True)
    emerg_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emerg_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    emerg_contact_relation = models.CharField(max_length=50, blank=True, null=True)
    emerg_contact_nid = models.CharField(max_length=50, blank=True, null=True)
    app_user_id = models.CharField(max_length=20, null=False, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name

class Student_Admission(models.Model):
    add_id=models.CharField(max_length=30,blank=True)
    # student_roll = models.CharField(max_length=30,null=True, blank=True)
    student_roll = models.ForeignKey(Students_Info, on_delete=models.CASCADE, null=True, blank=True, db_column='student_roll', related_name='sta_student_roll')
    class_roll = models.CharField(max_length=30,null=True, blank=True)
    app_user_id = models.CharField(max_length=20, null=False, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    


class Result_Grade(models.Model):
    grade_id = models.CharField(max_length=30, primary_key=True)
    grade_name = models.CharField(max_length=20)
    result_gpa = models.DecimalField(max_digits=22, decimal_places=2, null=True, blank=True )
    lowest_mark = models.DecimalField(max_digits=22, decimal_places=2, null=True, blank=True )
    highest_mark = models.DecimalField(max_digits=22, decimal_places=2, null=True, blank=True )
    is_failed = models.BooleanField(blank=True,default=False)
    app_user_id = models.CharField(max_length=20, null=False, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.grade_name

 
class Exam_Type(models.Model):
    examtype_id = models.CharField(max_length=30, primary_key=True)
    examtype_name = models.CharField(max_length=20)
    app_user_id = models.CharField(max_length=20, null=False, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.examtype_name





class Exam_Setup(models.Model):
    exam_id=models.CharField(max_length=30,primary_key=True)
    exam_name = models.CharField(max_length=200)
    examtype_id = models.ForeignKey(Exam_Type, on_delete=models.CASCADE, null=True, blank=True, db_column='examtype_id', related_name='exs_examtype_id2')
    total_exam_marks = models.DecimalField(max_digits=22, decimal_places=2, null=True, blank=True )
    minimum_pass_marks = models.DecimalField(max_digits=22, decimal_places=2, null=True, blank=True )
    app_user_id = models.CharField(max_length=20, null=False, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.exam_name



class Exam_Marks_Details(models.Model):
    exam_id = models.ForeignKey(Exam_Setup, on_delete=models.CASCADE, null=True, blank=True, db_column='exam_id', related_name='emd_exam_id3')
    subject_id = models.ForeignKey(Subject_List, on_delete=models.CASCADE, null=True, blank=True, db_column='subject_id', related_name='emd_subject_id3')
    student_roll = models.ForeignKey(Students_Info, on_delete=models.CASCADE, null=True, blank=True, db_column='student_roll', related_name='emd_student_roll3')
    total_exam_marks = models.DecimalField(max_digits=22, decimal_places=2, null=True, blank=True )
    obtain_marks = models.DecimalField(max_digits=22, decimal_places=2, null=True, blank=True )
    result_grade = models.CharField(max_length=20)
    grade_point_average = models.DecimalField(max_digits=22, decimal_places=2, null=True, blank=True)
    app_user_id = models.CharField(max_length=20, null=False, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)




class Exam_Marks_Final(models.Model):
    student_roll = models.ForeignKey(Students_Info, on_delete=models.CASCADE, null=True, blank=True, db_column='student_roll', related_name='emd_student_roll2')
    total_exam_marks = models.DecimalField(max_digits=22, decimal_places=2, null=True, blank=True )
    obtain_marks = models.DecimalField(max_digits=22, decimal_places=2, null=True, blank=True )
    result_grade = models.CharField(max_length=20)
    grade_point_average = models.DecimalField(max_digits=22, decimal_places=2, null=True, blank=True)
    app_user_id = models.CharField(max_length=20, null=False, blank=True)
    app_data_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.grade_point_average
        