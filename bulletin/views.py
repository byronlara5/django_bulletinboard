# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from collections import OrderedDict

from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from utilitys.decorators import ajax_required

import json


from bulletin.models import Event, Birthday, Memorandum, Comment
from bulletin.forms import CommentForm, FeedbackForm


# Create your views here.
def Home(request):
	#cumpleaños y eventos
	today = datetime.now()
	a_birthdays = Birthday.objects.filter(start_date=today)
	a_events = Event.objects.filter(start_date=today)
	memos = Memorandum.objects.filter(active=True).order_by('-date')

	#pagination
	paginator = Paginator(memos, 8)
	page = request.GET.get('page')

	try:
		memosp = paginator.page(page)
	except PageNotAnInteger:
		memosp = paginator.page(1)
	except EmptyPage:
		memosp = paginator.page(paginator.num_pages)

	
	template = loader.get_template('index.html')
	context = {
		'memosp' : memosp,
		'a_birthdays' : a_birthdays,
		'a_events' : a_events,
	}
	return HttpResponse(template.render(context, request))

def Memorandum_detail(request, slug):
	memos = get_object_or_404(Memorandum, slug=slug)

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.memo = memos
			comment.user = request.user
			comment.save()
			return redirect('memorandum_detail', slug=memos.slug)
	else:
		form = CommentForm()

	template = loader.get_template('memo_detail.html')
	context = {
		'memos' : memos,
		'form' : form,
	}

	return HttpResponse(template.render(context, request))


def Birthday_calendar(request):
	today = datetime.now()
	birthdays = Birthday.objects.all()
	birthdayToday = Birthday.objects.filter(start_date=today)
	listsb_result =[]

	for lisb in birthdays:
		temb = OrderedDict()
		temb['id'] = lisb.id
		temb['title'] = lisb.name
		temb['department'] = lisb.department
		temb['allDay'] = lisb.allDay
		temb['start'] = str(lisb.start_date) + 'T' + str(lisb.start_time)
		temb['end'] = str(lisb.end_date) + 'T' + str(lisb.end_time)
		temb['backgroundColor'] = lisb.backgroundColor
		listsb_result.append(temb)
		json.dumps(listsb_result)

	context = {
		'data': json.dumps(listsb_result),
		'birthdayToday': birthdayToday,
	}


	return render(request, 'birthday.html',context)
	

def Calendar(request):
	events = Event.objects.all()
	eventsDetail = Event.objects.all()
	lists_result =[]

	for lisp in events:
		temp = OrderedDict()
		temp['id'] = lisp.id
		temp['title'] = lisp.title
		temp['allDay'] = lisp.allDay
		temp['start'] = str(lisp.start_date) + 'T' + str(lisp.start_time)
		temp['end'] = str(lisp.end_date) + 'T' + str(lisp.end_time)
		temp['backgroundColor'] = lisp.backgroundColor
		temp['url'] = str(lisp.url) + str(lisp.id)

		lists_result.append(temp)
		json.dumps(lists_result)

	context = {
		'data': json.dumps(lists_result),
		'eventsDetail': eventsDetail,
	}

	return render(request, 'calendar.html',context)


def create_post(request):
    if request.method == 'POST':
    	memo_id = request.POST.get('memo')
    	article = get_object_or_404(Memorandum, slug=memo_id)
    	post_text = request.POST.get('the_post')
    	if post_text is not '':
        	post = Comment(memo=article, comment=post_text, user=request.user)
        	post.save()
        	return HttpResponseRedirect('/')

def feedback_form(request):
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			feed = form.save(commit=False)
			feed.date = datetime.now()
			feed.save()
			return HttpResponseRedirect('/feedback/success')
	else:
		form = FeedbackForm()

	template = loader.get_template('feedback.html')
	context = {
	'form' : form,
	}
	
	return HttpResponse(template.render(context, request))

def feedback_form_success(request):
	return render(request,'feedback_success.html',)