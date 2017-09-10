from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$',
        views.PostListView.as_view(),
        name='post_list'),

    url(r'^about/$',
        views.AboutView.as_view(),
        name='about'),

    url(r'^post/(?P<pk>\d+)$',
        views.PostDetailView.as_view(),
        name='post_detail'),

    url(r'^post/new/$',
        views.CreatePostView.as_view(),
        name='post_new'),

    url(r'^post/update/(?P<pk>\d+)$',
        views.UpdatePostView.as_view(),
        name='post_update'),

    url(r'^post/delete/(?P<pk>\d+)$',
        views.DeletePostView.as_view(),
        name='post_delete'),

    url(r'^drafts/$',
        views.DraftListView.as_view(),
        name='drafts'),

    url(r'^post/comment/(?P<pk>\d+)$',
        views.add_comment_to_post,
        name='add_comment_to_post'),

    url(r'^comment/approve/(?P<pk>\d+)$',
        views.comment_approve,
        name='comment_approve'),

    url(r'^comment/remove/(?P<pk>\d+)$',
        views.comment_remove,
        name='comment_remove'),

    url(r'^comment/publish/(?P<pk>\d+)$',
        views.post_publish,
        name='post_publish'),

]
