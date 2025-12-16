#Convertion en svg 27/11, Clear_Last 2/12, Import de la fonction qui permet d'envoyer au serv 4/12
# importation des bibliothèques
import requests 
import tkinter as tk

# Configuration de la fenêtre principale
root = tk.Tk()
root.title("Paint")
root.geometry("900x636")


# Variables globales
color = 'black'
size = 1
shape = ""
start_x, start_y = None, None
preview = None
saved_shapes = []
url = "http://172.16.100.30:5432/recevoir"

# --- Les fonctions principales ---

def set_shape(s):
	global shape
	shape = s
	highlight_button(s)

def clear_canvas():#Clear tout le canvas 
	global saved_shapes
	canvas.delete("all")
	saved_shapes = []

def clear_last(event):#Clear la forme la plus proche de la souris quand un clique droit est effectué
	global saved_shapes
	x, y = event.x, event.y
	cbl = canvas.find_closest(x, y)[0]
	canvas.delete(cbl)
	saved_shapes = [s for s in saved_shapes if s["iden"] != cbl]

	print("Formes sup:", cbl)
	print("Formes restantes:", saved_shapes)

def start_draw(event):
	global start_x, start_y
	start_x, start_y = event.x, event.y

def draw(event):
	global preview
	x, y = event.x, event.y

	canvas.delete("preview")

	if shape == 'ligne':
		preview = canvas.create_line(start_x, start_y, x, y, fill=color, width=size, dash=(4, 2), tags="preview")
	elif shape == 'rectangle':
		preview = canvas.create_rectangle(start_x, start_y, x, y, outline=color, width=size, dash=(4, 2), tags="preview")
	elif shape == 'oval':
		preview = canvas.create_oval(start_x, start_y, x, y, outline=color, width=size, dash=(4, 2), tags="preview")

def stop_draw(event):
	global start_x, start_y, preview
	x, y = event.x, event.y
	
	canvas.delete("preview")

	if shape == 'ligne':
		idd = canvas.create_line(start_x, start_y, x, y, fill=color, width=size)
		save_co(idd,shape, start_x, start_y, x, y)
	elif shape == 'rectangle':
		idd = canvas.create_rectangle(start_x, start_y, x, y, outline=color, width=size)
		print(canvas.coords(idd))
		save_co(idd,shape, start_x, start_y, x, y)
	elif shape == 'oval':
		idd = canvas.create_oval(start_x, start_y, x, y, outline=color, width=size)
		save_co(idd,shape, start_x, start_y, x, y)

	start_x, start_y, preview = None, None, None

def save_co(idd,forme, x1, y1, x2, y2): #Fonction qui sert à enregistrer les coordonnées des figures 
	global saved_shapes
	save = None
	if forme == "rectangle":
		save = {"iden":idd,"shape": "rect", "x1": x1, "y1": y1, "x2": x2, "y2": y2}
	elif forme == "oval":
		save = {"iden":idd,"shape": "ellipse", "x1": x1, "y1": y1, "x2": x2, "y2": y2}
	elif forme == "ligne":
		save = {"iden":idd,"shape": "line", "x1": x1, "y1": y1, "x2": x2, "y2": y2}
	if save is not None:
		saved_shapes.append(save)
	print(f"{saved_shapes}\n")
	return saved_shapes

def convertion(sauv):
	"""Convertion des coordonnées des formes en code svg"""
	conv = ' <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" > '
	for form in sauv : 
		x1 = form["x1"]
		x2 = form["x2"]
		y1 = form["y1"]
		y2 = form["y2"]
		echelle_x = 1.17
		echelle_y = 1.3
		if form["shape"] == "rect":
			w = x2 - x1 
			h = y2 - y1
			conv = conv + f'<rect x="{x1 * echelle_x}" y="{y1 * echelle_y}" width="{w * echelle_x}" height="{h * echelle_y}" style="stroke:black;  fill:none;" />'
		elif form["shape"] == "ellipse":
			cx = (x1 + x2) / 2
			cy = (y1 + y2) / 2
			rx = (x2 - x1) / 2
			ry = (y2 - y1) / 2
			conv = conv +  f'<ellipse cx="{cx * echelle_x}" cy="{cy * echelle_y}" rx="{rx * echelle_x}" ry="{ry * echelle_y}" style="stroke:black; fill:none;"/>'
		elif form["shape"] == "line":
			conv = conv + f'<line x1="{x1 * echelle_x}" y1="{y1 * echelle_y}" x2="{x2 * echelle_x}" y2="{y2 * echelle_y}" style="stroke:black; stroke-width:2" />'
	conv = conv + "</svg>"
	return conv 



def imprimer_svg_client(svg,url):
	'''envoie sur le serveur le fichier svg pour imprimer'''

	# création du dictionnaire "chaine" contenant le svg
	chaine = {'message' : svg}
	# transfert du svg au serveur
	response = requests.post(url, data = chaine)
	# retourne la reponse
	return response.text



# --- Interface de l'utilisateur ---
toolbar = tk.Frame(root, bg="#ececec", height=50)
toolbar.pack(fill=tk.X, side=tk.TOP, pady=4)

buttons = {}

def make_button(parent, text, command, key):
	b = tk.Button(parent, text=text, command=command, relief=tk.RAISED, bg="#f2f2f2",\
	activebackground="#dcdcdc", width=13, height=2, bd=3)
	b.pack(side=tk.LEFT, padx=6, pady=6)
	buttons[key] = b
	return b

def highlight_button(active):
	for key, btn in buttons.items():
		if key == active:
			btn.config(bg="#cce6ff", relief=tk.SUNKEN)
		else:
			btn.config(bg="#f2f2f2", relief=tk.RAISED)

make_button(toolbar, "Effacer", clear_canvas, "effacer") #Bouton Effacer
make_button(toolbar, "Ligne", lambda: set_shape('ligne'), "ligne") #Bouton pour faire une ligne 
make_button(toolbar, "Rectangle", lambda: set_shape('rectangle'), "rectangle") #Bouton pour faire un rectangle
make_button(toolbar, "Oval", lambda: set_shape('oval'), "oval") #Bouton pour faire un oval
make_button(toolbar, "Creer Code SVG", lambda : convertion(saved_shapes) , "Code SVG")#Bouton pour créer le code SVG 
make_button(toolbar, "Envoyer au serveur", lambda : imprimer_svg_client(convertion(saved_shapes),url), "Envoi")#Bouton pour envoyer au serv 

# Le canvas principal
canvas = tk.Canvas(root, bg='white', highlightthickness=0, cursor="cross")
canvas.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)

# Événements
canvas.bind('<Button-1>', start_draw)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>', stop_draw)
canvas.bind("<Button-3>", clear_last)


# Lancement
root.mainloop()

