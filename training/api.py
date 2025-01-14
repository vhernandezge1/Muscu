from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TrainingTip
from .serializers import TrainingTipSerializer

@api_view(['GET', 'POST'])
def tips_api(request):
    if request.method == 'GET':
        tips = TrainingTip.objects.all()
        serializer = TrainingTipSerializer(tips, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TrainingTipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tip_detail_api(request, pk):
    try:
        tip = TrainingTip.objects.get(pk=pk)
    except TrainingTip.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TrainingTipSerializer(tip)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TrainingTipSerializer(tip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
