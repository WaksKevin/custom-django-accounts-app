from django.urls import path
from . import views

urlpatterns = [
    path("create_user/", views.CreateUser.as_view(), name="create_user"),
    path("update_user/<int:pk>", views.UpdateUser.as_view(), name="update_user"),
    path("delete_user/<int:pk>", views.DeleteUser.as_view(), name="delete_user"),
    path("user_list/", views.UserList.as_view(), name="user_list"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
]
