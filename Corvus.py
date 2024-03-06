import carreg, os, cr, banners, edc, sys, inf, links, logo
from pystyle import Colorate, Colors


carreg.carreg()

while True:
 
 os.system('clear')
 print(Colorate.Vertical(Colors.blue_to_red, logo.banner1))
 mrpi=input(f'{cr.bpurple}digite sua opção: {cr.white}')
 
 if mrpi=='03' or mrpi=='3':
  
  os.system('clear')
  
  print(edc.criadores1)

  input(f'{cr.bpurple}Pressione enter para voltar ao menu')
 elif mrpi=='00' or mrpi=='0':
  os.system('clear')
  print(f'{cr.bpurple}{banners.black}até a próxima{cr.white}')
  sys.exit()
  
 elif mrpi=='02' or mrpi=='2':

  os.system('clear')

  print(inf.inf1)
 
  input(f'{cr.bpurple}Pressione enter para voltar ao menu')
 
 elif mrpi=='01' or mrpi=='1':

  os.system('clear')

  print(links.Morphei)

  print(f'{cr.red} copie o link que deseja utilizar ou')
   
  input(f'{cr.red} Pressione enter para voltar ao menu')
