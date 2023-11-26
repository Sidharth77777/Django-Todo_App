from django.shortcuts import render,reverse
from django.contrib.auth import authenticate,login as user_login,logout as user_logout
from users.forms import CustomUserCreationForm
from django.http.response import HttpResponseRedirect
from users.models import CustomUser
from django.http.response import HttpResponse

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email and password:
            user  = authenticate(request,email=email, password=password)
            if user is not None:
                user_login(request,user)
                
                return HttpResponseRedirect("/")
                
        context = {
            'error' : True,
            'message' : 'Invalid email address and password',
        }
        return render (request, 'login.html',context=context)
    
    else:        
        context = {
            
        }
        return render (request, 'login.html',context=context)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            
            CustomUser.objects.create_user(
                email = instance.email,
                full_name = instance.full_name,
                user_class = instance.user_class,
                user_division = instance.user_division, 
                password = instance.password,  
            )
            
            user = authenticate(request, email=instance.email, password=instance.password)
            user_login(request,user)
            
            return HttpResponseRedirect('/')
    else:
        message = 'Check again if you are already signed up'
        form = CustomUserCreationForm()
        context = {
            'form': form,
            'error' : True,
            'message' : message,   
        }
    return render(request, 'signup.html', context=context)


def logout(request):
    user_logout(request)
    return HttpResponseRedirect(reverse('todo:index'))