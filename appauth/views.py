from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import FieldDoesNotExist
from django.core import serializers
from random import randint
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import datetime
from datetime import date, datetime, timedelta
from django.db import connection, transaction
from django.template.loader import render_to_string
from django.db.models import Count, Sum, Avg
import logging
import sys
logger = logging.getLogger(__name__)
from decimal import Decimal

all_permissions = {}

from .models import *
from .forms import *
from .utils import *
from .validations import *
from .myException import *


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

class HomeView(TemplateView):
    template_name = 'appauth/appauth-login.html'

def appauth_home(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    # Get a session value by its key
    user_full_name = request.session['user_full_name']
    # global all_permissions
    # if not request.user.is_authenticated:
    #     return render(request, "appauth/appauth-login.html", {"message": None})
    context = get_global_data(request)
    # print(all_permissions)
    return render(request, "appauth/appauth-home.html", context)

def login_view(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    global all_permissions
    branch_code = ''

    try:

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            user_info = User.objects.get(username=username)
            all_permissions = user_info.get_all_permissions()

            request.session['user_full_name'] = user_info.first_name + \
                " "+user_info.last_name
            request.session['app_user_id'] = username
            app_setting = Global_Parameters.objects.get()
            request.session['application_title'] = app_setting.application_title
            return HttpResponseRedirect(reverse("appauth-home"))
        else:
            return render(request, "appauth/appauth-login.html", {"message": "Invalid credentials."})

    except Exception as e:
        print(str(e))
        return render(request, "appauth/appauth-login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "appauth/appauth-login.html", {"message": "Logged out."})

class reset_password(TemplateView):
    template_name = 'appauth/appauth-reset-password.html'

def reset_user_password(request):

    new_password = request.POST.get('new_password', False)
    old_password = request.POST.get('password', False)
    user_name = request.POST.get('username', False)
    confirm_password = request.POST.get('new_password_confirm', False)

    if new_password != confirm_password:
        return render(request, "appauth/appauth-reset-password.html", {"message": "New password and confirm password does not match!"})

    user = authenticate(request, username=user_name, password=old_password)

    if user is not None:
        user = User.objects.get(username=user_name)
        user_info = User_Settings.objects.get(app_user_name=user_name)
        user_info.reset_user_password = False
        user.set_password(new_password)
        user.save()
        user_info.save()
        return render(request, "appauth/appauth-login.html", {"message": "Password Reset Successfully"})
    else:
        return render(request, "appauth/appauth-reset-password.html", {"message": "Invalid Credentials!"})

def DashboardView(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    context = get_global_data(request)
    data = dict()
    try:
        app_user_id = request.session["app_user_id"]
        #cbd = get_business_date(branch_code)
        #cursor = connection.cursor()
        #cursor.callproc("fn_fin_dashboard_data",[branch_code, somity_code, app_user_id, cbd])
        #row = cursor.fetchone()
    except Exception as e:
        data['form_is_valid'] = False
        logger.error("Error in finance_ledger_balance on line {} \nType: {} \nError:{}".format(
            sys.exc_info()[-1], type(e).__name__, str(e)))
            
class CreateUser(TemplateView):
    template_name = 'appauth/appauth-app-user.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = AppUserModelForm()
        context = get_global_data(request)
        context['success_message'] = ''
        context['error_message'] = ''
        context['form'] = form
        return render(request, self.template_name, context)

    @transaction.atomic
    def post(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        context = get_global_data(request)
        form = AppUserModelForm(request.POST)
        error_message = "Please check the error"
        success_message = ""
        if form.is_valid():

            try:
                with transaction.atomic():
                    user_setting = Global_Parameters.objects.get()
                    user_name = form.cleaned_data["app_user_name"]
                    employee_name = form.cleaned_data["employee_name"]
                    user_password = 'Pass'+str(randint(1111, 9999))
                    user = User.objects.create_user(
                        user_name, '', user_password)
                    user.last_name = employee_name
                    user.save()

                    user_info = User.objects.get(username=user_name)
                    post = form.save(commit=False)
                    post.app_user_id = user_info.id
                    post.reset_user_password = True
                    post.cash_gl_code = user_setting.cash_gl_code

                    post.save()
                    success_message = "User Created Successfully! \nTemporary password for the User : "+user_password
                    error_message = ""
                    form = AppUserModelForm()
            except Exception as e:
                logger.error("Error in Creating User {} \nType: {} \nError:{}".format(
                    sys.exc_info()[-1], type(e).__name__, str(e)))
                context['form'] = form
                context['success_message'] = success_message
                context['error_message'] = 'Error '+str(e)+' in Creating User!'
                return render(request, self.template_name, context)
        else:
            error_message = form.errors.as_json()

        context['form'] = form
        context['success_message'] = success_message
        context['error_message'] = error_message
        return render(request, self.template_name, context)


class ApplicationUserList(TemplateView):
    template_name = 'appauth/appauth-application-users.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        forms = AppUserSearch()
        context = get_global_data(request)
        context['forms'] = forms
        return render(request, self.template_name, context)


@csrf_exempt
@transaction.atomic
def reset_appuser_password(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')

    data = dict()
    data['success_message'] = ''
    data['form_is_valid'] = False
    data['error_message'] = ''
    try:
        with transaction.atomic():
            user_info = User_Settings.objects.get(id=id)
            user = User.objects.get(username=user_info.app_user_name)
            user_info.reset_user_password = True
            new_password = 'Pass'+str(randint(1111, 9999))
            user.set_password(new_password)
            user.save()
            user_info.save()
            data['form_is_valid'] = True
            data['success_message'] = 'Password Reset Successfylly\nNew temporary password for this user : '+new_password
    except Exception as e:
        data['form_is_valid'] = False
        data['error_message'] = str(e)
        logger.error("Error on line {} \nType: {} \nError:{}".format(
            sys.exc_info()[-1], type(e).__name__, str(e)))
        return JsonResponse(data)

    return JsonResponse(data)


class appauth_branch_view(TemplateView):
    template_name = 'appauth/appauth-branch-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = BranchModelForm()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)

def appauth_branch_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = BranchModelForm(request.POST)
        if form.is_valid():
            branch_code = form.cleaned_data["branch_code"]
            if fn_val_check_branch_exist(branch_code):
                data['error_message'] = 'Branch Code Already Exist!'
                return JsonResponse(data)

            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'Branch Opened Successfully!'
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def appauth_branch_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
        
    instance_data = get_object_or_404(Branch, branch_code=id)
    old_branch_code = instance_data.branch_code
    template_name = 'appauth/appauth-branch-edit.html'
    data = dict()

    if request.method == 'POST':
        form = BranchModelForm(request.POST, instance=instance_data)
        data['form_error'] = form.errors.as_json()
        if form.is_valid():
            branch_code = form.cleaned_data["branch_code"]

            if branch_code != old_branch_code:
                data['error_message'] = 'Branch Code Modification is Not Allowed!'
                data['form_is_valid'] = False
                return JsonResponse(data)

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
        form = BranchModelForm(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
    return JsonResponse(data)

class appauth_country_view(TemplateView):
    template_name = 'appauth/appauth-country-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Country_Model_Form()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)

def appauth_country_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Country_Model_Form(request.POST)
        if form.is_valid():
            country_id = fn_get_country_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.country_id = country_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'Country Added Successfully!'
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def appauth_country_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
        
    instance_data = get_object_or_404(Loc_Country, country_id=id)
    template_name = 'appauth/appauth-country-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Country_Model_Form(request.POST, instance=instance_data)
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
        form = Country_Model_Form(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
    return JsonResponse(data)







class appauth_division_view(TemplateView):
    template_name = 'appauth/appauth-division-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Division_Model_Form()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)

def appauth_division_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Division_Model_Form(request.POST)
        if form.is_valid():
            division_id = fn_get_division_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.division_id = division_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'Division Added Successfully!'
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def appauth_division_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
        
    instance_data = get_object_or_404(Loc_Division, division_id=id)
    template_name = 'appauth/appauth-division-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Division_Model_Form(request.POST, instance=instance_data)
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
        form = Division_Model_Form(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
    return JsonResponse(data)






class appauth_upozila_view(TemplateView):
    template_name = 'appauth/appauth-upozila-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Upazila_Model_Form()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)

def appauth_upozila_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Upazila_Model_Form(request.POST)
        if form.is_valid():
            upozila_id = fn_get_upozila_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.upozila_id = upozila_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'Upozila Added Successfully!'
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def appauth_upozila_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
        
    instance_data = get_object_or_404(Loc_Upazila, upozila_id=id)
    template_name = 'appauth/appauth-upozila-edit.html'
    data = dict()

    if request.method == 'POST':
        form = Upazila_Model_Form(request.POST, instance=instance_data)
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
        form = Upazila_Model_Form(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
    return JsonResponse(data)





class appauth_district_view(TemplateView):
    template_name = 'appauth/appauth-district-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = District_Model_Form()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)

def appauth_district_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = District_Model_Form(request.POST)
        if form.is_valid():
            district_id = fn_get_district_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.district_id = district_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'District Added Successfully!'
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def appauth_district_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
        
    instance_data = get_object_or_404(Loc_District, district_id=id)
    template_name = 'appauth/appauth-district-edit.html'
    data = dict()

    if request.method == 'POST':
        form = District_Model_Form(request.POST, instance=instance_data)
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
        form = District_Model_Form(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
    return JsonResponse(data)



class appauth_union_view(TemplateView):
    template_name = 'appauth/appauth-union-createlist.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = Union_Model_Form()
        context = get_global_data(request)
        context['form'] = form
        return render(request, self.template_name, context)

def appauth_union_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data = dict()
    data['form_is_valid'] = False

    if request.method == 'POST':
        form = Union_Model_Form(request.POST)
        if form.is_valid():
            union_id = fn_get_union_id()
            post = form.save(commit=False)
            post.app_user_id = request.session["app_user_id"]
            post.union_id = union_id
            post.save()
            data['form_is_valid'] = True
            data['success_message'] = 'Union Added Successfully!'
        else:
            data['error_message'] = form.errors.as_json()
    return JsonResponse(data)

def appauth_union_edit(request, id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
        
    instance_data = get_object_or_404(Loc_Union, union_id=id)
    template_name = 'appauth/appauth-union-edit.html'
    data = dict()

    if request.method == 'POST':
        form = District_Model_Form(request.POST, instance=instance_data)
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
        form = District_Model_Form(instance=instance_data)
        context = get_global_data(request)
        context['form'] = form
        context['id'] = id
        data['html_form'] = render_to_string(
            template_name, context, request=request)
    return JsonResponse(data)



# class appauth_User_Settings_view(TemplateView):
#     template_name='appauth/appauth-user-setting-createlist.html'

#     def get(self, request):
#         if not request.user.is_authenticated:
#              return render(request, 'appauth/appauth-login.html')

#         form=user_setting_Form()
#         context=get_global_data(request)
#         context['form']=form
#         return render(request,self.template_name,context)


# def appauth_user_setting_nsert(request):
#     if not request.user.is_authenticated:
#         return render(request,'appauth/appauth-login.html')

#         data=dict()
#         data['form.is_valid']=False

#         if request.method=='POST':
#             from=user_setting_Form(request.POST)
#             if form.is_valid():
                
