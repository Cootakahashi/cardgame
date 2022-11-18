from django.contrib import admin
from django.urls import path, include
from card_app import views

urlpatterns = [
    path('save/', views.cardsave, name='cardsave' ),
    path('deck/', views.Decklistview.as_view(), name='deck'),
    path('card/', views.Cardlistview.as_view(), name='card'),
    path('saveinfo/', views.saveinfo, name='saveinfo'),
    path('tessave/', views.tessave, name='tessave'),
    path('card_detail/<int:pk>/', views.card_detail.as_view(), name='card_detail'),
    path('ifrafunc/', views.ifrafunc, name='ifrafunc'),
    path('top/', views.top, name='top')

]

