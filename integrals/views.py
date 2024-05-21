from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import IntegralSerializer
class IntegralApiView(APIView):
    def post(self, request):
        try:
            serializer = IntegralSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({"create":"ok"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": "Internal Server Error","exec":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
