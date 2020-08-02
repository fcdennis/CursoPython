import urllib.request

def siteDisponibilidade(url):
    try:
        urllib.request.urlopen(f'https://{url}')
    except:
        print('O site não está acessível :(')
    else:
        print('Consegui acessar o site com sucesso!')


site = input('Digite o endereço do site: [comece com www...]')
siteDisponibilidade(site)
