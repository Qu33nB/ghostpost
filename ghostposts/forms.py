from django import forms
from ghostposts.models import GhostPost

class GhostPostForm(forms.Form):
    boast_or_roast = forms.BooleanField(help_text='Check this box to boast about someone/something!')
    post = forms.CharField(max_length=750)
    up_votes = forms.IntegerField(disabled=True)
    down_votes = forms.IntegerField(disabled=True)
    submission_time = forms.DateTimeField(localize=True)