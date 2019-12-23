# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from bulletin.models import Event, Birthday, Memorandum, Comment, Feedback 
from bulletin.forms import EventForm
# 3rd party
from import_export import resources, fields
from import_export.admin import ImportExportMixin, ExportActionModelAdmin 
from datetime import date



# Register your models here.
class BirthdayResource(resources.ModelResource):

	def before_import_row(self, row, **kwargs):
		date_row = row.get('start_date') #Fecha del archivo a importar
		today = date.today().isoformat() #Fecha del sistema para tomar el ano
		
		year = today[0:4]
		row_month = str(date_row[5:7])
		row_day = str(date_row[8:10])

		if row_month == '02' and row_day == '29':
			full_date = year + '-' + '03' + '-' + '01'
		else:
			full_date = year + '-' + row_month + '-' + row_day

		row['start_date'] = full_date
		

		

	class Meta:
		model = Birthday


class BirthdayResAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = BirthdayResource
	list_filter = ('department',)
	list_display = ('name', 'department', 'start_date')


class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'memo', 'date')


class MemorandumResource(resources.ModelResource):

	class Meta:
		model = Memorandum

class MemorandumResAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = MemorandumResource
	list_display = ('title', 'section', 'active', 'date')
	list_filter = ('section', 'active', 'date')
	prepopulated_fields = {'slug': ('title',)}


class EventAdmin(admin.ModelAdmin):
	"""docstring for EventAdmin"""
	form = EventForm
	list_filter = ('location',)
		



admin.site.register(Event, EventAdmin)
admin.site.register(Feedback)
admin.site.register(Birthday, BirthdayResAdmin)
admin.site.register(Memorandum, MemorandumResAdmin)
admin.site.register(Comment, CommentAdmin)