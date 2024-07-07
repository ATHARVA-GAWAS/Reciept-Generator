from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('receipts/', views.manage_receipts, name='manage_receipts'),
    path('receipts/delete/<int:receipt_id>/', views.delete_receipt, name='delete_receipt'),
    path('generate_bill/', views.generate_bill, name='generate_bill'),
    path('add_receipt/',views.add_receipt,name='add_receipt'),
    path('accounts/', include('django.contrib.auth.urls')),
]
