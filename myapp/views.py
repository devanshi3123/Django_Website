from django.shortcuts import render
from django.http import response

# Create your views here.

def homepage(request):
	return render(request,'page.html')
def adalajvav(request):
	return render(request,'page1.html')
def sabarmatiashram(request):
	return render(request,'page2.html')
def akshardham(request):
	return render(request,'page3.html')
