from django.urls import path
from . import views


urlpatterns=[
    
    path("",views.home,name="home"),
    path("signin/",views.signin,name="signin"),
    path("logout/",views.logoutUser,name="logout"),
    path("write",views.write,name="write"),
    path("article/<int:pk>/",views.article_view, name="article"),
    path("staff/",views.staff_views,name="staff_view"),
    path("staff/<int:pk>/",views.article_setting,name="article_setting")
]
