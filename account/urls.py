from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', registerPage, name="register"),
	path('login/', loginPage, name="login"),  
	path('logout/', logoutUser, name="logout"),
    path('', home, name="home"),
    

]