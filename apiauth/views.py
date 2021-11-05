from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Case, CharField, Value, When, F
from rest_framework import generics
from rest_framework.generics import ListAPIView
# Create your views here.

from appauth.models import *

from apiauth.serializers import *

class BranchApiView(generics.ListAPIView):
    serializer_class = BranchSerializer
    def get_queryset(self):
        branch_code = self.request.query_params.get('branch_code',None)
        branch_name = self.request.query_params.get('branch_name',None)

        queryset = Branch.objects.filter().order_by('branch_name')

        if branch_code:
            queryset = queryset.filter(branch_code=branch_code)

        return queryset





class Country_Api_View(generics.ListAPIView):
    serializer_class = CountrySerializer
    def get_queryset(self):
        country_id = self.request.query_params.get('country_id',None)

        queryset = Loc_Country.objects.filter().order_by('country_name')

        if country_id:
            queryset = queryset.filter(country_id=country_id)

        return queryset


class Division_Api_View(generics.ListAPIView):
    serializer_class = DivisionSerializer
    def get_queryset(self):
        division_id = self.request.query_params.get('division_id',None)

        queryset = Loc_Division.objects.filter().order_by('division_name')

        if division_id:
            queryset = queryset.filter(division_id=division_id)

        return queryset




class Upozila_Api_View(generics.ListAPIView):
    serializer_class = UpozilaSerializer
    def get_queryset(self):
        upozila_id = self.request.query_params.get('upozila_id',None)

        queryset = Loc_Upazila.objects.filter().order_by('upozila_name')

        if upozila_id:
            queryset = queryset.filter(upozila_id=upozila_id)

        return queryset


class District_Api_View(generics.ListAPIView):
    serializer_class = DistrictSerializer
    def get_queryset(self):
        district_id = self.request.query_params.get('district_id',None)

        queryset = Loc_District.objects.filter().order_by('district_name')

        if district_id:
            queryset = queryset.filter(district_id=district_id)

        return queryset


class Union_Api_View(generics.ListAPIView):
    serializer_class = UnionSerializer
    def get_queryset(self):
        union_id = self.request.query_params.get('union_id',None)

        queryset = Loc_Union.objects.filter().order_by('union_name')

        if union_id:
            queryset = queryset.filter(union_id=union_id)

        return queryset