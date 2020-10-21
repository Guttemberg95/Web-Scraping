from bs4 import BeautifulSoup
from requests import get
import pandas as pd
from time import sleep

"""url= 'https://www.brazilian.hostelworld.com/Hostels/Florianopolis/Brasil'
response= get(url)"""

"""Criando uma Soup
soup= BeautifulSoup(response.text, 'html.parser')"""

"""Procurando as class
holstel_containers= soup.findAll(class_='fabresult rounded clearfix hwta-property')"""

"""Quantidade encontrada de holstels na página
len(holstel_containers)"""

"""first_holstel= holstel_containers[0] => código inteiro do primeiro hostel
first_holstel.h2.a.text => nome do holstel
first_holstel.prettify() => para ver o código inteiro do holstel"""

holstel_nome= []
holstel_link= []
holstel_ratings= []
holstel_rewiew= []
holstel_preco= []

for pagina in range(1):
    url= 'https://www.brazilian.hostelworld.com/Hostels/Florianopolis/Brasil' + str(pagina)
    response= get(url)
    soup= BeautifulSoup(response.text, 'html.parser')
    holstel_containers= soup.findAll(class_='fabresult rounded clearfix hwta-property')

    for item in range(len(holstel_containers)):
        holstel_nome.append(holstel_containers[item].h2.a.text)
        holstel_link.append(holstel_containers[item].h2.a.get('href'))
        holstel_ratings.append(holstel_containers[item].find(class_='hwta-rating-score').text.replace('\n', '').strip())
        holstel_rewiew.append(holstel_containers[item].find(class_='hwta-rating-counter').text.replace('\n', '').strip())
        holstel_preco.append(holstel_containers[item].find(class_='price').text.replace('\n', '').strip()[3:])
    sleep(2)

holstel_floripa= pd.DataFrame({
    'Nome': holstel_nome,
    'Nota': holstel_ratings,
    'Rewiew': holstel_rewiew,
    'Preço': holstel_preco,
    'Link': holstel_link
})
print(holstel_floripa.head()

#Criar arquivo csv
holstel_floripa.to_csv('holstel_floripa.csv', encoding='utf-8')











