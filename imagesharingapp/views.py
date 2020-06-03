from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def login_redirect(request):
    return redirect('/account/login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://localhost:3000/')
    else:
        form = UserCreationForm()
        args = {'form' : form}
        return render(request, 'accounts/reg_form.html', args)