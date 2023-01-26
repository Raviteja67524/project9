from django.shortcuts import render

# Create your views here.


def forloop(request):
    d={'name':'ravi','L':[11, 12, 13],}
    return render(request,'forloop.html',d)