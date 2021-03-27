import requests
resultado = requests.get("https://dog.ceo/api/breed/hound/images/random/3")
print(resultado.content)

