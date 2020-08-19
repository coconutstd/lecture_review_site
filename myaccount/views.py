from django.shortcuts import render
from .forms import SignupForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request, 'myaccount/login.html')
    else:
        form = SignupForm()

    return render(request, 'myaccount/signup.html', {'form': form})