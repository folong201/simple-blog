from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name="index"),
   path('auth/login',views.login,name="login"),
   path('userdashboard/',views.userdashboard,name="userdashboard"),
   path('auth/register',views.register,name="register"),
   path('admindashboard',views.admindashboard,name="admindashboard"),
   path('allarticle',views.allarticle,name="allarticle"),
   path('articledetail',views.articledetail,name="articledetail"),
   path('createarticle',views.createarticle,name="createarticle"),
   path('updatearticle',views.updatearticle,name="updatearticle"),
   path('createcomment',views.createcomment,name="createcomment"),
    

]