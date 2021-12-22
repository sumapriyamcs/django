from app.form import EmpForm
from django.shortcuts import render
# Create your views here.
#from django.shortcuts import render

def index(request):
    stu = EmpForm()
    return render(request, "index.html", {'form': stu})