from django import forms
from notes.models import Post
from pagedown.widgets import PagedownWidget

class theform(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ('content', 'user', 'date')
