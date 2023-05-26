from django import forms
from django.db import models
from phone.models import Product


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField()


class ProductCreateReview(forms.Form):
    comment = forms.CharField(max_length=100)
