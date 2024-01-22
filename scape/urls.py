
from django.urls import path
from scape.views import ScapeView, ScapeDetailView, profile_view


urlpatterns = [
    path("", ScapeView.as_view(), name="scape"),
    path('scape/<int:pk>', ScapeDetailView.as_view(), name='scape-detail'),
    path('profile/<int:pk>', profile_view, name='profile-detail')
    

]