from django import forms

from message.models import MessageModel


class MessageForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'size': '10'}))
    web = forms.URLField(required=False,widget=forms.TextInput(attrs={'size': '10'}))
    class Meta:
        model = MessageModel
        fields = ['name', 'email', 'web', 'content']