##
##		Esse script foi escrito por Cairé C. Rocha
##
##		Esse script rola a página para baixo e para cima
##
##		Esse script foi desenvolvido para a Godot 3.2.3
##
##

extends TextureRect


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
export (Vector2) var limites
export (float) var salto

## Essa função captura eventos ocorridos
func _input(event):
	## Verifica se o scroll do mouse foi acionado
	if event is InputEventMouseButton:
		if event.get_button_index() == 4:
			if(self.margin_top < limites.x):
				self.margin_top += salto
#				print("subir")
		if event.get_button_index() == 5:
			if(self.margin_top > limites.y):
				self.margin_top -= salto
#				print("descer")

## Essa função retorna a página para a posição inicial, limites.x
func retoma():
	self.margin_top = limites.x
