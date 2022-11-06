from checkup.models import Patient
from django.shortcuts import render,redirect
from Users.user_registration import NewUserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm 

from django.contrib import messages


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			# messages.success(request, "Registration successful." )
			return redirect("home_page")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	
	form = NewUserForm()
	return render (request=request, template_name="Users/register_user.html", context={"form":form})

def login_request(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)           
          return redirect('home_page')



		#    messages.success(("There was an error loging you in,Try again"))
        
         
    else:
           return render(request,"Users/loging_in.html",{
            
            
        })
      
# def login_request(request):
# 	if request.method == "POST":
# 		username = request.POST['username']
# 		password=request.POST["password"]
# 		user = authenticate(username=username, password=password)
#         if user is not None:
# 		    login(request,user)
		      

# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			# user.save()
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			login(request, user)
# 			messages.info(request, f"You are now logged in as {username}.")
# 			return redirect("home_page")
# 				# return username
			
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="Users/loging_in.html", context={"login_form":form})

# @login()
# def profile(request):
#     return render (request,"Users/profile.html",{"users":user})


