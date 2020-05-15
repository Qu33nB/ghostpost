from django.shortcuts import render

from ghostposts.models import GhostPost
from ghostposts.forms import GhostPostForm
# Create your views here.
def index(request):
    data = GhostPost.objects.all()
    return render(request, 'index.html', {'data': data})


def ghost_post(request):
    if request.method == 'POST':
        form = GhostPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GhostPost.objects.all()
        return render(request, 'addpost.html', {'data': data, 'form': form})

    form = GhostPostForm()
    return render(request, 'post.html', {'form': form})