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

class AppUserModelForm(forms.ModelForm):
    employee_name  = forms.CharField(label='Employee Name', initial="",)
    def __init__(self, *args, **kwargs):
        super(AppUserModelForm, self).__init__(*args, **kwargs)
        self.fields['employee_name'].widget.attrs['readonly'] = True
        self.fields['employee_name'].required = True
        self.fields['user_phone_number'].required = True
        self.fields['app_user_name'].required = True

        instance = getattr(self, 'instance', None)

        if instance and instance.pk:
            self.fields['employee_name'].widget.attrs['readonly'] = True
            self.fields['employee_name'].required = False
            self.fields['user_phone_number'].widget.attrs['readonly'] = True
            self.fields['app_user_id'].widget.attrs['readonly'] = True
            self.fields['app_user_name'].widget.attrs['readonly'] = True
 
    class Meta:
        model = User_Settings
        fields =['user_phone_number','app_user_id','app_user_name', 'status','employee_name', ]

        labels = {  
                    "user_phone_number": _("User Phone"),
                    "app_user_id": _("User ID"),
                    "app_user_name": _("User Name"),
                    "status": _("Status"),
                }

class AppUserSearch(forms.Form):
    app_user_name = forms.CharField(label="User Name", widget=forms.TextInput(
    attrs={'placeholder': 'User Name',  'id': 'id_app_user_name'}
    ),required=False)
    user_phone_number = forms.CharField(label="Phone Number", widget=forms.TextInput(
    attrs={'placeholder': '',  'id': 'id_user_phone_number'}
    ),required=False)
######
# class user_setting_Form(fomrs.modelForm):
#       def __init__(self, *args, **kwargs):
#           super(user_setting_Form,self).__init__(*args,*kwargs)
#           instance=getattr(self,'instance',None)

#           self.field['user_phone_number'].widget.attrs['Rendonly']=True
#           self.field['app_user_name'].required=True
#           self.field['employee_name'].required=True
#           self.field['account_number'].required=True
#           self.field['status'].required=False

#           if instance and instance.pk:
#               self.field['user_phone_number'].widget.attrs['Rendonly']=True
#               self.field['app_user_name'].required=True
#               self.field['employee_name'].required=True
#               self.field['account_number'].required=True
#               self.field['status'].required=False


#         class Meta:
#             model:User_Settings
#             fields=['user_phone_number','app_user_id','app_user_name','employee_name','status','account_number','reset_user_password']
#             labels={

#                 "user_phone_number":("User Phone No"),
#                 "employee_name":("Employee Name"),
#                 "account_number":("Account No")

#               }


    


#####
class BranchModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BranchModelForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)

        if instance and instance.pk:
            self.fields['branch_code'].widget.attrs['readonly'] = True

    class Meta:
        model = Branch
        fields = ['branch_code','branch_name','branch_address','manager_phone','status',
        'country_id','division_id','district_id','upozila_id','union_id','manager_id','opening_date',]
        widgets = {
            'opening_date': DateInput(),
            
        }
        labels = {
                    "branch_code": _("Branch Code"),
                    "branch_name": _("Branch Name"),
                    "opening_date": _("Opening Date"),
                    "country_id": _("Country"),
                    "division_id": _("Division"),
                    "district_id": _("District"),
                    "upozila_id": _("Upozila"),
                    "union_id": _("Union/City Corp"),
                    "manager_id": _("Branch Manager"),
                    "branch_address": _("Address"),
                    "manager_phone": _("Manager Phone"),
                    "status": _("Status"), 
                }


class Country_Model_Form(forms.ModelForm):

    class Meta:
        model = Loc_Country
        fields = ['country_name']
        labels = {
                    "country_name": _("Country Name"), 
                }


class Division_Model_Form(forms.ModelForm):
    
    class Meta:
        model = Loc_Division
        fields = ['division_name','country_id']
        labels = {
                    "division_name": _("Division Name"), 
                }

class District_Model_Form(forms.ModelForm):
    
    class Meta:
        model = Loc_District
        fields = ['district_name','division_id']
        labels = {
                    "district_name": _("District Name"), 
                    
                }

class Upazila_Model_Form(forms.ModelForm):
    
    class Meta:
        model = Loc_Upazila
        fields = ['upozila_name','district_id']
        labels = {
                    "upozila_name": _("Upozila Name"), 
                }





class Union_Model_Form(forms.ModelForm):
    
    class Meta:
        model = Loc_Union
        fields = ['union_name','upozila_id']
        labels = {
                    "union_name": _("Union Name"), 
                }



