from django.urls import path
from . import views
app_name = "user"
urlpatterns = [
    path('regestration/', views.UserRegestrationView.as_view(), name="regestration"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
