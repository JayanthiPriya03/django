from .views import*
from django.urls import path

urlpatterns=[
    path('add/',Sview.as_view()),
    path('get/',Getview.as_view()),
    path('del/<int:id>',Deleteview.as_view()),
]

