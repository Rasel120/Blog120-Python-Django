from django.urls import path
from .import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contactView, name='contact'),
    path('about', views.aboutView, name='about'),
    path('search', views.searchpage, name='searchpage'),
    path('signup', views.signuppage, name='registration'), # name ta html e dorar jonno
    path('login', views.loginpage, name='login'),
    path('logout', views.authlogout, name='logsout'),
    path('forget', views.forgetpasswordpage, name='forgetpassword'),    
    path('profile', views.authprofile, name='userprofile'),
]
