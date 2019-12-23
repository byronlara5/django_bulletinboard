"""bulletindelta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from bulletin.views import Calendar, Home, Birthday_calendar, Memorandum_detail, create_post, feedback_form, feedback_form_success
from django.conf.urls.static import static
from django.conf import settings

from core.views import home, settings_user, picture, upload_picture, password, network, profile
from auth.views import signup
from activities.views import notifications, last_notifications, check_notifications
from django.contrib.auth.views import login, logout



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^create_post/$', create_post, name='create_post'),

    #For feedback
    url(r'^feedback/$', feedback_form, name='feedback'),
    url(r'^feedback/success$', feedback_form_success, name='feedback_form_success'),
    
    #others
    url(r'^login', login, {'template_name': 'cover.html'}, name='login'),
    url(r'^logout', logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^settings/$', settings_user, name='settings'),
    url(r'^settings/picture/$', picture, name='picture'),
    url(r'^settings/upload_picture/$', upload_picture, name='upload_picture'),
    url(r'^settings/password/$', password, name='password'),
    url(r'^network/$', network, name='network'),
    url(r'^feeds/', include('feeds.urls')),
    url(r'^messages/', include('messages.urls')),
    url(r'^notifications/$', notifications, name='notifications'),
    url(r'^notifications/last/$', last_notifications, name='last_notifications'),
    url(r'^notifications/check/$', check_notifications, name='check_notifications'),
    url(r'^user/(?P<username>[\w-]+)/$', profile, name='profile'),
    url(r'^calendar', Calendar, name='calendar'),
    url(r'^birthday', Birthday_calendar, name='birthday'),

    # 3rd Party
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
    # Detail for posts
    url(r'^(?P<slug>[\w-]+)/$', Memorandum_detail, name='memorandum_detail'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
