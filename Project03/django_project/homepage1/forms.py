from django import forms
from .models import Post

class theform(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['content']

class theform(forms.ModelForm):
    class Meta:
        model = Post
        fields = [ ]
