
from .serializers import StudentSerializer
from .models import Student
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# Create your views here.

class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[IsAuthenticated]

    filterset_fields = [
        'course',
        'city',
    ]

    search_fields = [
        'name',
        'email',
        'course',
        'city',
    ]