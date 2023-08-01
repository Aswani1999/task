from . import views
from django.urls import path

urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name="register"),
    path('logout',views.logout,name='logout'),
    path('newpage',views.newpage,name='newpage'),
    path('appform',views.appform,name='appform'),
    path('submit',views.submit,name='submit'),
    # path('success_page',views.success_page_view,name='success_page'),

    # path('logout',views.logout,name='logout'),
    ]