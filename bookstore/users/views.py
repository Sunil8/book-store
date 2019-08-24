from django.template.loader import render_to_string
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from .forms import SignUpForm, UserLoginForm
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import (authenticate, get_user_model)
from users.tokens import account_activation_token
User = get_user_model()

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.set_password(form.cleaned_data.get('password1'))
            # user.save(commit = True)

            current_site = get_current_site(request)
            subject = "Activate your OpenPustakalay Account"
            
            message = render_to_string(
                'account_activation.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                }
            )

            user.send_email(subject, message)
            return redirect('account_activation_sent')
    else :
        form = SignUpForm()

    context = {
        "form":form,
    }
    return render(request, "users/signup.html", context = context)

def login_view(request):
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username = username, password = password)
            next = request.GET.get('next')
            if next:
                return redirect(next)
    else:
        form = UserLoginForm()

    return render(request, "users/login.html", context = {'form':form})


 