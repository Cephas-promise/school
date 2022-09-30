from django.shortcuts import redirect, render
from.forms import profileupdateform, registerform, userupdateform
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render (request, ('index.html'))

def reg (request):
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=registerform()
    return render (request,('reg.html'),{'form':form})

def login(request):
    return render(request, ('login.html'))


def studentprofile(request):
    return render(request, ('studentprofile.html'))

def result(request):
    return render(request, ('result.html'))



@login_required
def updateprofile(request):
    if request.method=='POST':
        s_form=userupdateform(request.POST, instance=request.user)
        p_form=profileupdateform(request.POST, request.FILES, instance=request.user.profile)
        if s_form.is_valid() and p_form.is_valid():
            s_form.save()
            p_form.save()
            return redirect('studentprofile')
    else:
        u_form=userupdateform(instance=request.user)
        p_form=profileupdateform(instance=request.user.profile)

    context={
        's_form':u_form,
        'p_form':p_form
    }

    return render (request, ('updateprofile.html'), context)

       
          
