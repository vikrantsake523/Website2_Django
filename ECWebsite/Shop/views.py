from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Shop HomePage")
    return render(request,"shop/index.html")