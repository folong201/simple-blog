from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render (request,"index.html")

def updatearticle(request):
    return render (request,"updatearticle.html")

def createarticle(request):
    return render (request,"createarticle.html")

def articledetail(request):
    return render (request,"articledetail.html")


def allarticle(request):
    return render (request,"allarticle.html")

def userdashboard(request):
    return render (request,"userdashboard.html")

def admindashboard(request):
    return render (request,"admindashboard.html")

def login(request):
    return render (request,"auth/login.html")

def register(request):
    return render (request,"auth/register.html")

def createcomment(request):
    return redirect('articledetail')