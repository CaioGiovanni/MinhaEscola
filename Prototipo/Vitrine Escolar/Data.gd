##
##		Esse script foi escrito por Cairé C. Rocha
##
##		Esse pega a hora e muda a imagem do fundo para condizer
##		com a iluminação da rua da Aurora.
##
##		Esse script foi desenvolvido para a Godot 3.2.3
##
##

extends Label


# Called when the node enters the scene tree for the first time.
func _ready():
	var dia = OS.get_datetime()
	## escreve a data e a hora no canto da página
	self.text = str(dia["day"]) + "    " + str(dia["month"]) + "     " + str(dia["year"])

