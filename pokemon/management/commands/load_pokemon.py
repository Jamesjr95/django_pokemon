import json


from django.core.management.base import BaseCommand


from ...models import Pokemon, Type


class Command(BaseCommand):
    
    
    def handle(self, *args, **options):
        
        # clear existing pokemon and Types
        Pokemon.objects.all().delete()
        Type.objects.all().delete()
        
        
        # open Pokemon JSON and load to list of dictionaries
        with open('pokemon.json') as p:
            pokemon_list = json.loads(p.read())
            
            
            # loop through pokemon to add to DB
            for pokemon in pokemon_list['pokemon']:
                
                
                # convert units to m and kg
                pokemon['height'] /= 10
                pokemon['weight'] /= 10
                
                
                # add pokemon to database
                poke_obj = Pokemon.objects.create(
                    number=pokemon['number'],
                    name=pokemon['name'],
                    height=pokemon['height'],
                    weight=pokemon['weight'],
                    image_front=pokemon['image_front'],
                    image_back=pokemon['image_back']
                )
                
                # loop through types list
                # for each type, create type if it doesn't exist yet, than add that type to current Pokemon
                for type in pokemon['types']:
                    type_obj, created = Type.objects.get_or_create(type=type)
                    type_obj.pokemon.add(poke_obj)