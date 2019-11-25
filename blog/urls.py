from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfaG, name='anasayfa'),
    path('haber/<int:haber_id>/', views.detayG, name="detay"),
    path('haber/<slug:haber_slug>/', views.detaySlugG, name="detaySlug"),
    path('haberEkle/', views.haberEkleG, name='haberEkle'),
    path('haberSil/<slug:haber_slug>/', views.haberSilG, name='haberSil'),
    path('haberGuncelle/<slug:haber_slug>/', views.haberGuncelleG, name='haberGuncelle'),
]
