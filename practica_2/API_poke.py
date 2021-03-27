mport requests

url= 'https://pokeapi.co/api/v2/pokemon-form'

respuesta = requests.get(url)

pokemon = respuesta.json()
lpokemon = pokemon.get('results', [])

for i in lpokemon:
    print(i['name'])
