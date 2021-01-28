from django.urls import path, include
from . import views
#이미지 업로드


urlpatterns = [
    path('', views.index, name="index"),
    path('writeDiary/', views.writeDiary, name="writeDiary"),
    path('modifyDiary/', views.modifyDiary, name="modifyDiary"),
    path('deleteDiary/', views.deleteDiary, name="deleteDiary"),
    #path('deleteTodo/', views.deleteTodo, name="deleteTodo")
]
