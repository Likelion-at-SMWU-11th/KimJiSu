from django.contrib import admin
from django.urls import path, include

from posts.views import url_view, url_parameter_view, function_view, index
from posts.views import class_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', url_view),
    path('url/<int:username>/', url_parameter_view),
    path('fbv/', function_view),
    path('cbv/', class_view.as_view()),

    path('', index, name='index'),
    path('posts/', include('posts.urls', namespace='posts')),
]