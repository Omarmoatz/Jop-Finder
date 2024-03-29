from django.urls import path
from .views import JobList, jop_detail, ApplyForm, AddJob, debug
from .api import JobDetailtApi , JobListApi,CompanyListApi,CategoryListApi

app_name = 'job'

urlpatterns = [
    path('debug', debug),
    
    path('add', AddJob.as_view(), name='add_job'),
    path('', JobList.as_view(), name='job_list'),
    path('<slug:slug>/', jop_detail, name='job_detail'),
    path('<slug:slug>/apply/', ApplyForm.as_view(), name='apply_form'),


    #api
    path('api/', JobListApi.as_view()),
    path('api/<int:pk>', JobDetailtApi.as_view()),
    path('api/company', CompanyListApi.as_view()),
    path('api/ctg', CategoryListApi.as_view()),
]