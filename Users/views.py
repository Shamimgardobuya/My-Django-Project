from checkup.models import Patient
from django.shortcuts import render,redirect
from Users.user_registration import NewUserForm
from django.contrib.auth import authenticate,login
from django.contrib import messages



def register(response):
    if response.method =="POST":
        form_user=NewUserForm(response.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect("/home")

        else:
            # messages.success(request,"There was an error trying to log you in,please try again....")
            return redirect("loging_in")

    else:
        form_user=NewUserForm()
    # messages.error(request, "Hello,this is an invalid email,try again")
    return render(response, "Users/register_user.html", {"form":form_user})

def loging_in(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
        else:
         messages.success(("There was an error loging you in,Try again"))
         return redirect('home')
    else:
        return render(request,"Users/loging_in.html",{
            
            
        })


# @login()
# def profile(request):
#     return render (request,"Users/profile.html",{"users":user})


