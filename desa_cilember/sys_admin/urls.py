from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    #Halaman Utama
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profil_desa/', views.profil_desa, name='profil_desa'),
    path('profil_aparatur/', views.profil_aparatur, name='profil_aparatur'),
    path('data_penduduk/', views.data_penduduk, name='data_penduduk'),
    path('data_pelayanan/', views.data_pelayanan, name='data_pelayanan'),
    path('data_berita/', views.data_berita, name='data_berita'),
    path('data_galeri/', views.data_galeri, name='data_galeri'),

    #Halaman Lain
    path('add_aparatur/', views.add_aparatur, name='add_aparatur'),
    path('edit_aparatur/<str:slug>/', views.edit_aparatur, name='edit_aparatur'),
    path('del_aparatur/<str:slug>/', views.del_aparatur, name='del_aparatur'),
    path('add_berita/', views.add_berita, name='add_berita'),
    path('detail_berita/<str:slug>/', views.detail_berita, name='detail_berita'),
    path('edit_berita/<str:slug>/', views.edit_berita, name='edit_berita'),
    path('del_berita/<str:slug>/', views.del_berita, name='del_berita'),
    path('add_galeri/', views.add_galeri, name='add_galeri'),
    path('detail_galeri/<str:slug>/', views.detail_galeri, name='detail_galeri'),
    path('edit_galeri/<str:slug>/', views.edit_galeri, name='edit_galeri'),
    path('del_galeri/<str:slug>/', views.del_galeri, name='del_galeri'),
    path('add_penduduk/', views.add_penduduk, name='add_penduduk'),
    path('detail_penduduk/<str:slug>/', views.detail_penduduk, name='detail_penduduk'),
    path('edit_penduduk/<str:slug>/', views.edit_penduduk, name='edit_penduduk'),
    path('del_penduduk/<str:slug>/', views.del_penduduk, name='del_penduduk'),
    path('edit_profil/<str:kades>/', views.edit_profil, name='edit_profil'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
