from django.urls import path
from exercises import views

app_name = 'exercises'

urlpatterns = [
    path('', views.bank, name='bank'),
    path('add/', views.bank_add, name='bank_add'),
    path('edit/<int:bank_pk>/', views.bank_edit, name='bank_edit'),
]