from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm , UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'your account has been created! you are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()


    return render(request,'users/register.html',{'form': form})

@login_required
def profile(request):
    u_form = UserUpdateForm(instance = request.User)
    p_form = ProfileUpdateForm(instance = request.User.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form,
    }
    return render(request, 'users/profile.html', context)
