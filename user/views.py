from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login , logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages 
# Create your views here.
a =  {'login':False}

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  # Redirect to the login page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def log_in(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        password = req.POST.get('Password')
        # print(password)
        try:
            user = User.objects.get(username=name)
            print(user)
        except:
            return HttpResponse('user not found ')
        user = authenticate(req,username = name , password = password)
        # print(user)
        if user is not None:
            login(req,user)
            print('login successful')
            a['login']=True
            return redirect('home')
    return render(req,'login.html',)

def log_out(req):
       user=req.user
       if req.method == 'POST':
            logout(req)
            return redirect('login')
       return render(req,'logout.html',{'user':user})