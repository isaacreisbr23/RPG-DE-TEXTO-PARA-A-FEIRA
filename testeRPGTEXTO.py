#libs
from contextlib import nullcontext
import json  
import time
import random
import termcolor
import os

try:
    os.system("color") #inicia o modo de cor do windows
except:
    print("color não foi iniciado")

#CORES DOS OUTPUTS DO TERMINAL
class Cores:
    verde = "\033[92m"
    ciano = "\033[96m"
    magenta = "\033[35m"
    amarelo = "\033[33m"
    vermelho = "\033[31m"
    fimdecor = "\033[0m"


#variaveis

player_turn = False
enemy_turn = False

var_turn = 0

var_decis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
var_enemys_decis = [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

var_dano_leve = [5,10,15,20] #variavel anti_player
var_efct_turnos = [2,4,6,8] #var anti_player
var_efct_chance = [1,2,3] #var anti_player

var_rec_value = [15,16,17,18,19,20] #var que favorece o player, seleciona um valor de 15 a 20, usar em poções pequenas

var_cidade  = "" #variavel importante para o salvamento do game, salva onde o player se encontra

#fim variaveis

#Itens
item_espada_madeira = {
    "nome":"espada de madeira",
    "ataque": 5,
    "defesa": 0,
    "skill":"",
}

item_poção_vida_pequena = {
    "recuperar_vida" : var_rec_value[0],

}

item_armadura_basica = {
    "nome" : "armadura basica",
    "defesa": 5,
    "skill": "",
}
#Fim Itens

#efeitos anti-player
efct_poison = {
    "tipo":"envenenamento",
    "dano": var_dano_leve[0],
    "duração_turnos": var_efct_turnos[0],
    
}


#inimigos

class Enemys():
    morcego = {
    "nome":"morcego",
        "vida":15,
        "ataque":5,
        "defesa":2,
    }

    cobra = {
    "nome":"cobra",
        "vida":10,
        "ataque":6,
        "defesa":4,
        "skill": "envenenamento leve",
        "chance_de_envenenamento": var_efct_chance[0],
    }


class Player():

    player_itens_list = [] #lista de itens que salva os itens coletados durante a gameplay/ Usada no inventario

    player_inventory = {
        "itens": player_itens_list,
    } #inventario do jogador

    player_status = {
        "nome":"",
        "vida":100,
        "mana":100,
        "nível":1,
        "envenenado":False,
        "defesa":0,
        "ataque":0,
    } #informações sobre o player

class Player_decisions():

    def start():
        player_decision = input("[*] O que você faz?: ")

        def fugir(): #CRIA A POSSIBILIDADE DO PLAYER FUGIR DA LUTA (DISPONIVEL APENAS FORA DE LUTAS DE BOSS)
            fugir_roll = random.choice(var_decis)

            if fugir_roll <= 5:
                print(f'{Cores.amarelo}[*] Você resolve fugir de forma engraçada{Cores.fimdecor}')
            elif fugir_roll >5:
                print(f'{Cores.vermelho}[*] Você resolve fugir de forma engraçada, mas falha miseravelmente {Cores.fimdecor}')
                

        if player_decision in "FugaFugirfugafugircorrerCorrerRunrun":
            fugir()


#Funções

def check_turn():

    if  var_turn <= 0:
        print(f'{Cores.amarelo}[*] Seu turno {Cores.fimdecor}')
        player_turn = True
    elif var_turn > 1:
        print(f'{Cores.amarelo}[*] Turno inimigo {Cores.fimdecor}')
        enemy_turn = True

def start_combat():
    enemy_roll = random.choice(var_enemys_decis)

    if enemy_roll <= 10: #adiciona um morcego como inimigo
        active_enemy = Enemys.morcego
    elif enemy_roll <= 20: #adiciona uma cobra como inimigo
        active_enemy = Enemys.cobra
    
    print(enemy_roll)
    print(f'{Cores.vermelho}[*] Um {active_enemy["nome"]} apareceu {Cores.fimdecor}')
    print("")
    print(f'{Cores.vermelho}[*] {active_enemy["nome"]} possui {active_enemy["ataque"]} pontos de ataque {Cores.fimdecor}')
            
    go_first_desc = [1,2,3,4,5,6]

    roll_go_first = random.choice(go_first_desc)

    def enemy_atk():
        var_turn = 0
        check_turn()

        if enemy_turn:
            print(f'{Cores.vermelho}[*]{active_enemy["nome"]} desferiu um ataque de {active_enemy["ataque"]} pontos! {Cores.fimdecor}')

            player_dano_sofrido = active_enemy["ataque"] - Player.player_status["defesa"]
            Player.player_status["vida"] = Player.player_status["vida"] - player_dano_sofrido

            print("")
            print(f'{Cores.amarelo}[*] Você sofreu {player_dano_sofrido} pontos de dano {Cores.fimdecor}')
            print("")
            print(f'{Cores.amarelo}[*] Sua vida agora é {Player.player_status["vida"]} {Cores.fimdecor}')

    def player_turn():
        var_turn = 1
        check_turn

        if player_turn:
            print(f'{Cores.amarelo}[*]Seu turno{Cores.fimdecor}')
            Player_decisions.start()
        

    if roll_go_first <= 3: #COMBATE
        enemy_atk()
    elif roll_go_first >=6:
        player_turn()

def roll_the_big_dice(): #FUNÇÃO LIGADA A GRANDE PARTE DAS DECISOES, todas as outras decisoes ramdomizadas do game sao variantes desta função
    roll = random.choice(var_decis)

    if roll <= 20 : #chama função para começar um combate
        start_combat()

    print(str(roll))


#creditos
def creditos():
    print("""----------STONE LAND----------
    programado por: Isaac G. A. dos Reis 1°A
    roteiro por: Isaac G. A. dos Reis 1°A
    agradecimentos: IP CONTROL, Anglo Viçosa
    parceiros: @isc.reis.av, @ipcontroltecnologias""")
    time.sleep(5)

#função que começa o game
def aventura_comeca():

    #Sonho do player
    print(f'{Cores.verde} [*] É madrugada, você está dormindo profundamente quando de repente uma voz o chama, você atende a voz? S/N [*] {Cores.fimdecor}')
    print("")#Espaço no terminal
    term_usr_inpu = input("[*]")
    print("")#Espaço no terminal

    #condição para acordar o player
    if term_usr_inpu not in "SimsimNaoNãonãonao":
        print(f'{Cores.vermelho}[*] Você deve digitar Sim ou Não {Cores.fimdecor}')
        aventura_comeca()
    
    #CASO O PLAYER SEJA ACORDADO
    elif term_usr_inpu in "Simsim":

        print(f'''{Cores.verde}[*] Você acorda, se depara com uma figura que não apresenta corpo físico, mesmo assim você a enxerga perfeitamente.
    A voz diz se chamar Estéria [*]{Cores.fimdecor}''')#narrador
        print("")

        print(f'''{Cores.magenta}[*] Estéria: -Caro {Player.player_status["nome"]} venho de uma terra distante daqui que passa por serios probemas;
            a algumas semanas o trono de Stone Land foi tomado por um ser maligno conhecido como  MASTER KRAUS e seu exercito de criaturas,
            o rei está desaparecido a dias e os moradores sofrem nas mãos de KRAUS, lhe peço jovem aventureiro, derrote KRAUS e assuma o trono de Stone Land.
            Apenas você poderá recuperar o que perdemos. Você aceita a missão? S/N {Cores.fimdecor}''')#Estéria
        
        print("")#Espaço no terminal
        
        #input para aceitar a MAIN QUEST DO JOGO
        term_usr_inpu_mission_0 = input("[*]")
        #condição MAIN QUEST
        if term_usr_inpu_mission_0 not in "SimsimNnãao":
            print(f'{Cores.vermelho}[*] Você deve digitar Sim ou Não {Cores.fimdecor}')
            aventura_comeca()
        elif term_usr_inpu_mission_0 in "Simsim":

            #CASO A MISSAO SEJA ACEITA
            print(f'{Cores.verde}[*] Você aceitou a missão, Estéria lhe entregou uma espada, um mapa e uma armadura [*]{Cores.fimdecor}')
            print("")#Espaço no terminal
            print(f'{Cores.amarelo}[*] Itens guardados no inventário {Cores.fimdecor}')

            Player.player_status["defesa"] = item_armadura_basica["defesa"] #Adiciona ao player a defesa da armadura basica
            Player.player_status["ataque"] = item_espada_madeira["ataque"] #Adiciona ao player o ataque da espada de madeira

            Player.player_itens_list.append(item_espada_madeira["nome"])
            Player.player_itens_list.append(item_armadura_basica["nome"])
            print(Player.player_inventory)
            print("")#Espaço no terminal

            print(f'{Cores.amarelo}[*] Sua defesa agora é: {Player.player_status["defesa"]} {Cores.fimdecor}') #info ao jogador
            print(f'{Cores.amarelo}[*] Seu ataque agora é: {Player.player_status["ataque"]} {Cores.fimdecor}') #info ao jogador 

            roll_the_big_dice()
            

        elif term_usr_inpu_mission_0 in "NaoNãonaonão":

            #CASO A MISSAO SEJA RECUSADA
            print(f'{Cores.vermelho}[*] Você recusou a missão, provavelmente estava muito cansado para salvar Stone Land {Cores.fimdecor}')
            creditos()
    
    #CASO O JOGADOR NAO ACORDE O PLAYER
    elif term_usr_inpu in "Nãonão":
        print(f'{Cores.vermelho}[*] Você tem um sono muito pesado, isso te impede de viver uma grande aventura{Cores.fimdecor}')
        creditos()
        time.sleep(5)

#ignorar por enquanto TESTE DE FEATURE
def sim_ou_não():
    pass

#FUNÇAO Q CHECA SE É A PRIMEIRA VEZ JOGANDO (IMPORTANTE) O JOGO ToDO DEPENDE DISSO
def primeira_vez_jogando():

    print(f'{Cores.verde}[*] Olá aventureiro, bem vindo as minhas terras, primeiro diga-me seu nome [*] {Cores.fimdecor}')  #narrador
    term_input_name = input("[*] Digite o seu nome para iniciar a aventura: ") #narrador

    Player().player_status["nome"] = str(term_input_name) #salva o nome do jogador dentro do objeto Player().player_status["nome"]
        
    print(f'{Cores.verde}[*] Bem vindo {Player.player_status["nome"]} me chamo NOME, serei seu guia pelas terras de NOME DO JOGO [*]{Cores.fimdecor}') #narrador

    print("")#Espaço no terminal

    print(f'{Cores.verde}[*] Veja as regras [*]{Cores.fimdecor}')#narrador
    print("")#Espaço no terminal

    time.sleep(1) #espera 1 segundos

    print(f'''{Cores.verde}[*] REGRAS:
    1- O jogo é baseado em turnos, logo o jogador deverá esperar sua vez para realizar uma ação
    2- Para acessar o inventário digite (inventário > opção) exemplo: inventário > usar item > poção
    3- Para checar informações sobre o personagem digite (informações do jogador)
    4- Para usar um feitiço digite (feitiço > nome do feitiço) exemplo: feitiço > bola de fogo
    5- Digite (regras) para ler esta mensagem novamente
    {Cores.fimdecor}''') #narrador #REGRAS

    aventura_comeca()



#GAME AREA

class game_main():

    try:
        open("../game..dll") #checa se é a primeira vez jogando, busca um arquivo dll que é criado no inicio do game
        #CONTINUAR SAVE (EM BREVE)
    except:
        primeira_vez_jogando() #EXECUTA O JOGO PELA PRIMEIRA VEZ, AJUDA + HISTORIA + TUTORIAL
