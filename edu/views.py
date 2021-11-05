import datetime
import json
import logging
import sys
from datetime import date, datetime, timedelta
from random import randint

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.exceptions import FieldDoesNotExist
from django.db import connection, transaction
from django.db.models import Avg, Count, Sum
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)
from decimal import Decimal

all_permissions = {}

from .forms import *
from .models import *
from .myException import *
from .utils import *
from .validations import *

# Create your views here.


def get_global_data(request):

    global all_permissions

    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')

    user_full_name = request.session['user_full_name']
    application_title = request.session['application_title']
    user_id = request.session["app_user_id"]
    user_info = User.objects.get(username=request.user)
    all_permissions = user_info.get_all_permissions()
    user_designation = "......"
    context = {
        'user': request.user,
        'user_full_name': user_full_name,
        'application_title': application_title,
        'app_user_id': user_id,
        'all_permissions': all_permissions,
        'user_designation' : user_designation
    }

    for programs in all_permissions:
        # print(program.split('.')[1])
        context[programs.split('.')[1]] = True

    return context





class edu_academic_year_view(TemplateView):
    template_name = 'appeducation/appeducation-academic-year-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Academic_YearForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)

@transaction.atomic
def edu_acaademic_year_insert(request):
    if not request.user.is_authenticated:
        return render(request,'appauth/appauth-login.html')
    data=dict()
    data['form_is_valid']=False
    app_user_id=request.session['app_user_id']
    if request.method=='POST':
        form=Academic_YearForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    post=form.save(commit=False)
                    post.app_user_id=app_user_id
                    post.save()
                    data['form_is_valid']=True
                    data['success_message']="Traning info create successfully"
                    data['error_message']=''
                    return JsonResponse(data)

            except Exception as e:
                print(str(e))
                data['form_is_valid']=False
                data['error_message']=str(e)
                return JsonResponse(data)

        else:
            data['error_message']=form.errors.as_json()
    return JsonResponse(data)

def edu_academic_year_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    # instance_data = get_object_or_404(Academic_Year, academic_year=id)
    instance_data = get_object_or_404(Academic_Year,id=id)
    template_name = 'appeducation/appeducation-academic-year-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Academic_YearForm(request.POST, instance=instance_data)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Academic_YearForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
    return JsonResponse(data)

###academic class


class  edu_academic_class_view(TemplateView):
    template_name = 'appeducation/appeducation-academic-class-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Academic_ClassFrom()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_academic_class_insert(request):
    if not request.user.is_authenticated:
        return render(request,'appauth/appauth-login.html')
    data=dict()
    data['form_is_valid']=False
    app_user_id=request.session['app_user_id']
    if request.method=='POST':
        form=Academic_ClassFrom(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    post=form.save(commit=False)
                    post.app_user_id=app_user_id
                    class_id=fn_get_class_id()
                    post.class_id=class_id
                    post.save()
                    data['form_is_valid']=True
                    data['success_message']="Traning info create successfully"
                    data['error_message']=''
                    return JsonResponse(data)

            except Exception as e:
                print(str(e))
                data['form_is_valid']=False
                data['error_message']=str(e)
                return JsonResponse(data)

        else:
            data['error_message']=form.errors.as_json()
    return JsonResponse(data)

def edu_academic_class_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Academic_Class, class_id=id)
    template_name = 'appeducation/appeducation-academic-class-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Academic_ClassFrom(request.POST, instance=instance_data)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Academic_ClassFrom(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
    return JsonResponse(data)

###academic class

class  edu_academic_class_group_view(TemplateView):
    template_name = 'appeducation/appeducation-academic-class-group-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Academic_Class_GroupFrom()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_academic_class_group_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Academic_Class_GroupFrom(request.POST)
        if form.is_valid():
            class_group_id = fn_get_class_group_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.class_group_id = class_group_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'Section Added Successfully!'
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def edu_academic_class_group_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Academic_Class_Group, class_group_id=id)
    template_name = 'appeducation/appeducation-academic-class-group-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Academic_Class_GroupFrom(request.POST, instance=instance_data)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Academic_Class_GroupFrom(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
    return JsonResponse(data)


###section info

class edu_section_view(TemplateView):
    template_name = 'appeducation/appeducation-section-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Section_InfoForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_section_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Section_InfoForm(request.POST)
        if form.is_valid():
            section_id = fn_get_section_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.section_id = section_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'Section Added Successfully!'
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def edu_section_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Section_Info, section_id=id)
    template_name = 'appeducation/appeducation-section-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Section_InfoForm(request.POST, instance=instance_data)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Section_InfoForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
    return JsonResponse(data)


#####subject type


class edu_Subject_Type_view(TemplateView):
    template_name = 'appeducation/appeducation-subject-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Subject_TypeForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_Subject_Type_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Subject_TypeForm(request.POST)
        if form.is_valid():
            subject_type_id = fn_get_subject_type_group_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.subject_type_id = subject_type_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'Section Added Successfully!'
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def edu_Subject_Type_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Subject_Type, subject_type_id=id)
    template_name = 'appeducation/appeducation-subject-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Subject_TypeForm(request.POST, instance=instance_data)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Subject_TypeForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
    return JsonResponse(data)

####### subjict list

class edu_Subject_List_view(TemplateView):
    template_name = 'appeducation/appeducation-subject-list-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Subject_ListForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_Subject_List_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Subject_ListForm(request.POST)
        if form.is_valid():
            subject_id = fn_get_subject_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.subject_id = subject_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'Section Added Successfully!'
            return JsonResponse(data)
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def edu_Subject_List_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Subject_List, subject_id=id)
    template_name = 'appeducation/appeducation-subject-list-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Subject_ListForm(request.POST, instance=instance_data)
        # print(form)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Subject_ListForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
        # print(form)
    return JsonResponse(data)
 

##### department info


class edu_department_info_view(TemplateView):
    template_name = 'appeducation/appeducation-department-info-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Department_InfoForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_department_info_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Department_InfoForm(request.POST)
        if form.is_valid():
            department_id = fn_get_department_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.department_id = department_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'DEPARTMENT Added Successfully!'
            return JsonResponse(data)
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def edu_department_info_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Department_Info, department_id=id)
    template_name = 'appeducation/appeducation-department-info-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Department_InfoForm(request.POST, instance=instance_data)
        # print(form)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Department_InfoForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
        # print(form)
    return JsonResponse(data)

#### shift info

class edu_shift_info_view(TemplateView):
    template_name = 'appeducation/appeducation-shift-info-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Shift_InfoForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_shift_info_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Shift_InfoForm(request.POST)
        if form.is_valid():
            shift_id = fn_get_shift_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.shift_id = shift_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'Section Added Successfully!'
            return JsonResponse(data)
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def edu_shift_info_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Shift_Info, shift_id=id)
    template_name = 'appeducation/appeducation-shift-info-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Shift_InfoForm(request.POST, instance=instance_data)
        # print(form)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Shift_InfoForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
        # print(form)
    return JsonResponse(data)


#degree-info

class edu_degree_info_view(TemplateView):
    template_name = 'appeducation/appeducation-degree-info-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Degree_InfoForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_degree_info_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Degree_InfoForm(request.POST)
        if form.is_valid():
            degree_id = fn_get_degree_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.degree_id = degree_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'degree_info Added Successfully!'
            return JsonResponse(data)
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def edu_degree_info_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Degree_Info, degree_id=id)
    template_name = 'appeducation/appeducation-degree-info-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Degree_InfoForm(request.POST, instance=instance_data)
        # print(form)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Degree_InfoForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
        # print(form)
    return JsonResponse(data)


##occupation

class edu_occupation_info_view(TemplateView):
    template_name = 'appeducation/appeducation-occupation-info-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Occupation_InfoForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_occupation_info_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Occupation_InfoForm(request.POST)
        if form.is_valid():
            occupation_id = fn_get_occupation_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.occupation_id = occupation_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'ocupation Added Successfully!'
            return JsonResponse(data)
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def edu_occupation_info_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Occupation_Info, occupation_id=id)
    template_name = 'appeducation/appeducation-occupation-info-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Occupation_InfoForm(request.POST, instance=instance_data)
        # print(form)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Occupation_InfoForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
        # print(form)
    return JsonResponse(data)

### institute...

class edu_educaation_inst_view(TemplateView):
    template_name = 'appeducation/appeducation-educaation-inst-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Education_InstituteForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_educaation_inst_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Education_InstituteForm(request.POST)
        if form.is_valid():
            institute_id = fn_get_institute_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.institute_id = institute_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'degree_info Added Successfully!'
            return JsonResponse(data)
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def edu_educaation_inst_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Education_Institute, institute_id=id)
    template_name = 'appeducation/appeducation-education-inst-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Education_InstituteForm(request.POST, instance=instance_data)
        # print(form)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Education_InstituteForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
        # print(form)
    return JsonResponse(data)


#student informantion:

class edu_student_info_view(TemplateView):
    template_name = 'appeducation/appeducation-student-info-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Student_infoForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_student_info_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Student_infoForm(request.POST)
        if form.is_valid():
            student_roll = fn_get_student_roll()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.student_roll = student_roll
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'student_info Added Successfully!'
            return JsonResponse(data)
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def edu_student_info_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Students_Info, student_roll=id)
    template_name = 'appeducation/appeducation-student-info-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Student_infoForm(request.POST, instance=instance_data)
        # print(form)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Student_infoForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
        # print(form)
    return JsonResponse(data)

## student-addmission:
class edu_student_addmission_view(TemplateView):
    template_name = 'appeducation/appeducation-student-addmission-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Student_AdmissionForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_student_addmission_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Student_AdmissionForm(request.POST)
        if form.is_valid():
            # student_roll = fn_get_student_roll()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            # post.student_roll = student_roll
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'addmission Added Successfully!'
            return JsonResponse(data)
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def edu_student_addmission_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Student_Admission,id=id)
    template_name = 'appeducation/appeducation-student-addmission-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Student_AdmissionForm(request.POST, instance=instance_data)
        # print(form)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Student_AdmissionForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
        # print(form)
    return JsonResponse(data)

####
class edu_result_grade_view(TemplateView):
    template_name = 'appeducation/appeducation-result-grade-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Result_GradeForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_result_grade_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Result_GradeForm(request.POST)
        if form.is_valid():
            grade_id = fn_get_grade_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.grade_id = grade_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'student_info Added Successfully!'
            return JsonResponse(data)
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def edu_result_grade_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Result_Grade, grade_id=id)
    template_name = 'appeducation/appeducation-result-grade-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Result_GradeForm(request.POST, instance=instance_data)
        # print(form)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Result_GradeForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
        # print(form)
    return JsonResponse(data)




class edu_Exam_Type_view(TemplateView):
    template_name = 'appeducation/appeducation-Exam-Type-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Exam_TypeForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_Exam_Type_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Exam_TypeForm(request.POST)
        if form.is_valid():
            examtype_id = fn_get_examtype_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.examtype_id = examtype_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'student_info Added Successfully!'
            return JsonResponse(data)
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def edu_Exam_Type_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Exam_Type, examtype_id=id)
    template_name = 'appeducation/appeducation-Exam-Type-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Exam_TypeForm(request.POST, instance=instance_data)
        # print(form)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Exam_TypeForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
        # print(form)
    return JsonResponse(data)



class edu_Exam_Setup_view(TemplateView):
    template_name = 'appeducation/appeducation-Exam-Setup-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Exam_SetupForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_Exam_Setup_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Exam_SetupForm(request.POST)
        if form.is_valid():
            exam_id = fn_get_exam_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.exam_id = exam_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'student_info Added Successfully!'
            return JsonResponse(data)
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def edu_Exam_Setup_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Exam_Setup, exam_id=id)
    template_name = 'appeducation/appeducation-Exam-Setup-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Exam_SetupForm(request.POST, instance=instance_data)
        # print(form)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Exam_SetupForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
        # print(form)
    return JsonResponse(data)





class edu_Marks_Details_view(TemplateView):
    template_name = 'appeducation/appeducation-Marks-Details-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Exam_Marks_DetailsForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_Marks_Details_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Exam_Marks_DetailsForm(request.POST)
        if form.is_valid():
            # exam_id = fn_get_exam_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            # post.exam_id = exam_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'student_info Added Successfully!'
            return JsonResponse(data)
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)



######
def edu_Marks_Details_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Exam_Marks_Details, id=id)
    template_name = 'appeducation/appeducation-Mark-Details-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Exam_Marks_DetailsForm(request.POST, instance=instance_data)
        # print(form)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Exam_Marks_DetailsForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
        # print(form)
    return JsonResponse(data)





###

class edu_Exam_Marks_Final_view(TemplateView):
    template_name = 'appeducation/appeducation-Exam-Marks-Final-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Exam_Marks_FinalForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)


def edu_Exam_Marks_Final_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Exam_Marks_FinalForm(request.POST)
        if form.is_valid():
            # exam_id = fn_get_exam_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            # post.exam_id = exam_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'sfinal-mark Added Successfully!'
            return JsonResponse(data)
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)



######
def edu_Exam_Marks_Final_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    
    instance_data = get_object_or_404(Exam_Marks_Final, id=id)
    template_name = 'appeducation/appeducation-Exam-Marks-Final-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Exam_Marks_FinalForm(request.POST, instance=instance_data)
        # print(form)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            data['success_message'] = 'Updated Successfully!'
            data['error_message'] = ''
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    else:
        form = Exam_Marks_FinalForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
        # print(form)
    return JsonResponse(data)

# student in with filter
class edu_student_info_filter(TemplateView):
    template_name = 'appeducation/appeducation-student-info-filterlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Student_infoForm()
        exams = Exam_Setup.objects.all()
        context = get_global_data(request)
        context['form'] = form
        context['exams'] = exams
        return render(request, self.template_name, context)

def edu_student_info_filter_list(request):
    template_name = 'appeducation/appeducation-student-info-filtered.html'
    context=dict()
    if request.method == 'POST':
        class_id=request.POST.get('class_id')
        class_group_id=request.POST.get('class_group_id')
        subject_id=request.POST.get('subject_id')
        
        if class_id and class_group_id and subject_id:
            students = Students_Info.objects.raw('''select * from edu_students_info s LEFT JOIN edu_exam_marks_details m 
            on s.class_id='''+"'"+class_id+"'"+" and s.student_roll=m.student_roll and m.subject_id='"+subject_id+"'"+" where s.class_id='"+class_id+"' and s.class_group_id='"+class_group_id+"'")
            context['students'] = students
            return render(request, template_name, context)

        if class_id and subject_id:
            students = Students_Info.objects.raw('''select * from edu_students_info s LEFT JOIN edu_exam_marks_details m 
            on s.class_id='''+"'"+class_id+"'"+" and s.student_roll=m.student_roll and m.subject_id='"+subject_id+"'"+" where s.class_id='"+class_id+"'")
            context['students'] = students
            return render(request, template_name, context)
        
        if class_id and class_group_id:
            students=Students_Info.objects.filter(class_id=class_id,class_group_id=class_group_id)
            context['students'] = students
            return render(request, template_name, context)

        if class_id:
            students=Students_Info.objects.filter(class_id=class_id)
            context['students'] = students
            return render(request, template_name, context)
    students=Students_Info.objects.all()
    context['students'] = students
    return render(request, template_name, context)


def edu_insert_student_mark(request):
    data={}
    if request.method == 'POST':
        exam_id=Exam_Setup.objects.get(exam_id=request.POST.get('exam_id'))
        subject_id=Subject_List.objects.get(subject_id=request.POST.get('subject_id'))
        total_exam_marks=request.POST.get('total_exam_marks')
        obtain_marks=request.POST.get('obtain_marks')
        student_roll=Students_Info.objects.get(student_roll=request.POST.get('student_roll'))
        mark_percent=( float(obtain_marks)/float(total_exam_marks))*100
        result_grade=Result_Grade.objects.filter(lowest_mark__lte = mark_percent, highest_mark__gte=mark_percent)
        # print(result_grade[0])
        
        if Exam_Marks_Details.objects.filter(student_roll=request.POST.get('student_roll'),subject_id=request.POST.get('subject_id'),exam_id=request.POST.get('exam_id')).exists():
            exam_mark=Exam_Marks_Details.objects.get(student_roll=request.POST.get('student_roll'),subject_id=request.POST.get('subject_id'),exam_id=request.POST.get('exam_id'))
            exam_mark.total_exam_marks=total_exam_marks
            exam_mark.obtain_marks=obtain_marks
            exam_mark.result_grade=result_grade[0].grade_name
            exam_mark.grade_point_average=result_grade[0].result_gpa
            exam_mark.app_user_id=request.session["app_user_id"]
            exam_mark.save()
        else:
            exam_mark=Exam_Marks_Details()
            exam_mark.exam_id=exam_id
            exam_mark.subject_id=subject_id
            exam_mark.total_exam_marks=total_exam_marks
            exam_mark.obtain_marks=obtain_marks
            exam_mark.student_roll=student_roll
            exam_mark.result_grade=result_grade[0]
            exam_mark.grade_point_average=result_grade[0].result_gpa
            exam_mark.app_user_id=request.session["app_user_id"]
            exam_mark.save()
        data['result_grade']=str(exam_mark.result_grade)
        data['grade_point']=str(exam_mark.grade_point_average)
    return JsonResponse(data)
    #     jData=json.dumps(data)
    # return HttpResponse(jData,content_type="application/json")


# class student_report(TemplateView):
#     template_name = 'appeducation/appeducation-student-result-all-filterlist.html'
#     def get(self, request):
#         if not request.user.is_authenticated:
#             return render(request, 'appauth/appauth-login.html')
#         form = Student_rollInput()
#         context = get_global_data(request)
#         context['form'] = form
#         return render(request, self.template_name, context)

# def indivitual_total_mark(request):
#     template_name='appeducation/appeducation-student-result-all-filterlist.html'
#     data={}

#     if request.method=="POST":
#         roll=request.POST.get("student_roll")
#         query=Exam_Marks_Details.objects.get(student_roll=roll)
#         print(query)
#         data["total_mark"]=query
#         print(data)
#         return JsonResponse(data)
#         # return render(request,template_name,context=data)

class edu_finalmark_filterview(TemplateView):
    template_name = 'appeducation/appeducation-final-mark-filterlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        classes = Academic_Class.objects.all()
        context = get_global_data(request)
        context['classes'] = classes
        return render(request, self.template_name, context)

def edu_finalmark_filtertable(request):
    template_name = 'appeducation/appeducation-finalmark-filter-table.html'
    students = Students_Info.objects.all()
    context = dict()
    if request.method == 'POST':
        class_id = request.POST.get('class_id')
        if class_id:
            students=Students_Info.objects.raw('''select * from edu_students_info s left join edu_exam_marks_final f on s.class_id='''+"'"+class_id+"'"+"and s.student_roll=f.student_roll where s.class_id='"+class_id+"'")
            context['students']=students
            return render( request, template_name, context)
    context['students']=students
    return render( request, template_name, context)


def edu_finalmark_show(request):
    data={}
    if request.method=='POST':
        student_roll=Students_Info.objects.get(student_roll=request.POST.get('student_roll'))
        query=Exam_Marks_Details.objects.filter(student_roll=student_roll)
        total_marks=0
        obtain_marks=0
        for result in query:
            total_marks=total_marks+result.total_exam_marks
            obtain_marks=obtain_marks+result.obtain_marks
        
        percent=(float(obtain_marks)/float(total_marks))*100
        result_grade=Result_Grade.objects.filter(lowest_mark__lte=percent,highest_mark__gte=percent)

        if Exam_Marks_Final.objects.filter(student_roll=request.POST.get('student_roll')):
            final_marks=Exam_Marks_Final.objects.get(student_roll=request.POST.get('student_roll'))
            final_marks.total_exam_marks = total_marks
            final_marks.obtain_marks=obtain_marks
            final_marks.result_grade=result_grade[0].grade_name
            final_marks.grade_point_average=result_grade[0].result_gpa
            final_marks.app_user_id=request.session["app_user_id"]
            final_marks.save()
        else:
            final_marks=Exam_Marks_Final()
            final_marks.student_roll=student_roll
            final_marks.total_exam_marks = total_marks
            final_marks.obtain_marks=obtain_marks
            final_marks.result_grade=result_grade[0].grade_name
            final_marks.grade_point_average=result_grade[0].result_gpa
            final_marks.app_user_id=request.session["app_user_id"]
            final_marks.save()

        data['total_marks']=str(final_marks.total_exam_marks)
        data['obtain_marks']=str(final_marks.obtain_marks)
        data['result_grade']=str(final_marks.result_grade)
        data['grade_point']=str(final_marks.grade_point_average)
        return JsonResponse(data)
    return JsonResponse(data)


    ##########################################################################

class edu_student_exam_filter(TemplateView):
    template_name = 'appeducation/appeducation-student-exam-filterlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Student_infoForm()
     
        context = get_global_data(request)
        context['form'] = form
        
        return render(request, self.template_name, context)



def edu_student_exam_filter_list(request):
    template_name = 'appeducation/appeducation-student-exam-filtered1.html'
    context=dict()
    if request.method == 'POST':
        class_id=request.POST.get('class_id')
        student_roll=request.POST.get('student_roll')
        subject_id=request.POST.get('subject_id')
        
        if class_id and student_roll and subject_id:
            students = Students_Info.objects.raw('''select * from edu_students_info s LEFT JOIN edu_exam_marks_details m 
            on s.class_id='''+"'"+class_id+"'"+" and s.student_roll=m.student_roll and m.subject_id='"+subject_id+"'"+" where s.class_id='"+class_id+"' and s.student_roll='"+student_roll+"'")
            context['students'] = students
            return render(request, template_name, context)

        if class_id and subject_id:
            students = Students_Info.objects.raw('''select * from edu_students_info s LEFT JOIN edu_exam_marks_details m 
            on s.class_id='''+"'"+class_id+"'"+" and s.student_roll=m.student_roll and m.subject_id='"+subject_id+"'"+" where s.class_id='"+class_id+"'")
            context['students'] = students
            return render(request, template_name, context)
        
        if class_id and student_roll:
            students=Students_Info.objects.filter(class_id=class_id,student_roll=student_roll)
            context['students'] = students
            return render(request, template_name, context)

        if class_id:
            students=Students_Info.objects.filter(class_id=class_id)
            context['students'] = students
            return render(request, template_name, context)
    students=Students_Info.objects.all()
    exams=Exam_Setup.objects.all()
    context['students'] = students
    context['exams']=exam
    return render(request, template_name, context)
