from django import forms
from django.db import models
from phone.models import Product


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField()


class ProductCreateFeedback(forms.Form):
    title = forms.FileField(required=False)
    comment = forms.FileField(required=256)