from django import forms
from app.models import Student
class EmpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"