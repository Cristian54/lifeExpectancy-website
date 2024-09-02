from django import forms
from .models import CountriesData

class CountryForm(forms.Form):
    countries = CountriesData.objects.values('country').distinct()
    c_list = [(c['country'], c['country']) for c in countries]
    c_list.insert(0, ('', 'Select a country'))
    c_tuple = tuple(c_list)

    country_list = forms.ChoiceField(choices=c_tuple, label="", required=True, 
                                     widget=forms.Select(attrs={'style': 'max-width: 300px;','class':'form-control'}))
    
class YearForm(forms.Form):
    years = CountriesData.objects.values('year').distinct()
    y_list = [(y['year'], y['year']) for y in years]
    y_list.insert(0, ('', 'Select a year'))
    y_tuple = tuple(y_list)
    
    year_list = forms.ChoiceField(choices=y_tuple, label="", required=True, 
                                     widget=forms.Select(attrs={'style': 'max-width: 300px;','class':'form-control'}))