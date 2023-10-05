from django.urls import path
from core.views import index,contact

from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/',views.detail,name='detail'),
]
