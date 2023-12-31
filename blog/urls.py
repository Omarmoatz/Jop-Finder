from django.urls import path
from .views import BlogList,BlogDetail,add_comment
from .api import BlogListAPI,BlogDetailAPI

app_name='blog'

urlpatterns = [
    path('',BlogList.as_view(), name='blog_list'),
    path('<slug:slug>',BlogDetail.as_view(), name='blog_detail'),
    path('<slug:slug>/add-comment',add_comment, name='add_comment'),

    #__  API  __
    path('api/',BlogListAPI.as_view()),
    path('api/<int:pk>',BlogDetailAPI.as_view())
]


