from django.urls import path
from posts import views
from django.views.decorators.cache import cache_page


app_name = "posts"

urlpatterns = [
    path("", cache_page(60 * 1)(views.PostsView.as_view()), name="posts"),
    path("create/", views.PostCreate.as_view(), name="create_post"),
    path("update/<slug:slug>/", views.PostUpdate.as_view(), name="update_post"),
    path("delete/<slug:slug>/", views.PostDelete.as_view(), name="delete_post"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
