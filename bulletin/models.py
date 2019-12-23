# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PIL import Image
from io import StringIO	
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

SECTION_CHOICES = (
	('memo', 'Memorandum'),
	('welcome', 'Bienvenida'),
	('promotion', 'Promocion'),
	('meet', 'Conoce compañero'),
	('mournful', 'Nota Luctuosa'),
	('accompli', 'Noti Cumplimiento'),
	('notes', 'Notas de Interes'),
	('birthboy', 'Nacimiento/Niño'),
	('birthgirl', 'Nacimiento/Niña'),
)

LOCATION_CHOICES = (
	('Salón de Entrenamiento - Lexus', 'Salón de Entrenamiento - Lexus'),
	('Salón de Conferencia - Administrativo', 'Salón de Conferencia - Administrativo'),
)


class Event(models.Model):
	title = models.CharField(max_length=80, verbose_name ='titulo')
	allDay = models.BooleanField(verbose_name ='Todo el dia', editable=False, default=False)
	start_date = models.DateField(null=True, verbose_name ='Fecha de inicio')
	start_time = models.TimeField(null=True, verbose_name ='Hora de inicio')
	end_date = models.DateField(null=True, verbose_name ='Fecha de termino')
	end_time = models.TimeField(null=True, verbose_name ='Hora de termino')
	location = models.CharField(max_length=80,choices=LOCATION_CHOICES, default='lexussalon', verbose_name='Lugar')
	url = models.CharField(max_length=80, default='#modal', editable=False)

	backgroundColor = models.CharField(max_length=15, null=True, verbose_name ='Color')

	description = RichTextUploadingField(verbose_name ='Detalles')

	class Meta:
		verbose_name = 'Evento'
		verbose_name_plural = 'Eventos'

	def __unicode__(self):
		return self.title


class Birthday(models.Model):
	name = models.CharField(max_length=80, verbose_name ='Nombre')
	department = models.CharField(max_length=80, verbose_name ='Departamento')
	allDay = models.BooleanField(default=True, verbose_name ='Todo el dia')
	start_date = models.DateField(null=True, verbose_name ='Fecha de inicio')
	start_time = models.TimeField(auto_now=True, verbose_name ='Hora de inicio')
	end_date = models.DateField(null=True, blank=True, editable=False, verbose_name ='Fecha de termino')
	end_time = models.TimeField(auto_now=True, verbose_name ='Hora de termino')
	backgroundColor = models.CharField(max_length=15, null=True, default='#1b9200', editable=False, verbose_name ='Color')

	class Meta:
		verbose_name = 'Cumpleaño'
		verbose_name_plural = 'Cumpleaños'

	def __unicode__(self):
		return self.name

class Memorandum(models.Model):
	section = models.CharField(max_length=30,choices=SECTION_CHOICES, default='memo', verbose_name='Tipo de publicacion')
	title = models.CharField(max_length=30, null=True, verbose_name ='Titulo')
	slug = models.SlugField(max_length=300, verbose_name ='slug')
	active = models.BooleanField(default=True, verbose_name='Activa')
	color = models.CharField(max_length=300, default='#009688')
	picture = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True, verbose_name ='Imagen')
	text = RichTextUploadingField(verbose_name ='Descripcion')
	date = models.DateTimeField(editable=False, auto_now_add=True)

	def get_comments(self):
		return Comment.objects.filter(memo=self)

	class Meta:
		verbose_name = 'Memo'
		verbose_name_plural = 'Memorandums'

	def get_absolute_url(self):
		return reverse('memorandum_detail', args=[self.slug])	

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	memo = models.ForeignKey(Memorandum, related_name='comments')
	user = models.ForeignKey(User)
	comment = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Comentario'
		verbose_name_plural = 'Comentarios'
		ordering = ['date']

	def __unicode__(self):
		return u'{0} - {1}'.format(self.user.username, self.memo.title)

class Feedback(models.Model):
	title = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	
	class Meta:
		verbose_name = 'Sugerencia'
		verbose_name_plural = 'Sugerencias'
	
	def __unicode__(self):
		return self.title