from django.shortcuts import render
from .forms import dashForm
from django.http import HttpResponse

# Create your views here.
def dash_form(request):
	form=dashForm()
	return render(request,'books/dashbord.html',{'form':form})
