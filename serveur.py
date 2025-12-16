from pyaxidraw import axidraw   
import cherrypy 
import os

def index():
	''' instanciation de la page index '''
	return "Hello"

def recevoir(message,imprimer=True):
	''' instanciation de la page recevoir, permettant le traitement du fichier svg et son impression  '''
	# source pour le traitement du svg : https://stackoverflow.com/questions/71104397/how-to-convert-svg-string-to-svg-file-using-python
	with open("svgTest.svg", "w") as svg_file:
			svg_file.write(message)
			print("fichier enregistré")
	# imprime le svg si imprimer = True
	if imprimer:
		ad = axidraw.AxiDraw()
		ad.plot_setup("svgTest.svg")
		ad.plot_run()
	
	print(message)
	# retourne le svg reçu
	return f"Chaine reçue : {message}"

# exposition des pages
index.exposed = True
recevoir.exposed = True

# configuration réseau
cherrypy.config.update({
        'server.socket_host': '0.0.0.0',   # Accessible depuis tout le réseau
        'server.socket_port': 5432,
        'server.thread_pool': 8,}
    )

# lancement du serveur web
cherrypy.tree.mount(index, "/")
cherrypy.tree.mount(recevoir, "/recevoir")

cherrypy.engine.start()
cherrypy.engine.block()


