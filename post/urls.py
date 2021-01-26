from django.urls import path
from .views import *

urlpatterns = [
    path('', PostView.as_view(), name='index'),
    path('add-us/', PostCreateView.as_view(), name='add-us'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('draft/', PostDraftView.as_view(), name='draft'),
    path('search/', SearchView.as_view(), name="search"),
    path('register/', RegisterView.as_view(), name='register'),
    path('user_detal/<int:pk>', UserDetailView.as_view(), name='user_detail')
]
