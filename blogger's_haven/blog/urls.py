from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  
    path("header/", views.header, name="header"),
    path("posts/<int:post_id>/", views.post_details, name="post_details"),
    path("posts/<int:post_id>/comment/", views.add_comment, name="add_comment"),
    path("contact/", views.contact, name="contact"),
    path("post/<int:post_id>/like/", views.like_post, name="like_post"),
    path("login/", views.user_login, name="user_login"),
    path("footer/",views.foot, name="footer.html"),
    path("create/", views.create_post, name="create_post"),
    path("update/<int:post_id>/", views.update_post, name="update_post"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
]
