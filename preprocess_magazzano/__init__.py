from preprocess_magazzano import utils

__version__ = '0.0.2'

def contpalavras(x):
	return utils._contpalavras(x)

def contcaracteres(x):
	return utils._contcaracteres(x)

def contadorstopwords(x):
	return utils.contadorstopwords(x)

def contadorhashtag(x):
	return utils.contadorhashtag(x)

def contadormentions(x):
	return utils.contadormentions(x)

def contadordigitos(x):
	return utils.contadordigitos(x)

def contadormaiuscula(x):
	return utils.contadormaiuscula(x)

def converteminuscula(x):
	return converteminuscula(x)

def cont_exp(x):
	return utils.cont_exp(x)

def contadoremail(x):
	return utils.contadoremail(x)

def removeemail(x):
	return utils.removeemail(x)

def contadorurl(x):
	return utils.contadorurl(x)

def removeurl(x):
	return utils.removeurl(x)

def removert(x):
	return utils.removert(x)

def removecarpont(x):
	return utils.removecarpont(x)

def removehtml(x):
	return utils.removehtml(x)

def removeacento(x):
	return utils.removeacento(x)

def removestopwords(x):
	return utils.removestopwords(x)

def contvalores(df, col):
	return utils._contvalores(df, col)

def removepalavrascomuns(x, freq, n=20):
	return utils.removepalavrascomuns(x, freq, n)

def removepalavrasraras(x, freq, n=20):
	return utils.removepalavrasraras(x, freq, n)


