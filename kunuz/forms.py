from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
class AddNews(forms.Form):
    theme = forms.CharField(label='Mavzu',max_length = 300)
    text = forms.CharField(label='Text',max_length = 1000)
    tag = forms.CharField(label='Hashtag',max_length=50)
    image = forms.ImageField(label='Rasm yuklash')