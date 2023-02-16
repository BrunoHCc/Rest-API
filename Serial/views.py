from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Avaliacao, Cursos
from EstudoDjango.serializers import CursoSerializer, AvaliacaoSerializer

# Create your views here.

class CursoAPIView(APIView):
    """
    API de Cursos
    """
    def get(self, request):
        print(request.user)
        curso = Cursos.objects.all()
        serializer = CursoSerializer(curso, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self,request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CursoInfoAPIView(APIView):

    def get(self,request, id):

        try:
            curso = Cursos.objects.get(id=id)

        except Cursos.DoesNotExist:
            msg = {"msg": "Não encontrado "}
            return Response (msg, status=status.HTTP_404_NOT_FOUND)

        serializer = CursoSerializer(curso)
        return Response (serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):

        try:
            curso = Cursos.objects.get(id=id)

        except Cursos.DoesNotExist:
            msg = {"msg": "Não encontrado "}
            return Response (msg, status=status.HTTP_404_NOT_FOUND)

        serializer = CursoSerializer(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):

        try:
            curso = Cursos.objects.get(id=id)

        except Cursos.DoesNotExist:
            msg = {"msg": "Não encontrado "}
            return Response (msg, status=status.HTTP_404_NOT_FOUND)

        serializer = CursoSerializer(curso, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):

        try:
            curso = Cursos.objects.get(id=id)

        except Cursos.DoesNotExist:
            msg = {"msg": "Não encontrado "}
            return Response (msg, status=status.HTTP_404_NOT_FOUND)

        curso.delete()
        return Response({"msg": "Deletado com sucesso! "}, status=status.HTTP_204_NO_CONTENT)


#################################
#################################

class AvaliacaoAPIView(APIView):
    """
    API de Avaliaçoes
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self,request):
        serializer = AvaliacaoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class AvaliacaoInfoAPIView(APIView):

    def get(self,request, id):

        try:
            avaliacoes = Avaliacao.objects.get(id=id)

        except avaliacoes.DoesNotExist:
            msg = {"msg": "Não encontrado "}
            return Response (msg, status=status.HTTP_404_NOT_FOUND)

        serializer = CursoSerializer(avaliacoes)
        return Response (serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):

        try:
            avaliacoes = Avaliacao.objects.get(id=id)

        except avaliacoes.DoesNotExist:
            msg = {"msg": "Não encontrado "}
            return Response (msg, status=status.HTTP_404_NOT_FOUND)

        serializer = AvaliacaoSerializer(avaliacoes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):

        try:
            avaliacoes = Avaliacao.objects.get(id=id)

        except avaliacoes.DoesNotExist:
            msg = {"msg": "Não encontrado "}
            return Response (msg, status=status.HTTP_404_NOT_FOUND)

        serializer = AvaliacaoSerializer(avaliacoes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):

        try:
            avaliacoes = Avaliacao.objects.get(id=id)

        except avaliacoes.DoesNotExist:
            msg = {"msg": "Não encontrado "}
            return Response (msg, status=status.HTTP_404_NOT_FOUND)

        avaliacoes.delete()
        return Response({"msg": "Deletado com sucesso! "}, status=status.HTTP_204_NO_CONTENT)