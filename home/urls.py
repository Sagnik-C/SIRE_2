from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('summarizer', views.summarizer, name='summarizer'),
    path('uploads', views.uploads, name='uploads'),
    path('inspection', views.inspection, name='inspection')
]