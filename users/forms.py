from django import forms
from .models import Message

class MessagePost(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'text',
        ]