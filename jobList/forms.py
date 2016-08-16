from django import forms
from .models import UrlList

class PostForm(forms.ModelForm):

    class Meta:
        model = UrlList
        fields = ('title', 'posting_url', 'text', )
