
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tratores/', include('trator.urls')),
    path('', include('usuario.urls')),
    path('dispositivos/', include('dispositivo.urls')),
    path('trabalhos/', include('trabalho.urls')),
    path('areas/', include('area.urls')),
    path('imagens/', include('imagem.urls')),
    path('rotas/', include('rota.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
