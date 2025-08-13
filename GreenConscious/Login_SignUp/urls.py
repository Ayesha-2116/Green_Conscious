from django.urls import path
from . import views

app_name = 'Login_SignUp'

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('login/', views.loginPage,  name='loginPage'),
    path('logout/', views.logoutPage, name='logoutPage'),
    path('signup/', views.signupPage, name='signupPage'),
    path('profile/', views.profile, name='profile_view'),
    path('change_password/', views.change_password, name='change_password'),
    path('passwordchangesuccess/',views.password_change_success,name='password_change_success'),
    path('passwordreset', views.password_reset, name='passwordreset'),
    path('passwordreset_next/<int:user_id>', views.password_reset_next, name='passwordresetnext'),
    path('add_security_questions/<int:user_id>', views.add_security_questions, name='add_security_questions'),
]
