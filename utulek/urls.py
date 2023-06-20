from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('utulky/', views.UtulekListView.as_view(), name='utulky_list'),
    path('utulky/<int:pk>', views.UtulekDetailView.as_view(), name='utulek_detail'),
    path('psi/', views.PesListView.as_view(), name='psi_list'),
    path('psi/<int:pk>', views.PesDetailView.as_view(), name='pes_detail'),
]
