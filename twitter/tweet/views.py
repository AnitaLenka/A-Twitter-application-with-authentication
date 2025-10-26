
from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

def tweet_list(request):
    query = request.GET.get('q')
    if query:
        tweets = Tweet.objects.filter(
            Q(text__icontains=query) | Q(user__username__icontains=query)
        ).order_by('-created_at')
    else:
        tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    if tweet.user != request.user:
        return redirect('tweet_list')
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    if tweet.user == request.user:
        tweet.delete()
    return redirect('tweet_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
