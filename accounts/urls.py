from django.urls import path
from .views import registration_page, login_page, logout_page

app_name = 'accounts'
urlpatterns = [
    path('register/', registration_page, name = 'register'),
    path('login/', login_page, name = 'login'),
    path('logout/', logout_page, name = 'logout')
]
