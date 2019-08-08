from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def index(request):
    #get data from infobook
    res=models.InfoBook.objects.all()
    print(res)
    context={
        'books':res#getdata
    }
    return render(request,'book/index.html',context=context)
def book_detail(request,book_id):
    return HttpResponse("这里显示{}图书的详细信息".format(book_id))