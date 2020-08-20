from django.shortcuts import render, redirect
from .forms import SignupForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            print('성공')
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'myaccount/signup.html', {'form': form})