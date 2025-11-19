from django.shortcuts import render
from  django.views import View
from employees.forms import Employeeform
from employees.models import Employee_records


class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Employeeview(View):
    def get(self,request):
        form_instance=Employeeform()
        context = {'form': form_instance}
        return render(request, 'employee.html', context)

    def post(self,request):
        form_instance = Employeeform(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return render(request, 'employee.html')