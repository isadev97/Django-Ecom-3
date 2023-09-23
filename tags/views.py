# Create your views here.
from rest_framework import views , status
from rest_framework.response import Response 
from tags.serializer import WriteTagSerializer, ReadTagSerializer
from tags.models import Tags
from django.utils.text import slugify
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView
from products.filters import SimplePaginationClass
from authentication.permissions import IsAdmin

class CreateTagView(APIView):
    permission_classes = (IsAdmin, )
    
    # def get(self, request):
    #     pass 
    
    # def put(self, request):
    #     pass 
    
    # def delete(self, request):
    #     pass
    
    def post(self, request):
        serializer = WriteTagSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            tag_object = Tags.objects.create(name=name, slug=slugify(name))
            response_data = ReadTagSerializer(instance=tag_object).data 
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagDetailViewV1(APIView):
    
    def get(self, request, slug):
        try:
            tag_object = Tags.objects.get(slug=slug)
            print(tag_object)
            response_data = ReadTagSerializer(instance=tag_object).data 
            print(response_data)
            return Response(response_data, status=status.HTTP_200_OK)
        except (Tags.DoesNotExist, Tags.MultipleObjectsReturned):
            return Response({"message" : "Tag not found !"}, status=status.HTTP_400_BAD_REQUEST)


class TagDetailViewV2(RetrieveAPIView):
    queryset = Tags.objects.all()
    serializer_class = ReadTagSerializer
    lookup_field = "slug"
    

class DeleteTagView1(APIView):
    
    def delete(self, request, slug):
        try:
            tag_object = Tags.objects.get(slug=slug)
            tag_object.delete()
            return Response({"message" : "Tag deleted"}, status=status.HTTP_200_OK)
        except (Tags.DoesNotExist, Tags.MultipleObjectsReturned):
            return Response({"message" : "Tag not found !"}, status=status.HTTP_400_BAD_REQUEST)

class DeleteTagView2(DestroyAPIView):
    queryset = Tags.objects.all()
    lookup_field = "slug"
    

class TagListView1(APIView):
    
    def get(self, request):
        queryset = Tags.objects.all()
        response_data = ReadTagSerializer(instance=queryset, many=True).data 
        return Response(response_data, status=status.HTTP_200_OK)


class TagListView2(ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = ReadTagSerializer
    pagination_class = SimplePaginationClass

    
        