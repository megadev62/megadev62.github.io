from django import forms
from sys_admin.models import *

class AparaturCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = "*"
    
    nama    = forms.CharField(label="Nama Lengkap", widget=forms.TextInput(attrs={'class':'form-control'}))
    tml     = forms.CharField(label="Tempat Lahir", widget=forms.TextInput(attrs={'class':'form-control'}))
    ttl     = forms.CharField(label="Tanggal Lahir", widget=forms.DateInput(attrs={'placeholder':'YYYY/MM/DD','class':'form-control'}))
    jabatan = forms.CharField(label="Jabatan", widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Aparatur
        fields = (
            'nama', 
            'tml', 
            'ttl',
            'jabatan',
            'gambar',
        )

class AparaturEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = "*"
    
    nama    = forms.CharField(label="Nama Lengkap", widget=forms.TextInput(attrs={'class':'form-control'}))
    tml     = forms.CharField(label="Tempat Lahir", widget=forms.TextInput(attrs={'class':'form-control'}))
    ttl     = forms.CharField(label="Tanggal Lahir", widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'form-control'}))
    jabatan = forms.CharField(label="Jabatan", widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Aparatur
        fields = (
            'nama', 
            'tml', 
            'ttl',
            'jabatan',
            'gambar',
        )

class BeritaCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = "*"
    
    judul    = forms.CharField(label="Judul Berita", widget=forms.TextInput(attrs={'class':'form-control'}))
    uraian   = forms.CharField(label="Uraian Berita", widget=forms.Textarea(attrs={'class':'form-control'}))
    
    class Meta:
        model   = Berita
        fields  = '__all__'
        exclude = ('slug','created','update',)

class BeritaEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = "*"
    
    judul    = forms.CharField(label="Judul Berita", widget=forms.TextInput(attrs={'class':'form-control'}))
    uraian   = forms.CharField(label="Uraian Berita", widget=forms.Textarea(attrs={'class':'form-control'}))
    
    class Meta:
        model   = Berita
        fields  = '__all__'
        exclude = ('slug','created','update',)

class GaleriCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = "*"
    
    judul    = forms.CharField(label="Judul Galeri", widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model   = Galeri
        fields  = '__all__'
        exclude = ('slug','created','update',)

class GaleriEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = "*"
    
    judul    = forms.CharField(label="Judul Galeri", widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model   = Galeri
        fields  = '__all__'
        exclude = ('slug','created','update',)

class PendudukCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = "*"
    
    nama    = forms.CharField(label="Nama Lengkap", widget=forms.TextInput(attrs={'class':'form-control'}))
    nik     = forms.CharField(label="NIK", widget=forms.TextInput(attrs={'class':'form-control'}))
    tml     = forms.CharField(label="Tempat Lahir", widget=forms.TextInput(attrs={'class':'form-control'}))
    ttl     = forms.CharField(label="Tanggal Lahir", widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'form-control'}))
    alamat  = forms.CharField(label="Alamat", widget=forms.TextInput(attrs={'class':'form-control'}))
    rtrw    = forms.CharField(label="RT/RW", widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model   = Penduduk
        fields  = '__all__'
        exclude = ('slug','created','update',)

class PendudukEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = "*"
    
    nama    = forms.CharField(label="Nama Lengkap", widget=forms.TextInput(attrs={'class':'form-control'}))
    nik     = forms.CharField(label="NIK", widget=forms.TextInput(attrs={'class':'form-control'}))
    tml     = forms.CharField(label="Tempat Lahir", widget=forms.TextInput(attrs={'class':'form-control'}))
    ttl     = forms.CharField(label="Tanggal Lahir", widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD','class':'form-control'}))
    alamat  = forms.CharField(label="Alamat", widget=forms.TextInput(attrs={'class':'form-control'}))
    rtrw    = forms.CharField(label="RT/RW", widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model   = Penduduk
        fields  = '__all__'
        exclude = ('slug','created','update',)

class ProfilEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = "*"
    
    nama    = forms.CharField(label="Nama Desa", widget=forms.TextInput(attrs={'class':'form-control'}))
    email   = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control'}))
    tlp     = forms.CharField(label="Telepon", widget=forms.NumberInput(attrs={'class':'form-control'}))
    wa      = forms.CharField(label="WhatsApp", widget=forms.NumberInput(attrs={'class':'form-control'}))
    alamat  = forms.CharField(label="Alamat", widget=forms.TextInput(attrs={'class':'form-control'}))
    kab     = forms.CharField(label="Kota/Kabupaten", widget=forms.TextInput(attrs={'class':'form-control'}))
    prov    = forms.CharField(label="Provinsi", widget=forms.TextInput(attrs={'class':'form-control'}))
    pos     = forms.CharField(label="Kode Pos", widget=forms.NumberInput(attrs={'class':'form-control'}))
    visi    = forms.CharField(label="Visi", widget=forms.Textarea(attrs={'class':'form-control'}))
    misi    = forms.CharField(label="Misi", widget=forms.Textarea(attrs={'class':'form-control'}))
    kades    = forms.CharField(label="Sambutan Kepala Desa", widget=forms.Textarea(attrs={'class':'form-control'}))
    
    class Meta:
        model   = ProfilDesa
        fields  = '__all__'
        exclude = ('created','update',)