from django.shortcuts import render, reverse, HttpResponseRedirect

from ghostposts.models import GhostPost
from ghostposts.forms import GhostPostForm
# Create your views here.
def index(request):
    data = GhostPost.objects.all()
    return render(request, 'index.htm', {'data': data})


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