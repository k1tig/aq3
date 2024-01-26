
from django.urls import path
from scape.views import ScapeView, ScapeDetailView, profile_view, AddScapeView


urlpatterns = [
    path("", ScapeView.as_view(), name="scape"),
    path('scape/<int:pk>', ScapeDetailView.as_view(), name='scape-detail'),
    path('scape/add', AddScapeView.as_view(), name = 'add-scape'),
    path('profile/<int:pk>', profile_view, name='profile-detail'),

    

]