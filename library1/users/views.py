from django.shortcuts import render
from django.views import View
# from users.forms import Registerform,Loginform

# def register(request):
#     return render(request,'register.html')
#
# def login(request):
#     return render(request,'login.html')
class Register(View):
    def get(self, request):
        return render(request, 'register.html')

class Login(View):
    def get(self, request):
        return render(request, 'login.html')