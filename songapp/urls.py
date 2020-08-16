from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('getBill', views.getBill, name='getBill'),
    path('reg',views.reg,name='reg'), 
    path('upload', views.create_profile, name = 'create'),
    path('login/',LoginView.as_view(),name='login'), 
    path('logout',LogoutView.as_view(next_page="/login"),name='logout'), 


]
