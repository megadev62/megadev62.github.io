from django.contrib import admin
from sys_admin.models import *
# Register your models here.

class AparaturAdmin(admin.ModelAdmin):
    list_display = ('nama','jabatan','tml','ttl')
    prepopulated_fields = {'slug':('nama',)}

class PendudukAdmin(admin.ModelAdmin):
    list_display = ('nama','nik','alamat','rtrw')
    search_fields = ('nama','nik','alamat','rtrw')
    date_hierarchy = ('update')
    prepopulated_fields = {'slug':('nama',)}

class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul','created')
    search_fields = ('judul','uraian')
    date_hierarchy = ('created')
    prepopulated_fields = {'slug':('judul',)}

class GaleriAdmin(admin.ModelAdmin):
    list_display = ('judul','created')
    search_fields = ('judul','uraian')
    date_hierarchy = ('created')
    prepopulated_fields = {'slug':('judul',)}

class ProfilDesaAdmin(admin.ModelAdmin):
    list_display = ('nama','alamat','tlp','kab','prov')

admin.site.register(Aparatur, AparaturAdmin)
admin.site.register(Penduduk, PendudukAdmin)
admin.site.register(Berita, BeritaAdmin)
admin.site.register(Galeri, GaleriAdmin)
admin.site.register(ProfilDesa, ProfilDesaAdmin)
admin.site.register(JenisPel)
admin.site.register(JenisSur)
admin.site.register(Pelayanan)