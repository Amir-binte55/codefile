
from django.urls import path
from.views import *
urlpatterns = [
    path('', home, name='home'),
    path('base/', base, name='base'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', registration, name='registration'),
    path('Profile/', Profile, name='profile'),

    # path('', include('app.urls')),

]