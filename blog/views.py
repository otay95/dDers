from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Haber


# Anasayfa (Tüm haberler) (READ (all))
def anasayfaG(request):
    return render(request, 'anasayfa.html',
                  {'haberler': Haber.objects.all()})


# Detay Sayfası (ID ile Süzme) (READ (single))
def detayG(request, haber_id):
    return render(request, 'detay.html',
                  {'haber': Haber.objects.get(pk=haber_id)})


# Detay Sayfası (Slug ile Süzme) (READ (single))
def detaySlugG(request, haber_slug):
    return render(request, 'detay.html',
                  {'haber': Haber.objects.get(slug=haber_slug)})


# Haber Ekleme Görünümü (CREATE)
def haberEkleG(request):
    if request.method == 'POST':
        baslik = request.POST['baslik']
        icerik = request.POST['icerik']
        slug = slugify(baslik)
        Haber.objects.create(baslik=baslik, slug=slug, icerik=icerik)
        return redirect('anasayfa')
    else:
        return render(request, 'haberEkle.html')


# Haber Silme Görünümü (DELETE)
def haberSilG(request, haber_slug):
    haberObj = Haber.objects.get(slug=haber_slug)
    haberObj.delete()
    return redirect('anasayfa')


# Haber Güncelleme Görünümü (UPDATE)
def haberGuncelleG(request, haber_slug):
    if request.method == 'POST':
        baslik = request.POST['baslik']
        icerik = request.POST['icerik']
        haberObj = Haber.objects.get(slug=haber_slug)
        haberObj.baslik = baslik
        haberObj.icerik = icerik
        haberObj.save()
        return redirect('anasayfa')
    else:
        return render(request, 'haberGuncelle.html',
                      {'haber': Haber.objects.get(slug=haber_slug)})
