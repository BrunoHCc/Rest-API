from django.urls import path

from .views import CursoAPIView, AvaliacaoAPIView, CursoInfoAPIView, AvaliacaoInfoAPIView


urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacao/', AvaliacaoAPIView.as_view()),
    path('cursos/<int:id>/', CursoInfoAPIView.as_view()),
    path('avaliacao/<int:id>/', AvaliacaoInfoAPIView.as_view()),
]