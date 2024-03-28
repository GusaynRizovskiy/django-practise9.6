from django.contrib.auth.views import LoginView
from .views import MylogoutView,get_cookie,set_cookie,get_session,set_session
from django.urls import path
LoginView
app_name = "myauth"
urlpatterns = [
    path("login/",LoginView.as_view(
        template_name = "myauth/login-myauth.html",
        redirect_authenticated_user = True,
    ),  name = 'login_view'),
    path("logout/",MylogoutView.as_view(),name = 'logout_view'),
    path("getcookie/",get_cookie,name='get_cookie'),
    path("setcookie/",set_cookie,name='set_cookie'),
    path("session/set",set_session,name='session_set'),
    path("session/get",get_session,name='session_get'),
    ]