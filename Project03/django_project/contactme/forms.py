from django import forms
from homepage1.models import Post

class thecontact(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    email = forms.CharField(required=True)
    last_name = models.CharField(required=True)
    first_name = first_name = models.CharField(required=True)
    title = models.CharField(required=True)
    class Meta:
        model = Contact
        fields = ['content', 'email', 'last_name','first_name','title' ]
