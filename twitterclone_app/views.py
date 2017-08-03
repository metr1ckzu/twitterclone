from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from twitterclone_app.forms import UserCreateForm, AuthenticateForm, TweetForm
from twitterclone_app.models import Tweet
# Create your views here.


def index(request, auth_form=None, user_form=None):
    # User is logged in
    if request.user.is_authenticated():
        tweet_form = TweetForm()
        user = request.user
        tweets_self = Tweet.objects.filter(user=user.id)
        tweets_buddies = Tweet.objects.filter(user__userprofile__in=user.profile.follows.all)
        tweets = tweets_self | tweets_buddies
 
        return render(request,
                      'buddies.html',
                      {'tweet_form': tweet_form, 'user': user,
                       'tweets': tweets,
                       'next_url': '/', })
    else:
        # User is not logged in
        auth_form = auth_form or AuthenticateForm()
        user_form = user_form or UserCreateForm()
 
        return render(request,
                      'home.html',
                      {'auth_form': auth_form, 'user_form': user_form, })