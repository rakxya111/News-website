from django.urls import include, path
from rest_framework import routers

from api import views

# r = raw data 
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'contacts',views.ContactViewSet)
router.register(r'newsletter',views.NewsLetterViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    path("post-by-category/<int:category_id>/", views.PostListByCategoryViewSet.as_view(), name="post-list-by-category-api"),
    path("post-by-tag/<int:tag_id>/", views.PostListByTagViewSet.as_view(), name="post-list-by-tag-api"),
    path("draft-list/", views.DraftListViewSet.as_view(), name="draft-list-api"),
    path("post-publish/", views.PostPublishViewSet.as_view(), name="post-publish-api"),
    path("post/<int:post_id>/comments/",views.CommentViewSet.as_view(),name="comment-api"),
]
