from django.shortcuts import render,redirect
from . models import Article,CustomUser

# Create your views here.
def index(request):
    articles = Article.objects.all()
    
    return render (request,"index.html",{'articles':articles})

def updatearticle(request):
    return render (request,"updatearticle.html")

def createarticle(request):
    if request.method == 'POST':
        article = Article()
        print('authuser')
        print(request.user)
        author = CustomUser.objects.get(id = request.user.id)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.author = author
        article.save()
        return redirect("index")
        
        
    return render (request,"createarticle.html")

def articledetail(request):
    return render (request,"articledetail.html")


def allarticle(request):
    return render (request,"allarticle.html")

def userdashboard(request):
    return render (request,"userdashboard.html")

def admindashboard(request):
    articles = Article.objects.all()   
    return render (request,"admindashboard.html",{'articles':articles})

def login(request):
    return render (request,"auth/login.html")

def register(request):
    return render (request,"auth/register.html")

def createcomment(request):
    return redirect('articledetail')