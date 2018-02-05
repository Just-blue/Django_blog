
from django import forms
from .models import CommentModel


class CommentForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'size': '25'}))
    url = forms.CharField(widget=forms.TextInput(attrs={'size': '10'}))
    class Meta:
        model = CommentModel
        fields = ['name', 'email', 'url', 'text']