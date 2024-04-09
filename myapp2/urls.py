from django.urls import path
from myapp2 import views
urlpatterns = [
    path('',views.home,name='my_home')

]