from django.shortcuts import render
from .models import Employee


# Create your views here.
def empdata(request):
    emp_list = Employee.objects.all()
    my_dict = {'emp_list': emp_list}
    return render(request, 'modelapp/emp.html', context=my_dict)
