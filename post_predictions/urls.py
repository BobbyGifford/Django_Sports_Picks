from django.conf.urls import url
from . import views

app_name = 'picks'

urlpatterns = [
    url(r"fullList/$", views.FullList.as_view(), name='full_list'),
    url(r"create/$", views.CreatePick.as_view(), name="create"),
    url(r"pick_list/$", views.PickListView.as_view(), name='pick_list'),
    url(r"pick_list_filter/$",views.UserPicksView.as_view(), name='pick_list_filter'),
]
