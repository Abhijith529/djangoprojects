from django import forms


from employees.models import Employee_records
class Employeeform(forms.ModelForm):
    class Meta:
        model=Employee_records
        fields="__all__"