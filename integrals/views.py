from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from integrals.response.IntegralDataResponseSerializer import IntegralDataSerializer
from .serializers import IntegralSerializer
class IntegralApiView(APIView):
    def post(self, request):
        try:
            serializer = IntegralSerializer(data=request.data)

            if serializer.is_valid():
                integral_data_response = serializer.save()
                integral_data_response_serializer = IntegralDataSerializer(integral_data_response)
                    
                return Response(integral_data_response_serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": "Internal Server Error","exec":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
