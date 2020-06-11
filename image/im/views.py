from django.shortcuts import render

# Create your views here.
from .serializers import ImageSerializer
from rest_framework.views import APIView
from utils.chaojiying import tranformImgCode
from image.settings import BASE_DIR
import os
from rest_framework.response import Response
from .models import ImageModel


class ImageAPIView(APIView):

    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        image = request.FILES['image']
        for i in image:
            with open('image.png', 'ab')as f:
                f.write(i)
        image_url = os.path.join(BASE_DIR, 'image.png')
        result = tranformImgCode(image_url, 3004)
        os.remove(BASE_DIR+'/image.png')
        json_result = {"content": []}
        for j in result:
            json_result['content'].append(j)

        instance = ImageModel.objects.create(
            image=image,
            json_result=json_result
        )

        return Response(json_result)

