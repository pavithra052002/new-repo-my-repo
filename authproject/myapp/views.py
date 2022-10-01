from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from myapp.forms import signUpform
from django.http import HttpResponseRedirect
def home_view(request):
    return render(request,'myapp/home.html')

@login_required
def java_view(request):
    return render(request,'myapp/javaexams.html')


@login_required
def python_view(request):
    return render(request,'myapp/pythonexams.html')

@login_required
def aptitude_view(request):
    return render(request,'myapp/aptitudeexams.html')


def logout_view(request):
    return render(request,'myapp/logout.html')

def singup_view(request):
    form=singUpForm()
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect("/accounts/login")
            d={'form':form}
            return render(request,'myapp/singup.html',d)