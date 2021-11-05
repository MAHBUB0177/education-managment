from rest_framework import serializers
import datetime

from appauth.models import *

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('__all__')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Loc_Country
        fields = ('__all__')

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loc_Division
        fields = ('__all__')


class UpozilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loc_Upazila
        fields = ('__all__')


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loc_District
        fields = ('__all__')

class UnionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loc_Union
        fields = ('__all__')