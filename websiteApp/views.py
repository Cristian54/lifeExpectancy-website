from django.shortcuts import render
from django_tables2 import RequestConfig
from django_tables2.export.export import TableExport
import json

from .models import CountriesData
from .tables import OneCountryTable, OneYearTable
from .forms import CountryForm, YearForm

# Create your views here.
def home(request):
    if request.method == 'GET':
        year_data = CountriesData.objects.values('country', 'population', 'life_expectancy').filter(year='1960')
        form = YearForm()
        
        data_dict = {"Country":[], "Population":[], "LifeExpectancy":[]}
        for y in year_data: 
            data_dict['Country'].append(y['country'])
            data_dict['Population'].append(y['population'])
            data_dict['LifeExpectancy'].append(y['life_expectancy'])
        
        data_json = json.dumps(data_dict)
        return render(request, 'home.html', {'countryData':data_json, 'year':'1960', 'form':form, 'yearData':year_data})
    
    elif request.method == 'POST':
        year_data = CountriesData.objects.values('country', 'population', 'life_expectancy').filter(year=request.POST['year_list'])
        form = YearForm()
        
        data_dict = {"Country":[], "Population":[], "LifeExpectancy":[]}
        for y in year_data: 
            data_dict['Country'].append(y['country'])
            data_dict['Population'].append(y['population'])
            data_dict['LifeExpectancy'].append(y['life_expectancy'])
        
        data_json = json.dumps(data_dict)
        return render(request, 'home.html', {'countryData':data_json, 'year':request.POST['year_list'], 'form':form, 'yearData':year_data})

def country(request):
    if request.method == 'GET':
        config = RequestConfig(request, paginate=False)
        usa_data = CountriesData.objects.values('year', 'population', 'life_expectancy').filter(country='United States of America')
        table = OneCountryTable(usa_data)
        config.configure(table)
        
        form = CountryForm()
        return render(request, 'country.html', {'countryData':usa_data, 'country':'United States of America', 'form':form})
        
    elif request.method == 'POST':
        config = RequestConfig(request, paginate=False)
        country_data = CountriesData.objects.values('year', 'population', 'life_expectancy').filter(country=request.POST['country_list'])
        table = OneCountryTable(country_data)
        config.configure(table)
        
        form = CountryForm()
        return render(request, 'country.html', {'countryData':country_data, 'country':request.POST['country_list'], 'form':form})

def year_csv(request): 
    if request.method == 'POST':
        config = RequestConfig(request, paginate=False)
        year_data = CountriesData.objects.values('country', 'population', 'life_expectancy').filter(year=request.POST['year'])
        table = OneYearTable(year_data)
        config.configure(table)
        
        export_format = 'csv'
        if TableExport.is_valid_format(export_format):
            exporter = TableExport(export_format, table)
            return exporter.response(request.POST['year'] + "-Data.{}".format(export_format))

def country_csv(request): 
    if request.method == 'POST':
        config = RequestConfig(request, paginate=False)
        country_data = CountriesData.objects.values('year', 'population', 'life_expectancy').filter(country=request.POST['country_list'])
        table = OneCountryTable(country_data)
        config.configure(table)
        
        export_format = 'csv'
        if TableExport.is_valid_format(export_format):
            exporter = TableExport(export_format, table)
            return exporter.response(request.POST['country_list'] + "-Data.{}".format(export_format))
    