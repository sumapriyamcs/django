"""project24 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import function_view,NewView
from app.views import EmployeeCreate
from app.views import EmployeeCreate, EmployeeRetrieve
from app.views import EmployeeCreate, EmployeeDetail, EmployeeRetrieve
from app.views import EmployeeCreate, EmployeeDetail, EmployeeRetrieve, EmployeeUpdate, EmployeeDelete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', NewView.as_view()),
    path('', EmployeeCreate.as_view(), name='EmployeeCreate'),
    path('retrieve/', EmployeeRetrieve.as_view(), name='EmployeeRetrieve'),
    path('retrieve/<int:pk>', EmployeeDetail.as_view(), name='EmployeeDetail'),
    path('<int:pk>/update/', EmployeeUpdate.as_view(), name='EmployeeUpdate'),
    path('<int:pk>/delete/', EmployeeDelete.as_view(), name='EmployeeDelete'),
]



