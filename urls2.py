from django.urls import path
from .import views

urlpatterns = [
    path('about', views.index, name='index'),#yusufaliokcu.com/first_app/
    path("<int:num1>", views.course_number_view, name='course_number_view'),#yusufaliokcu.com/first_app/10
    path("<str:item>" , views.course, name='course'),#yusufaliokcu.com/first_app/python
    path("<int:num1>/<int:num2>", views.calculator, name='calculator')#yusufaliokcu.com/first_app/5/4

]
