import django_tables2 as tables
from .models import CountriesData

class OneYearTable(tables.Table):
    population = tables.TemplateColumn(
        template_code="{% load humanize %}{{ value | intcomma }}",
        initial_sort_descending=True
    )
    life_expectancy = tables.TemplateColumn(
        template_code = "{{ value|floatformat:2 }}", 
        verbose_name = "Life Expectancy",
        initial_sort_descending=True
    )
    
    class Meta:
        model = CountriesData 
        template_name = "django_tables2/bootstrap.html"
        fields = ("country", "population", "life_expectancy")
        attrs = {'class': 'table table-striped table-hover',
                 'border':'2px solid black'}
        export_formats = ['csv']


class OneCountryTable(tables.Table):
    population = tables.TemplateColumn(
        template_code="{% load humanize %}{{ value | intcomma }}",
        initial_sort_descending=True, 
    )
    life_expectancy = tables.TemplateColumn(
        template_code = "{{ value|floatformat:2 }}", 
        verbose_name = "Life Expectancy",
        initial_sort_descending=True
    )
    year = tables.Column(initial_sort_descending=True)
    
    class Meta:
        model = CountriesData 
        template_name = "django_tables2/bootstrap.html"
        fields = ("year", "population", "life_expectancy")
        attrs = {'class': 'table table-striped table-hover',
                 'border':'2px solid black'}
        export_formats = ['csv']