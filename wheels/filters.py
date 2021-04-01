from django.db.models import fields
import django_filters

from .models import *

class PartFilter(django_filters.FilterSet):
    class Meta:
        model = WheelPart
        fields = ('Model_year','Car_model','Engine_type','Name_of_part')