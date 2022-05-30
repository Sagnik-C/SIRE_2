from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('summarizer', views.summarizer, name='summarizer'),
    path('uploads', views.uploads, name='uploads'),
    path('inspection', views.inspection, name='inspection'),
    path('signup', views.signuptemp, name='signup'),
    path('handlesignup', views.handlesignup, name='handlesignup'),
    path('handlelogin', views.handlelogin, name='handlelogin'),
    path('home', views.home, name='home'),
    path('handlelogout', views.handlelogout, name='handlelogout'),
    path('ret404', views.ret404, name='ret404'),
]