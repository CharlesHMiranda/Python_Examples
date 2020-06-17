import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    # print(response.status_code)
    # print(response.json())
    # print(response.text)
    dados_cep = response.json()
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    # dados_cep = retorna_dados_cep('07097380')
    # print(dados_cep['logradouro'])
    # print(dados_cep['bairro'])
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon['sprites']['front_shiny'])
    response = retorna_response('https://viacep.com.br/')
    print(response)

