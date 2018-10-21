from django import forms
from .models import Choice

class createform(forms.ModelForm):

    class Meta:
        model  = Choice
        fields=[
            'choice_text',
            'votes',
            'question'
        ]