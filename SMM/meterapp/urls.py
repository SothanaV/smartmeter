from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', views.home, name='home'),
    path('piupload/', views.pi_upload, name='pi_upload'),
    path('pressure/', views.pressure, name='pi_pressure'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)