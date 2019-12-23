from django.shortcuts import render, redirect, get_object_or_404
from feeds.views import feeds
from django.contrib.auth.models import User
from feeds.models import Feed
from auth.models import Profile
from feeds.views import FEEDS_NUM_PAGES
from bulletin.views import Home
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from core.forms import ProfileForm, ChangePasswordForm
from django.contrib import messages
from django.conf import settings as django_settings
from PIL import Image
from django.db.models import Count
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect,\
    HttpResponseBadRequest, Http404
import os

def home(request):
    if request.user.is_authenticated():
        return Home(request)
    else:
        return render(request, 'cover.html')

@login_required
def network(request):
    users = User.objects.filter(is_active=True).order_by('username')
    return render(request, 'core/network.html', {'users': users})

@login_required
def profile(request, username):
    page_user = get_object_or_404(User, username=username)
    all_feeds = Feed.get_feeds().filter(user=page_user)
    paginator = Paginator(all_feeds, FEEDS_NUM_PAGES)
    feeds = paginator.page(1)
    from_feed = -1
    if feeds:
        from_feed = feeds[0].id
    return render(request, 'core/profile.html', {
        'page_user': page_user,
        'feeds': feeds,
        'from_feed': from_feed,
        'cur_user': page_user
        #'page': 1
        })

@login_required 
def settings_user(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.job_title = form.cleaned_data.get('job_title')
            user.profile.url = form.cleaned_data.get('url')
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Your profile were successfully edited.')
    else:
        form = ProfileForm(instance=user, initial={
            'url': user.profile.url,
            'location': user.profile.location,
            })
    return render(request, 'core/settings.html', {'form':form})

@login_required
def picture(request):
    uploaded_picture = False
    try:
        if request.GET.get('upload_picture') == 'uploaded':
            uploaded_picture = True
    except Exception as e:
        pass
    return render(request, 'core/settings.html', {'uploaded_picture': uploaded_picture})

@login_required
def password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Your password were successfully changed.')
        return redirect('/')
    else:
        form = ChangePasswordForm(instance=user)
    return render(request, 'core/password.html', {'form':form})

@login_required
def upload_picture(request):
    try:
        profile_pictures = django_settings.MEDIA_ROOT + '/profile_pictures/'
        if not os.path.exists(profile_pictures):
            os.makedirs(profile_pictures)
        f = request.FILES['picture']
        filename = profile_pictures + request.user.username + '.jpg'
        with open(filename, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)    
        im = Image.open(filename)
        width, height = im.size
        if width > 350:
            new_width = 350
            new_height = (height * 350) / width
            new_size = new_width, new_height
            im.thumbnail(new_size, Image.ANTIALIAS)
            im.save(filename)
        return redirect('/settings/')
    except Exception as e:
        return redirect('/settings/picture/')

