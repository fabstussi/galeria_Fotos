from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.galeria, name='galeria'),
    path('galeria/<int:id>', views.categoria, name='categoria'),
    path('imagem/<int:id>', views.imagem, name='imagem'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)