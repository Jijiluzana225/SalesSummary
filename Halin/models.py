
from django.db import models

class LugawanHalin(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.CharField(max_length=150)
    transdate = models.DateTimeField(blank=True, null=True)
    item = models.CharField(max_length=150)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lugawan_halin'

class LugawanExpense(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.CharField(max_length=150)
    transdate = models.DateTimeField(blank=True, null=True)
    expense = models.CharField(max_length=150)
    price = models.FloatField(blank=True, null=True)
    notes = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    qty = models.DecimalField(db_column='Qty', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lugawan_expense'