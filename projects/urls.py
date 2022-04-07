from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name='projects'
urlpatterns = [
  path('', views.index, name='index'),
  path('<project_name>/', views.project, name='project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)