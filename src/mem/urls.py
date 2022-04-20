from django.urls import path, include

from mem.views import RegisterView, AddMemView, YourMemView, DeleteMemView, EditMemView, UserFollowingView, \
    UserFollowersView, FollowToggleUserView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('add_mem/', AddMemView.as_view(), name='addmem'),
    path('<str:author>/', YourMemView.as_view(), name='yourmemes'),
    path('delete_mem/<int:mem_id>/', DeleteMemView.as_view(), name='deletemem'),
    path('edit_mem/<int:mem_id>/', EditMemView.as_view(), name='editmem'),
    path('<str:author>/following/', UserFollowingView.as_view(), name='user_following_list'),
    path('<str:author>/followers/', UserFollowersView.as_view(), name='user_followers_list'),
    path('<str:author>/follow_unfollow/', FollowToggleUserView.as_view(), name='user_follow_unfollow'),
]
