# RPG-DE-TEXTO-PARA-A-FEIRA

31/03/22 - Novas funções, features, etc


Planejamento: 

  1- Sistema de Inventario - 50% completo
  2- Sistema de Combate - Completo
  3- Sistema de Níveis do personagem - 20% completo
  4- Sistema de Save - PENDENTE, porém ideias já surgiram
  5- Sistema de Boss Fights - Iniciado, porém fora de funcionamento
  6- Sistema de Dungeons - Ainda não iniciado - tempo para conclusão entre 1 a 2 dias
  7- Multiplataformas - Atualmente o executável roda em Windows, no caso do Linux o arquivo python roda perfeitamente, porém ainda sem executavel
  
Problemas que surgiram:

  1- Utilizar carcteres ACSII para colorir os outputs não funcionou de primeira no Windows - 31/03 - RESOLVIDO - bastava importar o modulo OS e excutar os.system("color") no inicio do código, como o método "color" não é reconhecido pelo linux(pelo menos não no Kali linux) eu adicionei um "try" no inicio do código, dets forma as nova linhas adicionadas foram - import os
                                         try:
                                             os.system("color") #caso no windows inicia o comando color
                                         except:
                                            pass #dessa forma caso o comando color não seja iniciado por qualquer motivo o programa não retornará um erro, apenas pulará a função e executará sem os outputs coloridos
 
 
 
 ---------------------------------------------------------------------- Journal -----------------------------------------------------------------------------------------
 
 [*] Dia 1, correu tudo bem com o inicio do projeto, pelo jeito o melhor nome que consegui pensar foi STONE LAND, hoje escrevi cerca de 200 linhas

[*] Dia 2 trabalhando no código e poucos bugs apareceram e ja foram resolvidos, ainda bem, hoje tive uma eficiencia melhor, adicionei + 250 linhas ao código, sem problemas por enquanto
  
