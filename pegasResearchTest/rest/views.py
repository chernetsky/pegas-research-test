from rest_framework.views import APIView
from rest_framework.response import Response
from data.models import ClientData
from .serializers import ClientDataSerializer


class DataView(APIView):
    '''
    REST API view
    '''
    def get(self, request):
        data = ClientData.objects.all()
        serializer = ClientDataSerializer(data, many=True)
        
        responseData = [(r['timestamp'], r['value']) for r in serializer.data]

        return Response({"data": responseData})


    def post(self, request):
        # clientId = request.data.get('clientId')
        dataRows = request.data.get('data')
        for row in dataRows:    
            serializer = ClientDataSerializer(data=row)
            if (serializer.is_valid(raise_exception=True)):
                serializer.save()
        return Response({"success": "Data row saved"})