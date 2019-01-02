from django.urls import path
from manager import views

app_name = 'manager'

urlpatterns = [
    path('', views.ListManager.as_view(), name='home'),
    path('generator', views.PasswordGenerator.as_view(), name='generator'),
    path('create', views.CreateManager.as_view(), name='create'),
    path('<pk>', views.DetailManager.as_view(), name='detail'),
    path('delete/<pk>', views.DeleteManager.as_view(), name='delete'),
    path('update/<pk>', views.UpdateManager.as_view(), name='update'),


]
