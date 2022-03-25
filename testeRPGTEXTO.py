#libs
import json
from termcolor import *
import time

#variaveis


var_dano_leve = [5,10,15,20] #variavel anti_player
var_efct_turnos = [2,4,6,8] #var anti_player
var_efct_chance = [1,2,3] #var anti_player

var_rec_value = [15,16,17,18,19,20] #var que favorece o player, seleciona um valor de 15 a 20, usar em poções pequenas

#fim variaveis

#Itens
item_espada_madeira = {
    "ataque": 5,
    "defesa": 0,
    "skill":"",
}

item_poção_vida_pequena = {
    "recuperar_vida" : var_rec_value[0],

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
        "vida":15,
        "ataque":2,
        "defesa":2,
    }

    cobra = {
        "vida":10,
        "ataque":4,
        "defesa":4,
        "skill": "envenenamento leve",
        "chance_de_envenenamento": var_efct_chance[0],
    }


class Player():
    player_inventory = {} #inventario do jogador

    player_status = {
        "nome":"",
        "vida":100,
        "mana":100,
        "nível":1,
        "envenenado":False,
    }#informações sobre o player


#Funções

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
    cprint("[*] É madrugada, você está dormindo profundamente quando de repente uma voz o chama, você atende a voz? S/N [*]","blue")
    term_usr_inpu = input("[*]")

    #condição para acordar o player
    if term_usr_inpu not in "SimsimNaoNãonãonao":
        cprint("[*] Você deve digitar Sim ou Não",'red')
        aventura_comeca()
    
    #CASO O PLAYER SEJA ACORDADO
    elif term_usr_inpu in "Simsim":

        cprint("""[*] Você acorda, se depara com uma figura que não apresenta corpo físico, mesmo assim você a enxerga perfeitamente.
    A voz diz se chamar Estéria [*]""",'green')#narrador

        cprint(f'''[*] Estéria: -Caro {Player.player_status["nome"]} venho de uma terra distante daqui que passa por serios probemas;
            a algumas semanas o trono de Stone Land foi tomado por um ser maligno conhecido como  MASTER KRAUS e seu exercito de criaturas,
            o rei está desaparecido a dias e os moradores sofrem nas mãos de KRAUS, lhe peço jovem aventureiro, derrote KRAUS e assuma o trono de Stone Land.
            Apenas você poderá recuperar o que perdemos. Você aceita a missão? S/N''','magenta')#Estéria
        
        #input para aceitar a MAIN QUEST DO JOGO
        term_usr_inpu_mission_0 = input("[*]")
        #condição MAIN QUEST
        if term_usr_inpu_mission_0 not in "SimsimNnãao":
            cprint("[*] Você deve digitar Sim ou Não",'red')
            aventura_comeca()
        elif term_usr_inpu_mission_0 in "Simsim":

            #CASO A MISSAO SEJA ACEITA
            cprint("[*] Você aceitou a missão, Estéria lhe entregou uma espada, um mapa e uma armadura [*]",'blue')
            cprint("[*] Itens guardados no inventário ","yellow")

        elif term_usr_inpu_mission_0 in "NaoNãonaonão":

            #CASO A MISSAO SEJA RECUSADA
            cprint("[*] Você recusou a missão, provavelmente estava muito cansado para salvar Stone Land","red")
            creditos()
    
    #CASO O JOGADOR NAO ACORDE O PLAYER
    elif term_usr_inpu in "Nãonão":
        cprint("[*] Você tem um sono muito pesado, isso te impede de viver uma grande aventura","red")
        creditos()
        time.sleep(5)

#ignorar por enquanto TESTE DE FEATURE
def sim_ou_não():
    pass

#FUNÇAO Q CHECA SE É A PRIMEIRA VEZ JOGANDO (IMPORTANTE) O JOGO ToDO DEPENDE DISSO
def primeira_vez_jogando():

    cprint("[*] Olá aventureiro, bem vindo as minhas terras, primeiro diga-me seu nome [*]",'green')  #narrador
    term_input_name = input("[*] Digite o seu nome para iniciar a aventura: ") #narrador

    Player().player_status["nome"] = str(term_input_name) #salva o nome do jogador dentro do objeto Player().player_status["nome"]
        
    cprint(f'[*] Bem vindo {Player.player_status["nome"]} me chamo NOME, serei seu guia pelas terras de NOME DO JOGO [*]',"green") #narrador

    cprint(f'[*] Veja as regras [*]',"green")#narrador

    time.sleep(1) #espera 1 segundos

    cprint('''[*] REGRAS:
    1- O jogo é baseado em turnos, logo o jogador deverá esperar sua vez para realizar uma ação
    2- Para acessar o inventário digite (inventário > opção) exemplo: inventário > usar item > poção
    3- Para checar informações sobre o personagem digite (informações do jogador)
    4- Para usar um feitiço digite (feitiço > nome do feitiço) exemplo: feitiço > bola de fogo
    5- Digite (regras) para ler esta mensagem novamente
    ''',"green") #narrador #REGRAS

    aventura_comeca()



#GAME AREA

class game_main():

    try:
        open("../game..dll") #checa se é a primeira vez jogando, busca um arquivo dll que é criado no inicio do game
        #CONTINUAR SAVE (EM BREVE)
    except:
        primeira_vez_jogando() #EXECUTA O JOGO PELA PRIMEIRA VEZ, AJUDA + HISTORIA + TUTORIAL



