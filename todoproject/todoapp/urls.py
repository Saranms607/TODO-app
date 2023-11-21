from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    # path('details/',views.details,name='details'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.TaskListview.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/',views.TaskDetailview.as_view(),name='cdvdetails'),
    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout/',views.logout,name='logout'),


]
