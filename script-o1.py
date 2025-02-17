import os
import bcrypt
execute = os.system

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
  
  execute(f"curl -fsSL https://tailscale.com/install.sh | sh && sudo tailscale up {auth_command}")

def docker():
  
  versi0n = str(input("\n  Que version (en blanco para ultima) \n \n  "))
  instalacion = f'--version {versi0n}' if versi0n else ''
  
  execute('curl -fsSL https://get.docker.com -o install-docker.sh')
  execute(f'sudo sh install-docker.sh {instalacion}')
  execute('dockerd-rootless-setuptool.sh install')
  
def portainer():
  execute
  

  
  
def traefik():
  # el script se hizo en mente con traefik 3.0 en mente
  
  # variables para personalizar la instalacion
  Cloudfare_Api = input('Cual es tu Api de cloudfare: ')
  Tu_dominio = input("cual es tu Dominio? debes ser el dueño: ") 
  Tu_correo = input('ingresa tu email de cloudfare: ')
  Usuario_panel = input('ingresa usuario para el panel de traefik: ')
  Contraseña_panel = input('ingresa la contraseña para el panel de traefik: ')
  Confrimar_contraseña = input('vuelve a introducir la contraseña: ')
  
  # verificar contraseñas correctas
  
  i=0
  
  while i == 0:
    if Contraseña_panel == Confrimar_contraseña:
      i +=1
    else:
      print('\n \n Introduce correctamente las contraseñas \n \n')
      Contraseña_panel = input('ingresa la contraseña para el panel de traefik: ')
      Confrimar_contraseña = input('vuelve a introducir la contraseña: ')
      

  # contenido de los archivos que se van a crear
  Docker_Compose = f"""version: "3.8"

services:
  traefik:
    image: traefik
    container_name: traefik
    restart: unless-stopped
    security_opt:
      - no-new-privileges:true
    networks:
      - proxy
    ports:
      - 80:80
      - 443:443
      # - 443:443/tcp # Uncomment if you want HTTP3
      # - 443:443/udp # Uncomment if you want HTTP3
    environment:
      CF_DNS_API_TOKEN_FILE: /run/secrets/cf_api_token # note using _FILE for docker secrets
      # CF_DNS_API_TOKEN: ${{CF_DNS_API_TOKEN}} # if using .env
      TRAEFIK_DASHBOARD_CREDENTIALS: ${{TRAEFIK_DASHBOARD_CREDENTIALS}}
    secrets:
      - cf_api_token
    env_file: .env # use .env
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./data/traefik.yml:/traefik.yml:ro
      - ./data/acme.json:/acme.json
      - ./data/config.yml:/config.yml:ro
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.traefik.entrypoints=http"
      - "traefik.http.routers.traefik.rule=Host(`traefik-dashboard.local.{Tu_dominio}`)"
      - "traefik.http.middlewares.traefik-auth.basicauth.users=${{TRAEFIK_DASHBOARD_CREDENTIALS}}"
      - "traefik.http.middlewares.traefik-https-redirect.redirectscheme.scheme=https"
      - "traefik.http.middlewares.sslheader.headers.customrequestheaders.X-Forwarded-Proto=https"
      - "traefik.http.routers.traefik.middlewares=traefik-https-redirect"
      - "traefik.http.routers.traefik-secure.entrypoints=https"
      - "traefik.http.routers.traefik-secure.rule=Host(`traefik-dashboard.local.{Tu_dominio}`)"
      - "traefik.http.routers.traefik-secure.middlewares=traefik-auth"
      - "traefik.http.routers.traefik-secure.tls=true"
      - "traefik.http.routers.traefik-secure.tls.certresolver=cloudflare"
      - "traefik.http.routers.traefik-secure.tls.domains[0].main=local.{Tu_dominio}"
      - "traefik.http.routers.traefik-secure.tls.domains[0].sans=*.local.{Tu_dominio}"
      - "traefik.http.routers.traefik-secure.service=api@internal"

secrets:
  cf_api_token:
    file: ./cf_api_token.txt

networks:
  proxy:
    external: true"""
     
#######################################################################################################################################################
####################################################################################################################################################### si no no los diferencio
#######################################################################################################################################################
  
  traefik_yml = f"""api:
  dashboard: true
  debug: true
entryPoints:
  http:
    address: ":80"
    http:
      redirections:
        entryPoint:
          to: https
          scheme: https
  https:
    address: ":443"
serversTransport:
  insecureSkipVerify: true
providers:
  docker:
    endpoint: "unix:///var/run/docker.sock"
    exposedByDefault: false
  # file:
  #   filename: /config.yml
certificatesResolvers:
  cloudflare:
    acme:
      email: {Tu_correo}
      storage: acme.json
      # caServer: https://acme-v02.api.letsencrypt.org/directory # prod (default)    # esta comentado mientras pruebo el script para que no me baneen, NO OLVIDAR COMENTAR
      caServer: https://acme-staging-v02.api.letsencrypt.org/directory # staging
      dnsChallenge:
        provider: cloudflare
        #disablePropagationCheck: true # uncomment this if you have issues pulling certificates through cloudflare, By setting this flag to true disables the need to wait for the propagation of the TXT record to all authoritative name servers.
        #delayBeforeCheck: 60s # uncomment along with disablePropagationCheck if needed to ensure the TXT record is ready before verification is attempted 
        resolvers:
          - "1.1.1.1:53"
          - "1.0.0.1:53" """
    
  #comandos que se ejecutaran
  execute('sudo su')
  execute('mkdir docker_volumes && cd docker_volumes')
  execute('mkdir traefik && cd traefik')
  execute('touch docker-compose.yaml')
  with open('docker-compose.yaml', "w", encoding="utf-8") as Docker_archivo: # escribir sobre el archivo
    Docker_archivo.write(Docker_Compose)
  execute('touch cf_api_token.txt')
  with open('cf_api_token.txt', "w", encoding='utf-8') as TOKEN:
    TOKEN.write(Cloudfare_Api)
    execute('touch .env')
  #
  salt = bcrypt.gensalt()
  hash_bcrypt = bcrypt.hashpw(Contraseña_panel.encode(), salt)
  hash_formateado = hash_bcrypt.decode().replace("$", "$$")
  hash_apache = f"{Usuario_panel}:{hash_formateado}"
  with open('.env', "w", encoding="utf-8") as credenciales:
    credenciales.write(f'TRAEFIK_DASHBOARD_CREDENTIALS={hash_apache}')
  # execute(f'echo $(htpasswd -nbB {Usuario_panel} {Contraseña_panel}) | sed -e s/\\$/\\$\\$/g') 
  # basicamente estoy similando el comando de arriba y lo mete en .env, que seria igual a        echo $(htpasswd -nbB usuario contraseña) | sed -e s/\\$/\\$\\$/g'
  execute('mkdir data && cd data')
  execute('rm -f acme.json')
  execute('touch acme.json && chmod 600 acme.json')
  execute('touch traefik.yml')
  with open('traefik.yml', "w", encoding="utf-8") as traefikyml:
    traefikyml.write(traefik_yml)
  execute('docker network create proxy')

  
  
  
  
  #voy por el minuto 20 del video, es decir, me queda todavia hacer el congif.yml
  
  
  
  
  execute('docker compose up -d --force-recreate')
  
  execute('exit')
  
def regreso_al_menu():
  INPUT()
  script()
  
#############
# ejecucion #
#############
execute('sudo apt update && sudo apt upgrade -y')


# COMENTADO PARA PROBAR EN WINDOWS, DESCOMENTAR CUANDO SE FINALICE
# if os.geteuid() != 0:
#   print('ejecuta con permisos sudo por favor')
# else:
#   os.system('sudo apt update && sudo apt upgrade -y')
#   INPUT()
#   script()


INPUT()
script()