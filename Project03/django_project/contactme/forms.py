from django import forms
from homepage1.models import Post

class thecontact(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    email = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    first_name = first_name = forms.CharField(required=True)
    title = forms.CharField(required=True)
