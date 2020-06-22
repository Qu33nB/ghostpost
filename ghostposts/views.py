from django.shortcuts import render, reverse, HttpResponseRedirect

from ghostposts.models import GhostPost
from ghostposts.forms import GhostPostForm

html= 'index.htm'

def index(request):
    data = GhostPost.objects.all().order_by('-submission_time')
    return render(request, html, {'data': data})


def add_ghost_post(request):
    if request.method == 'POST':
        form = GhostPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GhostPost.objects.create(
                boast_or_roast=data['boast_or_roast'],
                post=data['post'],
            )
        return HttpResponseRedirect(reverse('home'))

    form = GhostPostForm()
    return render(request, 'post.htm', {'form': form})

def boasts(request):
    data = GhostPost.objects.filter(boast_or_roast=True).order_by('-submission_time')
    return render(request, html, {'data': data})

def roasts(request):
    data = GhostPost.objects.filter(boast_or_roast=False).order_by('-submission_time')
    return render(request, html, {'data': data})

def likes(request, id):
    post = GhostPost.objects.get(id=id)
    post.up_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))

def dislikes(request, id):
    post = GhostPost.objects.get(id=id)
    post.down_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))

def most_liked(request):
    data = GhostPost.objects.order_by('-up_votes')
    return render(request, html, {'data': data})

def least_liked(request):
    data = GhostPost.objects.order_by('up_votes')
    return render(request, html, {'data': data})
