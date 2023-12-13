from django.conf.urls.static import static
from django.urls import path

from inmakeproject import settings
from . import views

urlpatterns = [

    path('',views.demo,name='demo'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
