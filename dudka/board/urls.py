from . import views
from django.urls import path

from .views import answer

urlpatterns = [
    path('', views.board, name="board"),
    path('create', views.create, name="create"),
    path('<int:pk>', views.BoardView.as_view(), name='board_view'),
    path('<int:pk>/answer', views.answer, name='board_answer'),
    path('<int:pk>/update', views.BoardUpdate.as_view(), name='board_update'),
    path('<int:pk>/delete', views.BoardDelete.as_view(), name='board_delete')
]

