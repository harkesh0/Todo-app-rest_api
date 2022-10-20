from rest_framework import viewsets

from my_awesome_api.serializers import PersonSerializer
from my_awesome_api.models import Person


class PersonViewSet(viewsets.ModelViewSet):
   queryset = Person.objects.all()
   serializer_class = PersonSerializer