import django_filters
from django_filters import DateFilter
from django_filters import CharFilter, ChoiceFilter, NumberFilter

from .models import Voyage 



class FlightsFilter(django_filters.FilterSet):

   	#name = django_filters.CharFilter(lookup_expr='iexact')

	#start_date = DateFilter(field_name='datedep', lookup_expr='gte')
	#end_date = DateFilter(field_name='datedep', lookup_expr='lte')	    
    
	depart = CharFilter(field_name ='depart', lookup_expr='icontains')
	destination = CharFilter(field_name ='destination', lookup_expr = 'icontains')
    # name__icontains = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

	datedep = DateFilter(field_name ='datedep', lookup_expr='date')
 	

	class Meta:
		model = Voyage
		fields = '__all__'
		exclude = ['voyid', 'avion']


# class searchFilter(django_filters.FilterSet):

# 	addressName = CharFilter(field_name='address__address', lookup_expr = 'icontains')
