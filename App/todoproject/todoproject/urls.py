from django.contrib import admin
from django.urls import include, path
from todo.views import addTodo, deleteTodo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
]
