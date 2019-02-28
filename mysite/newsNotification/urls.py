from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
    path('newkeyword/', views.enterKeyword, name='enterkeyword'),
    path('removekeyword/', views.removeKeyword, name='removekeyword')
]