from django.contrib import admin
from django.urls import path, include
from card_app import views

urlpatterns = [
    path('save/', views.cardsave, name='cardsave' ),
    path('deck/', views.Decklistview.as_view(), name='deck'),
    path('card/', views.Cardlistview.as_view(), name='card'),
]

