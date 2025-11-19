from django.shortcuts import render

#
def home(request):
    return render(request,'home.html')


def addition(request):
    if(request.method=="GET"):
        return render(request,'addition.html')

    if(request.method=="POST"):
        print(request.POST)
        n1=request.POST['num1']
        n2=request.POST['num2']
        s=int(n1)+int(n2)
        print(s)

        context={'result':s, 'num1':n1 , 'num2':n2}

        return render(request,'addition.html',context)


def factorial(request):
    if (request.method == "GET"):
        return render(request, 'factorial.html')


    if (request.method == "POST"):

        f1=int(request.POST["fact1"])

        fact=1

        for i in range(1,f1 + 1):
            fact *= i
            print(fact)

        context = {'result':fact, 'fact1':f1 }

        return render(request, 'factorial.html', context)


def bmi(request):
    if (request.method == "GET"):
        return render(request, 'bmi.html')

    if(request.method=="POST"):
        b1=int(request.POST['w1'])
        b2=int(request.POST['h1'])/100
        bmi=b1/(b2**2)


        context={'result':bmi, 'w1':b1 , 'h1':b2}

        return render(request,'bmi.html',context)
