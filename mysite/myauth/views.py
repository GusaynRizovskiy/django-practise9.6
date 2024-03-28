from django.contrib.auth import login, authenticate, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LogoutView
# Create your views here.

# def login_view(request:HttpRequest):
#     if request.method=="GET":
#         if request.user.is_authenticated:
#             return redirect("/admin/")
#         return render(request,"myauth/login-myauth.html")
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(request,username=username,password=password)
#     if user is not None:
#         login(request,user)
#         return redirect("/admin/")
#     return redirect(request,"myauth/login-myauth.html")
# def (request:HttpRequest):
#     logout(request)
#     return redirect(reverse("myauth:logout_view"))
class MylogoutView(LogoutView):
    next_page = reverse_lazy("myauth:logout_view")

def set_cookie(request:HttpRequest):
    response = HttpResponse("Set-Cookiee")
    response.set_cookie("fizz","buzz",max_age=3600)
    return response
def get_cookie(request:HttpResponse):
    values = request.COOKIES.get("fizz","default value")
    return HttpResponse(f"Cookie value: {values}")

def set_session(request:HttpRequest):
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set")
def get_session(request:HttpRequest):
    value = request.session.get("foobar", "default value")
    return HttpResponse(f"Cookie get: {value}")