
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('submit_exam/', views.submit_exam, name='submit_exam'),
    path('exam_result/', views.exam_result, name='exam_result'),
    path('course_details/', views.course_details, name='course_details'),
    path('mock_exam/', views.mock_exam, name='mock_exam'),
]