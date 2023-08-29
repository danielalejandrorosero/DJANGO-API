from rest_framework import viewsets

from .serializer import ProgrammerSerializer

from .models import Programmer


class ProgrammerViewset(viewsets.ModelViewSet):
    queryset=Programmer.objects.all()
    serializer_class=ProgrammerSerializer

# Create your views here.
