import re
import os
import sys
import pandas as pd
import numpy as np
import spacy
from spacy.lang.pt.stop_words import STOP_WORDS as stopwords
from bs4 import BeautifulSoup
import unicodedata


# contador de palavras
def _contpalavras(x):
	length = len(str(x).split())
	return length

# contador de caracteres
def _contcaracteres(x):
	s = x.split()
	x = ''.join(s)
	return len(x)

# tamanho médio das palavras
def _tamanho_medpalavras(x):
	media = _contcaracteres(x)/_contpalavras(x)
	return media

# contador de stopwords
def _contadorstopwords(x):
	l = len([t for t in x.split() if t in stopwords])
	return l

# contador de #tags
def _contadorhashtag(x):
	l = len([t for t in x.split() if t.startswith('#')])
	return l

# contadodor de @mentions
def _contadormentions(x):
	l = len([t for t in x.split() if t.startswith('@')])
	return l

# contador de dígitos numéricos
def _contadordigitos(x):
	l = len([t for t in x.split() if t.isdigit()])
	return l

# contador de palavras maiusculas
def _contadormaiuscula(x):
	l = len([t for t in x.split() if t.isupper()])
	return l

# converte todas as letras em minusculas
def _converteminuscula(x):
	return str(x).lower()

# expande contrações
def _cont_exp(x):
	contracoes = { 
	"cadê": "onde está",
	"quedê": "onde está",
	"pra": "para a",
	"pro": "para o"}

	if type(x) is str:
		for key in contracoes:
			value = contracoes[key]
			x = x.replace(key, value)
		return x
	else:
		return x

# contador de emails
def _contadoremail(x):
	emails = re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+\b)', x)
	l = len(emails)
	return l, emails

# remove emails
def _removeemail(x):
	return re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"", x)

# contador de URLs
def _contadorurl(x):
	url = re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', x)
	l = len(url)
	return l, url

# remove URLs
def _removeurl(x):
	return re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '' , x)

# remove RT
def _removert(x):
	return re.sub(r'\brt\b', '', x).strip()

# remove caracteres especiais, pontuação e espaços extras
def _removecarpont(x):
	x = re.sub(r'[^\w ]+', "", x)
	x = ' '.join(x.split())
	return x

# remove HTMLs
def _removehtml(x):
	return BeautifulSoup(x, 'lxml').get_text().strip()

# remove acentuação
def _removeacento(x):
	x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore')
	return x

# remove stopwords
def _removestopwords(x):
	return ' '.join([t for t in x.split() if t not in stopwords])

# remove palavras "comuns"; n = % palavras a ser retirada
def _removepalavrascomuns(x, n=20):
	text = x.split()
	freq_comm = pd.Series(text).value_counts()
	fn = freq_comm[:n]
	x = ' '.join([t for t in x.split() if t not in fn])
	return x

# remove palavras raras; n = % palavras a ser retirada
def _removepalavrasraras(x, n=20):
	text = x.split()
	freq_comm = pd.Series(text).value_counts()
	fn = freq_comm.tail(n)	
	x = ' '.join([t for t in x.split() if t not in fn])
	return x












