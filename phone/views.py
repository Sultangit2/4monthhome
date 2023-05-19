from django.shortcuts import render
import datetime
from phone.models import Product




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
