# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Movie(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True, null=True) # Field renamed because it started with '_'.
    field_title = models.TextField(db_column='_title', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    field_director = models.TextField(db_column='_director', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    field_writer = models.TextField(db_column='_writer', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    field_actor = models.TextField(db_column='_actor', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    field_summary = models.TextField(db_column='_summary', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    field_comment_time = models.TextField(db_column='_comment_time', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    field_comment_level = models.TextField(db_column='_comment_level', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    field_url = models.TextField(db_column='_url', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'Movie'

class Movie2(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True, blank=True, null=True) # Field renamed because it started with '_'.
    field_title = models.TextField(db_column='_title', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    field_director = models.TextField(db_column='_director', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    field_writer = models.TextField(db_column='_writer', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    field_actor = models.TextField(db_column='_actor', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    field_summary = models.TextField(db_column='_summary', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    field_comment_time = models.TextField(db_column='_comment_time', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    field_comment_level = models.TextField(db_column='_comment_level', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    field_url = models.TextField(db_column='_url', blank=True) # Field renamed because it started with '_'. This field type is a guess.
    class Meta:
        managed = False
        db_table = 'Movie2'

