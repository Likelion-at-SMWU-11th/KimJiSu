from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from posts.views import url_view, url_parameter_view, function_view, index
from posts.views import class_view

urlpatterns = [
    path('', index, name='index'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('posts/', include('posts.urls', namespace='posts')),


    path('admin/', admin.site.urls),
    # Function Based View
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view),
    path('fbv/', function_view),
    # Class Based View
    path('cbv/', class_view.as_view()), # as_view: 진입 메소드
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
