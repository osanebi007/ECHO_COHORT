from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import NewsSerializer
from .models import  News
from .permissions import IsAuthor
from django.shortcuts import get_object_or_404  


@api_view(["GET"])
def get_news(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response({"message": "News retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthor])
def create_news(request): 
    news_data = request.data
    serializer = NewsSerializer(data=news_data)
    if serializer.is_valid():
       serializer.save(author=request.user)
       return Response({"message": "News created successfully"}, status=status.HTTP_200_OK)
    else:
       return Response({"message": "Something went wrong.", "error": serializer.errors} ,status=status.HTTP_401_UNAUTHORIZED)



@api_view(["PUT", "PATCH"])
@permission_classes([IsAuthor])
def update_news(request, id):
    try:
        news_data = News.objects.get(id=id)
    except News.DoesNotExist:

        return Response({"message": "Sorry. The news you are looking for does not exists"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = NewsSerializer(news_data, data=request.data)
    else:
        serializer = NewsSerializer(news_data, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "News updated successfully."}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Something went wrong", "error": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
@permission_classes([IsAuthor])
def delete_news(request):
    try:
        news_data = News.objects.get(id=id)
    except News.DoesNotExist:
        return Response({"message": "Sorry, The news you are looking for does not exists."}, status=status.HTTP_404_NOT_FOUND)
    
    news_data.delete
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["PATCH"])
def like_news(request, id):

    news  = get_object_or_404(News, id=id)
    news.likes.add(request.user)    

    return Response({"message": "News liked."})