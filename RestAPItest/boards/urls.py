from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('boards',views.BoardViewSet,basename='boards')
app_name = 'boards'

urlpatterns = [
 
]
urlpatterns = urlpatterns + router.urls

'''
urlpatterns = [
      
    path('',views.BoardsList.as_view(),name='home'),
    path('board_details/<int:id>/',views.BoardDetails.as_view(),name='board_details'),
    path('boards/<int:board_id>/',views.BoardTopics.as_view(),name='board_topics'),
    
]
'''