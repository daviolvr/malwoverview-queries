from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import InsertService


class HashView(APIView):
    def post(self, request):
        file_hash = request.data.get("file_hash")

        if not file_hash:
            return Response(
                {"error": "file_hash é obrigatório"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data_dict = InsertService.realizar_buscas_paralelas(file_hash)

        inserted_id = InsertService.db_insert(data_dict)

        return Response({
            "message": "Dados inseridos com sucesso",
            "inserted_id": inserted_id
        }, status=status.HTTP_201_CREATED)

