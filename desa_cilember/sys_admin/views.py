from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from sys_admin.models import *
from sys_admin.forms import *

# Create your views here.

#Halaman Utama
def dashboard(request):
    berita = Berita.objects.all()
    galeri = Galeri.objects.all()
    context = {
        'berita':berita,
        'galeri':galeri
    }
    return render(request, 'sys_admin/dashboard.html', context)

def profil_desa(request):
    post_list = ProfilDesa.objects.all()
    context = {
        'post_list':post_list
    }
    return render(request, 'sys_admin/profil_desa.html', context)

def profil_aparatur(request):
    post_list = Aparatur.objects.all()
    context = {
        'post_list':post_list
    }
    return render(request, 'sys_admin/profil_aparatur.html', context)
    
def data_penduduk(request):
    post_list = Penduduk.objects.all()
    query = request.GET.get('q')
    if query:
        post_list = Penduduk.objects.filter(
            Q(nama__icontains=query)| 
            Q(nik__icontains=query)|
            Q(alamat__icontains=query)|
            Q(rtrw__icontains=query)
        ).distinct()
    context = {
        'post_list':post_list
    }
    return render(request, 'sys_admin/data_penduduk.html', context)

def data_pelayanan(request):
    post_list = Pelayanan.objects.all()
    context = {
        'post_list':post_list
    }
    return render(request, 'sys_admin/data_pelayanan.html', context)

def data_berita(request):
    post_list = Berita.objects.all()
    query = request.GET.get('q')
    if query:
        post_list = Berita.objects.filter(
            Q(judul__icontains=query)| 
            Q(uraian__icontains=query)
        ).distinct()
    context = {
        'post_list':post_list
    }
    return render(request, 'sys_admin/data_berita.html', context)

def data_galeri(request):
    post_list = Galeri.objects.all()
    query = request.GET.get('q')
    if query:
        post_list = Galeri.objects.filter(
            Q(judul__icontains=query)
        ).distinct()
    context = {
        'post_list':post_list
    }
    return render(request, 'sys_admin/data_galeri.html', context)


#Halaman Lain
def add_aparatur(request):
    if request.method == 'POST':
        form = AparaturCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('profil_aparatur')
    else:
        form = AparaturCreateForm()
    context = {
        'form':form
    }
    return render(request, 'otherpage/add_aparatur.html', context)

def edit_aparatur(request, slug):
    post = get_object_or_404(Aparatur, slug=slug)
    if request.method == 'POST':
        form = AparaturEditForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profil_aparatur')
    else:
        form = AparaturEditForm(instance=post)
    context = {
        'form':form,
    }
    return render(request, 'otherpage/edit_aparatur.html', context)

def del_aparatur(request, slug):
    item = get_object_or_404(Aparatur, slug=slug)
    if request.method == 'POST':
        item.delete()
        return redirect('profil_aparatur')
    context = {
        'item':item
    }
    return render(request, 'otherpage/del_aparatur.html', context)

def add_berita(request):
    if request.method == 'POST':
        form = BeritaCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('data_berita')
    else:
        form = BeritaCreateForm()
    context = {
        'form':form
    }
    return render(request, 'otherpage/add_berita.html', context)

def detail_berita(request, slug):
    post = get_object_or_404(Berita, slug=slug)
    context = {
        'post':post
    }
    return render(request, 'otherpage/detail_berita.html', context)

def edit_berita(request, slug):
    post = get_object_or_404(Berita, slug=slug)
    if request.method == 'POST':
        form = BeritaEditForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('data_berita')
    else:
        form = BeritaEditForm(instance=post)
    context = {
        'form':form,
    }
    return render(request, 'otherpage/edit_berita.html', context)

def del_berita(request, slug):
    item = get_object_or_404(Berita, slug=slug)
    if request.method == 'POST':
        item.delete()
        return redirect('data_berita')
    context = {
        'item':item
    }
    return render(request, 'otherpage/del_berita.html', context)

def add_galeri(request):
    if request.method == 'POST':
        form = GaleriCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('data_galeri')
    else:
        form = GaleriCreateForm()
    context = {
        'form':form
    }
    return render(request, 'otherpage/add_galeri.html', context)

def detail_galeri(request, slug):
    post = get_object_or_404(Galeri, slug=slug)
    context = {
        'post':post
    }
    return render(request, 'otherpage/detail_galeri.html', context)

def edit_galeri(request, slug):
    post = get_object_or_404(Galeri, slug=slug)
    if request.method == 'POST':
        form = GaleriEditForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('data_galeri')
    else:
        form = GaleriEditForm(instance=post)
    context = {
        'form':form,
    }
    return render(request, 'otherpage/edit_galeri.html', context)

def del_galeri(request, slug):
    item = get_object_or_404(Galeri, slug=slug)
    if request.method == 'POST':
        item.delete()
        return redirect('data_galeri')
    context = {
        'item':item
    }
    return render(request, 'otherpage/del_galeri.html', context)

def add_penduduk(request):
    if request.method == 'POST':
        form = PendudukCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('data_penduduk')
    else:
        form = PendudukCreateForm()
    context = {
        'form':form
    }
    return render(request, 'otherpage/add_penduduk.html', context)

def detail_penduduk(request, slug):
    post = get_object_or_404(Penduduk, slug=slug)
    context = {
        'post':post
    }
    return render(request, 'otherpage/detail_penduduk.html', context)

def edit_penduduk(request, slug):
    post = get_object_or_404(Penduduk, slug=slug)
    if request.method == 'POST':
        form = PendudukEditForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('data_penduduk')
    else:
        form = PendudukEditForm(instance=post)
    context = {
        'form':form,
    }
    return render(request, 'otherpage/edit_penduduk.html', context)

def del_penduduk(request, slug):
    item = get_object_or_404(Penduduk, slug=slug)
    if request.method == 'POST':
        item.delete()
        return redirect('data_penduduk')
    context = {
        'item':item
    }
    return render(request, 'otherpage/del_penduduk.html', context)

def edit_profil(request, kades):
    post = get_object_or_404(ProfilDesa, kades=kades)
    if request.method == 'POST':
        form = ProfilEditForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profil_desa')
    else:
        form = ProfilEditForm(instance=post)
    context = {
        'form':form,
    }
    return render(request, 'otherpage/edit_profil.html', context)