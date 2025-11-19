from django.shortcuts import render,redirect
from django.views import View
from users.forms import Signupform,Loginform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# def register(request):
#     return render(request,'register.html')
#
# def login(request):
#     return render(request,'login.html')
class Register(View):
        def get(self, request):
            form_instance = Signupform()
            context = {'form': form_instance}
            return render(request, 'register.html', context)

        def post(self, request):
            form_instance = Signupform(request.POST)
            if form_instance.is_valid():
                form_instance.save()
                return redirect('users:login')

class Userlogin(View):
        def get(self, request):
            form_instance = Loginform()
            context = {'form': form_instance}
            return render(request, 'login.html', context)

        def post(self, request):
            form_instance = Loginform(request.POST)
            if form_instance.is_valid():
                data = form_instance.cleaned_data
                u = data['username']
                p = data['password']
                user = authenticate(username=u, password=p)

                if user:
                    login(request, user)
                    return redirect('books:home')
                else:
                    messages.error(request, "invalid user credentials")
                    return redirect('users:login')

class Userlogout(View):
      def get(self,request):
          logout(request)
          return redirect('users:login')
