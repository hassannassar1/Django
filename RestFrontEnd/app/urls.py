from django.urls import path
from . import views
app_name = 'app'

urlpatterns = [
    path('',views.boards_list,name='home'),
    path('boards/<int:board_id>/',views.board_topics,name='board_topics'),
    path('boards/<int:board_id>/new/',views.new_topic,name='new_topic'),
]

