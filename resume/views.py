from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer

from .serializers import *
from .models import *


# Create your views here.


class ResumeList(generics.ListCreateAPIView):
    queryset = Resume.objects.all().order_by("-start_date")
    serializer_class = ResumeSerializer


class ResumeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all().order_by("-start_date")
    serializer_class = ResumeSerializer


class ContactInfoList(generics.ListCreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class ContactInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class TechnologyUsedList(generics.ListCreateAPIView):
    queryset = TechnologyUsed.objects.all()
    serializer_class = TechnologyUsedSerializer


class TechnologyUsedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechnologyUsed.objects.all()
    serializer_class = TechnologyUsedSerializer


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def im_a_little_teapot(request):
    data = {'teapot':
                """I'm a little teapot, Short and stout, Here is my handle Here is my spout 
                When I get all steamed up,
                Hear me shout,
                Tip me over and pour me out!

                I'm a very special teapot,
                Yes, it's true,
                Here's an example of what I can do,
                I can turn my handle into a spout,
                Tip me over and pour me out!"""}

    return Response(data, status=status.HTTP_418_IM_A_TEAPOT)
