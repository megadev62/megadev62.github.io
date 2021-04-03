from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Aparatur(models.Model):
    nama    = models.CharField(max_length=150, null=True)
    slug    = models.SlugField(max_length=150)
    tml     = models.CharField(max_length=150, null=True)
    ttl     = models.DateField()
    jabatan = models.CharField(max_length=150, null=True)
    gambar  = models.ImageField(upload_to='gambar_aparatur/', default='gambar_aparatur/default.jpg', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-update']

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nama)
        super(Aparatur, self).save(*args, **kwargs)

class Penduduk(models.Model):
    nama    = models.CharField(max_length=150, null=True)
    slug    = models.SlugField(max_length=150)
    nik     = models.CharField(max_length=150, null=True)
    tml     = models.CharField(max_length=150, null=True)
    ttl     = models.DateField()
    alamat  = models.CharField(max_length=150, null=True)
    rtrw    = models.CharField(max_length=150, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-update']

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nama)
        super(Penduduk, self).save(*args, **kwargs)

class Berita(models.Model):
    judul   = models.CharField(max_length=255, null=True)
    slug    = models.SlugField(max_length=255)
    uraian  = models.TextField()
    img1    = models.ImageField(upload_to='gambar_berita/', blank=True, null=True)
    img2    = models.ImageField(upload_to='gambar_berita/', blank=True, null=True)
    img3    = models.ImageField(upload_to='gambar_berita/', blank=True, null=True)
    img4    = models.ImageField(upload_to='gambar_berita/', blank=True, null=True)
    img5    = models.ImageField(upload_to='gambar_berita/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul)
        super(Berita, self).save(*args, **kwargs)

class Galeri(models.Model):
    judul   = models.CharField(max_length=255, null=True)
    slug    = models.SlugField(max_length=255)
    img1    = models.ImageField(upload_to='gambar_galeri/', blank=True, null=True)
    img2    = models.ImageField(upload_to='gambar_galeri/', blank=True, null=True)
    img3    = models.ImageField(upload_to='gambar_galeri/', blank=True, null=True)
    img4    = models.ImageField(upload_to='gambar_galeri/', blank=True, null=True)
    img5    = models.ImageField(upload_to='gambar_galeri/', blank=True, null=True)
    img6    = models.ImageField(upload_to='gambar_galeri/', blank=True, null=True)
    img7    = models.ImageField(upload_to='gambar_galeri/', blank=True, null=True)
    img8    = models.ImageField(upload_to='gambar_galeri/', blank=True, null=True)
    img9    = models.ImageField(upload_to='gambar_galeri/', blank=True, null=True)
    img10   = models.ImageField(upload_to='gambar_galeri/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul)
        super(Galeri, self).save(*args, **kwargs)

class ProfilDesa(models.Model):
    nama    = models.CharField(max_length=150, null=True)
    email   = models.EmailField()
    tlp     = models.CharField(max_length=13, null=True)
    wa      = models.CharField(max_length=13, null=True)
    alamat  = models.CharField(max_length=150, null=True)
    kab     = models.CharField(max_length=150, null=True)
    prov    = models.CharField(max_length=150, null=True)
    pos     = models.CharField(max_length=7, null=True)
    visi    = models.TextField()
    misi    = models.TextField()
    kades   = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

class JenisPel(models.Model):
    nama = models.CharField(max_length=30)

    class Meta:
        ordering = ['nama']

    def __str__(self):
        return self.nama

class JenisSur(models.Model):
    nama = models.CharField(max_length=100)
    jenis = models.ForeignKey(JenisPel, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nama']

    def __str__(self):
        return self.nama

class Pelayanan(models.Model):
    penduduk = models.ForeignKey(Penduduk, on_delete=models.CASCADE)
    jenis = models.ForeignKey(JenisSur, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update  = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['created']









