from django.urls import path, re_path
from users import views
from django.views.generic.base import TemplateView

app_name = "accounts"

urlpatterns = [
    path("login/",  views.login_view, name = "login"),
    path("signup/", views.signup, name = "signup"),
    
    path(
        "signup/thankyou/", 
        TemplateView.as_view(template_name = "users/activation_sent.html"),
        name = "account_activation_sent"
    ),

    # re_path("activate/<uidb64/<token>", )
    # url(r'^activate_account/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0
]