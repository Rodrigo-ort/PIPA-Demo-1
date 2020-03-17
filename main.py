from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://www.ifb.edu.br/brasilia/noticiasbrasilia")

soup = BeautifulSoup(url.read(), "html.parser")

titulos = []
link_noticia = []
descricao = []
link_imagem = []
horario = []

#pega titulo
for item in soup.select(".tileHeadline"):
	texto = item.get_text().strip()
	titulos.append(texto)
#print(titulos)

#pega link_noticia
for item in soup.select(".tileHeadline"):
	link = ("https://www.ifb.edu.br/brasilia/noticiasbrasilia" + item.a.get('href'))
	link_noticia.append(link)
#print(link_noticia)

#pegar descricao 
for item in soup.select(".description"):
  texto = item.get_text().strip()
  descricao.append(texto)
#print(descricao)
#".description" 

#pegar link_imagem
'''for item in soup.select(".tileImage"):
  link_img = ("https://www.ifb.edu.br/brasilia/noticiasbrasilia" + item.img.get('src'))
print(link_img)
  '''

for item in soup.find_all('div', class_='tileItem'):
	if item.find_all('img', class_='tileImage'):
		link = ("https://www.ifb.edu.br" + item.find_all('img')[0].attrs['src'])
		link_imagem.append(link)
	else:
			link_imagem.append('https://www.ifb.edu.br' + '/images/IFBVertical.png')
#print(link_imagem)

#buscar horario
for item in soup.find_all('div', class_='span2 tileInfo'):
  horario.append(item.find_all('li'))
for i in range(0,len(horario)):
	 horario[i] = "{0} {1}".format(horario[i][2].get_text(), horario[i][3].get_text())
print(horario)