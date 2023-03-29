from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def index(request):
    return render(request, 'registration')
def home(request):
    return render(request , 'registration/base.html')

def about(request):
    return render(request, 'registration/about.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')    # save the username
            messages.success(request, f'Account created for {username}!')    #flash message
            return redirect('regi-home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/registration.html', {'form': form})

def test(request):
    return render(request, 'registration/register2.html')