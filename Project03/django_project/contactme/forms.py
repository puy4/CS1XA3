from django import forms
from homepage1.models import Post

class thecontact(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    email = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    first_name = first_name = forms.CharField(required=True)
    title = forms.CharField(required=True)
    class Meta:
        model = Contact
        fields = ['content', 'email', 'last_name','first_name','title' ]
