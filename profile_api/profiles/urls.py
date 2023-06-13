from django.urls import path
from .views import profile_create_or_update

urlpatterns = [
    path('', profile_create_or_update, name='profile_create'),
    path('<int:profile_id>/', profile_create_or_update, name='profile_update'),
]
