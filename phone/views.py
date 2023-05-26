from django.shortcuts import render, redirect
import datetime
from phone.models import Product, Comment

from phone.forms import ProductCreateForm , ProductCreateReview


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
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': ProductCreateReview
        }

        return render(request, 'phones/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        data = request.POST
        form = ProductCreateReview(data=data)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                product=product

            )

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': form
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
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        data = request.POST
        form = ProductCreateReview(data=data)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text')
                )

            context = {
                'product': product,
                'comments': product.comment_set.all(),
                'form': form
            }

            return render(request, 'phones/detail.html', context=context)


