from rest_framework import serializers

from my_awesome_api.models import Person

class PersonSerializer(serializers.ModelSerializer):
   class Meta:
       model = Person
       fields = ('firstname', 'lastname', 'nickname')