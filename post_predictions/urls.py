from django.conf.urls import url
from . import views

app_name = 'picks'

urlpatterns = [
    url(r"create/$", views.CreatePick.as_view(), name="create"),
    url(r"pick_list/$", views.PickListView.as_view(), name='pick_list'),
    url(r'^update/(?P<pk>\d+)/$', views.UpdatePickView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeletePickView.as_view(), name='delete'),
    url(r"user_pick_list/(?P<username>[-\w]+)/$", views.UserPicksView.as_view(), name='pick_list_filter'),
    url(r"of/(?P<category>[-\w]+)/$", views.CategoryPicks.as_view(), name="category_list"),
]
