from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from auth.forms import SignUpForm
from django.contrib.auth.models import User
from feeds.models import Feed

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'signup.html', {'form': form})
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            welcome_post = u'{0} Se ha unido'.format(user.username, user.username)
            feed = Feed(user=user, post=welcome_post)
            feed.save()
            return redirect('/')
    else:
        return render(request, 'signup.html', {'form': SignUpForm()})