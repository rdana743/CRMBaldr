
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views

from core.views import index, about
from userprofile.views import signup,myaccount
from userprofile.forms import LoginForm

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/leads/',include('lead.urls')),
    path('dashboard/clients/', include('client.urls')),
    path('dashboard/myaccount/',myaccount,name='myaccount'),
    path('dashboard/teams/', include('team.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('about/',about, name='about'),
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html', authentication_form=LoginForm), name='login'),
    path('log-out/',views.LogoutView.as_view(),name='logout'),
    path('tasks/',include('tasks.urls')),
    path('admin/', admin.site.urls),
    
    
    
]