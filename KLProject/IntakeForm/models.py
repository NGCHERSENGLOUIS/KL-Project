"""
This file is used to design the database, 
where each class will represent a table,
while its contents will be the columns in the table.

*Note that inserts into the table will automatically create a primary key (pk)
"""

from django.db import models
from django.urls import reverse #only required if we want to link back to old url

#Admin Form Application
#class AdminDetails(models.Model):
