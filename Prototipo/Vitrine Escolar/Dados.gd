##
##		Esse script foi escrito por Cairé C. Rocha
##
##		Esse script é o primeiro protótipo do projeto
##		da disciplina de desenvolvimento web e não representa
##		o produto final.
##
##		Esse script foi desenvolvido para a Godot 3.2.3
##
##
extends Control


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
export (int) var destaque = 0 #Esse valor diz qual o destaque
var escolas #Lista das escolas
var paginas #Histórico de navegação
var seccoes #Páginas do site


##	Filtros de pesquisa
var alfa = false
var fun = false
var funn = false
var medio = false
var prof = false
var eja = false
var manha = true
var tarde = true
var noite = true
var integral = true


# Essa função é chamada quando o programa inicia
func _ready():
	## O programa procura os nodes que representam as seções do site
	seccoes = {}
	seccoes["Home"] = $Vitrine/Home
	seccoes["Quarry"] = $Vitrine/Quarry
	seccoes["School"] = $Vitrine/School
	print(seccoes["Home"])
	
	## O histórico de navegação é atualizado
	paginas = ["Home"]
	
	## Os dados são carregados para exibir as informações das escolas.
	var f = File.new()
	f.open("res://data.json", File.READ)
#	print(f.get_line())
	var dat = f.get_line()
	escolas = JSON.parse(dat).get_result()['escolas']
	
	print(escolas[0]['nome'])
	
	## A página é atualizada
	pagina()


##	Essa função atualiza a página
func pagina():
	## Esconde todos os nodes que representam seções do site
	for i in seccoes:
		seccoes[i].hide()
	
	## Retoma a página para a posição inicial
	$Vitrine.retoma()
	
	## opera o endereço atual para ele se tornar o endereço e os parametros.
	var at = paginas[-1].split("/")
	
	## Exibe o node que representa a página atual
	seccoes[at[0]].show()
	
	## Injeta informações na seção Home
	if (at[0] == "Home"):
		var tx = load(escolas[destaque]["foto"])
		var es = seccoes[at[0]].find_node("Escola")
		es.find_node("Foto").set_texture(tx)
		es.find_node("Escola").set_text(escolas[destaque]["nome"])
		es.find_node("Texto").set_text(escolas[destaque]["descricao"])



## Essa função limpa os filtros de pesquisa
func _limpar():
	alfa = false
	fun = false
	funn = false
	medio = false
	prof = false
	eja = false
	manha = true
	tarde = true
	noite = true
	integral = true

## Essa função também limpa os filtros de pesquisa
func _limpar2():
	alfa = true
	fun = true
	funn = true
	medio = true
	prof = true
	eja = true
	manha = true
	tarde = true
	noite = true
	integral = true


## Essa função retorna os filtros de pesquisa como uma lista
func _listar():
	return [alfa, fun, funn, medio, prof, eja, manha, tarde, noite, integral]

## Essa função assinala os chekins para condizer com os filtros de pesquisa
func _checkins():
	## Lista todos os nodes que representam chekins de filtros
	var cb = seccoes["Quarry"].get_child(0)
	var lista = []
	for i in range(2):
		for j in cb.get_child(i).get_children():
			lista.append(j)
	
	## Atualiza todos os nodes que representam chekins de filtros
	for i in range(len(_listar())):
		if (lista[i].pressed != _listar()[i]):
			lista[i].pressed = _listar()[i]

## Quando o botão buscar é pressionado
func _on_busc_pressed():
	self.paginas.append("Quarry")
	_limpar2()
	_checkins()
	pagina()

## Quando o botão pre-alfabetização é pressionado
func _on_alfa_pressed():
	self.paginas.append("Quarry")
	_limpar()
	alfa = true
	_checkins()
	pagina()

## Quando o botão Fundamental I é pressionado
func _on_fun_pressed():
	self.paginas.append("Quarry")
	_limpar()
	fun = true
	_checkins()
	pagina()

## Quando o botão Fundamental II é pressionado
func _on_funn_pressed():
	self.paginas.append("Quarry")
	_limpar()
	funn = true
	_checkins()
	pagina()

## Quando o botão Ensino Médio é pressionado
func _on_medio_pressed():
	self.paginas.append("Quarry")
	_limpar()
	medio = true
	_checkins()
	pagina()

## Quando o botão Ensino Profissionalizante é pressionado
func _on_prof_pressed():
	self.paginas.append("Quarry")
	_limpar()
	prof = true
	_checkins()
	pagina()

## Quando o botão Ensino EJA é pressionado

## Quando o usuário clicka na logo
func _on_Home_pressed():
	self.paginas.append("Home")
	pagina()
