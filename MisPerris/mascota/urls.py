from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'mascota'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    url(r'^guardar_mascota/$', views.crud.guardarMascota, name='guardar_mascota'),
    url(r'^actualizar_mascota/$', views.crud.actualizarMascota, name='actualizar_mascota'),
    url(r'^([0-9]+)/editar_mascota/$', views.crud.editarMascota, name='editar_mascota'),
    url(r'^([0-9]+)/eliminar_mascota/$', views.crud.eliminarMascota, name='eliminar_mascota'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
