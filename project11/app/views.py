from django.http import HttpResponse
from app.functions.functions import handle_uploaded_file
from app.forms import StudentForm
from django.shortcuts import render
# Create your views here.
def index(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
        student = StudentForm()
        return render(request,"index.html",{'form':student})