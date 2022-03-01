from django.urls import path, include
from . import views


urlpatterns = [
    path('users_profile/<int:user_id>', views.users_profile, name='users_profile'),
    path('accounts/', include('django.contrib.auth.urls')),
]
