from django.db import models
from django import forms
# Create your models here.

class TODO(models.Model):
    complete = models.BooleanField(default=False)
    todo_text = models.CharField(max_length=60)

    def __str__(self):
        return self.todo_text









class TODO_FORM(forms.Form):
    text = forms.CharField(max_length=45, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'A Django Todo'
    }))