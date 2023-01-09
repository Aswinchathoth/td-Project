
from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('home/',views.Tasklistview.as_view(),name='home'),
    path('details/<int:pk>/',views.detaileview.as_view(),name='details'),
    path('updates/<int:pk>/',views.TaskUpdate.as_view(),name='updates'),
    path('delete/<int:pk>/', views.Deleteview.as_view(), name='delete')
]