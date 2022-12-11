from django.shortcuts import render, redirect
from .forms import NewUserForm
from .forms import CustomLoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render (request, 'home.html')

def register_request(request):
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name = 'registration/signup.html', context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = CustomLoginForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = CustomLoginForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})
