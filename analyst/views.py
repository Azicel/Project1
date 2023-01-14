from django.shortcuts import render

# Create your views here.

def main(requset):
    return render(requset, 'analyst/main.html')

def years(requset):
    return render(requset, 'analyst/years.html')

def cities(request):
    return render(request,'analyst/cities.html')