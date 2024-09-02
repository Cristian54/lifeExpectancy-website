from django import db
from django.db import models

# Create your models here.
class CountriesData(models.Model):
    country = models.TextField(db_column='CountryName')  
    year = models.TextField(db_column='Year')  
    life_expectancy = models.TextField(db_column='LifeEx', blank=True) 
    population = models.TextField(db_column='Population', blank=True) 
    dummy_id = models.IntegerField(db_column='dummyID', primary_key=True)
    
    class Meta:
        managed = False
        db_table = 'Countries'

