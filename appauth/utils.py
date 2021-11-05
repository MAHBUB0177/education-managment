from appauth.models import *
from django.db import connection, transaction
from django.db.models import Count, Sum, Avg, Max, Min
import datetime
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from decimal import Decimal
import logging
import sys
from django.utils import timezone
from appauth.validations import *
logger = logging.getLogger(__name__)

from appauth.models import *

def get_inv_number(p_inv_code, p_branch_code, p_inv_prefix, p_inv_naration, p_length):
    cursor = connection.cursor()
    cursor.callproc("fn_get_inventory_number", [
                    p_inv_code, p_branch_code, p_inv_prefix, p_inv_naration, p_length])
    inv_number = cursor.fetchone()
    return inv_number

def fn_get_country_id():
    branch_code = 1
    inventory_number = get_inv_number(
        100, branch_code, '', 'Country ID Generate', 6)
    return inventory_number[0]

def fn_get_division_id():
    branch_code = 1
    inventory_number = get_inv_number(
        100, branch_code, '', 'Division ID Generate', 6)
    return inventory_number[0]




def fn_get_upozila_id():
    branch_code = 1
    inventory_number = get_inv_number(
        100, branch_code, '', 'Upozila ID Generate', 6)
    return inventory_number[0]



def fn_get_district_id():
    branch_code = 1
    inventory_number = get_inv_number(
        100, branch_code, '', 'District ID Generate', 6)
    return inventory_number[0]


def fn_get_union_id():
    branch_code = 1
    inventory_number = get_inv_number(
        100, branch_code, '', 'Union ID Generate', 6)
    return inventory_number[0]