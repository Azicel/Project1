from django.shortcuts import render

# Create your views here.

def main(requset):
    return render(requset, 'analyst/main.html')