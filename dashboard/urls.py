from django.urls import path
from dashboard import views


urlpatterns = [
   
    path("dashboard/",views.dashboardView.as_view(),name="dashboard"),
   
    
    path("tag-list/",views.TaglistView.as_view(),name="tag-list"),
    path("tag-delete/<int:pk>/",views.TagDeleteView.as_view(),name="tag-delete"),
    path("tag-update/<int:pk>",views.TagUpdateView.as_view(),name="tag-update"),
    path("tag-create/",views.TagCreateView.as_view(),name="tag-create"),
   
    path("category-list/",views.CategorylistView.as_view(),name="category-list"),
    path("category-delete/<int:pk>/",views.CategoryDeleteView.as_view(),name="category-delete"),
    path("category-update/<int:pk>",views.CategoryUpdateView.as_view(),name="category-update"),
    path("category-create/",views.CategoryCreateView.as_view(),name="category-create"),
    
    path("post-list-view/",views.PostlistView.as_view(),name="post-list-view"),
    path("post-create/",views.PostCreateView.as_view(),name="post-create"),
    path("post-delete/<int:pk>/",views.PostDeleteView.as_view(),name="post-delete"),
    path("post-update/<int:pk>/",views.PostUpdateView.as_view(),name="post-update"),
    path("dash-post-detail/<int:pk>/",views.PostDetailView.as_view(),name="dash-post-detail"),
   
    path("draft-list-view/",views.DraftListView.as_view(),name="draft-list-view"),
    path("draft-publish-view/<int:pk>",views.DraftPublishView.as_view(),name="draft-publish-view"),
    path("post-publish-view/<int:pk>",views.PostPublishView.as_view(),name="post-publish-view"),
    path("draft-delete-view/<int:pk>",views.DraftDeleteView.as_view(),name="draft-delete-view"),
    path("draft-detail-view/<int:pk>",views.DraftDetailView.as_view(),name="draft-detail-view"),
    path("draft-update-view/<int:pk>",views.DraftUpdateView.as_view(),name="draft-update-view"),
    
    path("inactive-post-view/",views.InactivePostListView.as_view(),name="inactive-post-view"),
    path("make-active-view/<int:pk>/",views.MakeActiveView.as_view(),name="make-active-view"),
    path("de-active-view/<int:pk>/",views.DeActiveView.as_view(),name="de-active-view"),


    
]