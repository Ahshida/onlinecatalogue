from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.

class ComUser(models.Model):
    name=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    address=models.CharField(max_length=1000)
    contact=models.IntegerField()
    postcode=models.IntegerField()
    email=models.CharField(max_length=100,primary_key=True)

class ToolsInfo(models.Model):
    steel = models.TextField(db_column='Steel', blank=True, null=True)  # Field name made lowercase.
    categories = models.TextField(blank=True, null=True)
    din = models.TextField(db_column='DIN', blank=True, null=True)  # Field name made lowercase.
    assab = models.TextField(db_column='ASSAB', blank=True, null=True)  # Field name made lowercase.
    aisi = models.TextField(db_column='AISI', blank=True, null=True)  # Field name made lowercase.
    jis = models.TextField(db_column='JIS', blank=True, null=True)  # Field name made lowercase.
    availablein = models.TextField(db_column='AvailableIn', blank=True, null=True)
    imagelinks=models.TextField(db_column='imagelinks',blank=True, null=True,max_length=400)
    

    class Meta:
        managed = True
        db_table = 'ToolsInfo'


class Enquiry(models.Model):
    who=models.CharField(max_length=100)
    orderText=models.CharField(max_length=100)
    leadTime=models.CharField(max_length=100)
    enquiryId=models.AutoField(primary_key=True)
    timeofEnquiry=models.DateTimeField(default=datetime.now,blank=False)

    class Meta:
        managed = True
        db_table = 'Enquiry'


