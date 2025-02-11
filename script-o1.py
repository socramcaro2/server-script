import os

################################################################################
# Esta funcion solo cambiaria el menu sin afectar al funcionamiento del script #
################################################################################

def INPUT():
  global que_hacer
  que_hacer = input(''' 
    
    
     ___       ___       ___       ___       ___       ___       ___   
    /\  \     /\  \     /\  \     /\  \     /\  \     /\__\     /\__\  
   /::\  \   /::\  \   /::\  \   /::\  \   /::\  \   /::L_L_   /:/ _/_ 
  /\:\:\__\ /:/\:\__\ /:/\:\__\ /::\:\__\ /::\:\__\ /:/L:\__\ /::-"\__\   
  \:\:\/__/ \:\/:/  / \:\ \/__/ \;:::/  / \/\::/  / \/_/:/  / \;:;-",-"
   \::/  /   \::/  /   \:\__\    |:\/__/    /:/  /    /:/  /   |:|  |  
    \/__/     \/__/     \/__/     \|__|     \/__/     \/__/     \|__|  
  
  
  
  ¿Qué quieres hacer? (ubuntu)

  1. installar tailscale 
  2. Instalar docker 
  3. Instalar portainer (solo se podra configurar como edge agent)
  4. instalar traefik
  5. instalar docker y traefik
  0. salir
  
  Input:   ''')

#################################
# Esta otra maneja las opciones #
#################################
  
def script():
    opcion = str(que_hacer)
    
    if opcion == "1":
      tailscale()
      regreso_al_menu()
  
    elif opcion == "2":
      docker()
      regreso_al_menu()
        
    elif opcion == "3":
      portainer()
      regreso_al_menu()

    elif opcion == "4":
      traefik()
      regreso_al_menu()

    elif opcion == "5":
      docker()
      traefik()
      regreso_al_menu()
      
    elif opcion == "0":
      print("\n  Bye!")

    else:
      correccion = input('\n  Introduce un input valido: ')
      opcion = str(correccion)

#####################################################################    
# se definen las funciones para no realizar tanto codigo espaghetti #
#####################################################################

def tailscale():
  key = str(input("\n  Ingresa una auth key (en blanco para ignorar) \n \n  "))
  auth_command = f'--auth-key={key}' if key else ""
  
  os.system(f"curl -fsSL https://tailscale.com/install.sh | sh && sudo tailscale up {auth_command}")

def docker():
  
  versi0n = str(input("\n  Que version (en blanco para ultima) \n \n  "))
  instalacion = f'--version {versi0n}' if versi0n else ''
  
  os.system('curl -fsSL https://get.docker.com -o install-docker.sh')
  os.system(f'sudo sh install-docker.sh {instalacion}')
  os.system('dockerd-rootless-setuptool.sh install')
  
def portainer():
  os.system()
  
def traefik():
  os.system('sudo su')
  
  os.system('mkdir docker_volumes && cd docker_volumes')
  os.system('mkdir traefik && cd traefik')
  os.system('')
  
  os.system('exit')
  
def regreso_al_menu():
  INPUT()
  script()
  
#############
# ejecucion #
#############

INPUT()
script()
