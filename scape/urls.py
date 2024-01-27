
from django.urls import path
from scape.views import ScapeView, ScapeDetailView, profile_view, ScapeCreate, ScapeEdit, HomePageView, CustomLoginView, ScapeDelete
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name = 'logout'),
    path('scape/', ScapeView.as_view(), name="scape"),
    path('scape/<int:pk>/', ScapeDetailView.as_view(), name='scape-detail'),
    path('scape-add/', ScapeCreate.as_view(), name = 'scape-add'),
    path('scape-edit/<int:pk>/', ScapeEdit.as_view(), name = 'scape-edit'),
    path('scape-delete/<int:pk>/', ScapeDelete.as_view(), name = 'scape-delete'),

    path('profile/<int:pk>', profile_view, name='profile-detail'),

]