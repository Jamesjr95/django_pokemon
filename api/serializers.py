from rest_framework import serializers
from pokemon.models import Pokemon, Type
from django.contrib.auth import get_user_model

class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('name',)
        
        
class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('type',)



class PokemonSerializer(serializers.ModelSerializer):
    type_info = NestedTypeSerializer(many=True, source='types', read_only=True)
    class Meta:
        model = Pokemon
        fields = ('id', 'number', 'type_info', 'name', 'height', 'weight', 'image_front', 'image_back')
        
        
class TypeSerializer(serializers.ModelSerializer):
    pokemon_info = NestedPokemonSerializer(many=True, source='pokemon', read_only=True)
    class Meta:
        model = Type
        fields = ('id', 'type')
        
class UserSerializer(serializers.ModelSerializer):
    caught_info = NestedPokemonSerializer(many=True, read_only=True, source='caught')
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'caught',
            'caught_info'
        )