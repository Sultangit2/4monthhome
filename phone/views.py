from django.shortcuts import render, redirect
import datetime
from phone.models import Product

from phone.forms import ProductCreateForm


def main_page_view(request):
    if request.method == 'GET':
        return render(request,'layouts/index.html')


def phone_view(request):
    if request.method == 'GET':
        phones = Product.objects.all()
        context = {
            'phones': phones,
        }
        return render(request, 'phones/phones.html', context=context)


def phone_detail_view(request, id):
    if request.method == 'GET':
        phone = Product.objects.get(id=id)

        context = {
            'phone': phone,
            'comments': phone.comment_set.all()
        }

        return render(request, 'phones/detail.html', context=context)


def product_create_view(request):
    if request.method == 'GET':
        context = {
            'form' : ProductCreateForm
        }

        return render(request, 'phones/create.html')
    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
            )
            return redirect('/phone/')
        return render(request,'phones/create.html',context={
            'form': form
        })

def product_create_feedback(request):
    if request.method == 'GET':
        context = {
            'form' : ProductCreateForm
        }
        return render(request,'phones/feedback.html')
    if request.method == 'POST':
        data,files = request.POST,request.FILES
        form = ProductCreateForm(data,files)

        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                comment = form.cleaned_data.get('commment'),
            )
            return redirect('/phone/')
        return render(request,'phones/create.html',context={
            'form': form
        })
