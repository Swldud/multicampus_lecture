from django.urls import path
from . import views

urlpatterns = [
    # qna/create/
    path('create/', views.create, name = 'create'),
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('<int:question_id>/update/', views.update, name = 'update'),
    path('<int:question_id>/delete/', views.delete, name = 'delete'),

]
