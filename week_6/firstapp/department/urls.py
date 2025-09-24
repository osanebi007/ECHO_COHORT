from django.urls import path
from .views import get_store    
from .views import get_todos, clubNames, post_todo, update_todo, delete_todo, patch_todo
urlpatterns = [
    path('getstore/', get_store),
    path('getmessage/', get_todos),
    path('postmessage/', post_todo),
    path('clubnames/', clubNames),
    path('updatemessage/<int:index>/', update_todo),
    path('deletemessage/<int:index>/', delete_todo),
    path('patchmessage/<int:index>/', patch_todo)
]