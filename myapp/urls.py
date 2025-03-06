from django.urls import path
from myapp import views
from myapp.views import index

urlpatterns = [
path('',views.index, name='my_home'),



]
