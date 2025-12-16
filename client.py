
def imprimer_svg_client(svg):
	'''envoie sur le serveur le fichier svg pour imprimer'''
	import requests 

	url = "http://172.16.100.30:5432/recevoir"

	chaine = {'message' : svg}
	response = requests.post(url, data = chaine)

	return response.text
