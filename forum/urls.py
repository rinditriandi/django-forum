from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import signup
from boards.views import home, board_topics, new_topic

urlpatterns = [
    path('', home, name='home' ),
    path('signup/', signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('boards/<int:pk>/', board_topics, name='board_topics'),
    path('boards/<int:pk>/new/', new_topic, name='new_topic'),
    path('admin/', admin.site.urls),
]
