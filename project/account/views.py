from django.shortcuts import render, redirect
from .forms import CustomSigninForm

def custom_signin_view(request):
    if request.method == 'POST':
        form = CustomSigninForm(request.POST)
        if form.is_valid():
            
            return redirect('/appoint/board')  
        else:
            return render(request, 'account/login.html', {'form': form})
    else:
        form = CustomSigninForm()
    return render(request, 'account/login.html', {'form': form})




