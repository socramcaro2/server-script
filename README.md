# ¿Qué es?

Este es un script hecho en python solamente que sirve para automatizar las descargas de algunos servicios.

Importante recalcar que para la correcta ejecucion se deberia ejecutar como sudo.

Esta principalmente orientado a ser usado en entorno de servidores tipo home lab, y deja margen de maniobra para que selecciones versiones o ingreses keys o lo necesario segun lo que se seleccione dentro del script

```xml
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
```

## Tailscale

El script de Tailscale utiliza el oficial suyo, de su link, lo unico que si quieres puedes especificar la key, no es necesario ya que te pediria que inicies sesion en una url que especifica el propio script oficial para añadir el dispositivo a tu red

## Docker

Me he basado en la documentacion que tiene racher sobre su instalacion de Docker limipia y de ahi rasuq el script oficial sh de docker ademas de automaticamente permitir que el usuario pueda utilizarlo como rootless

## Portainer


## Traefik (sin acabar)
 
Este script para instalar Traefik con docker me base en la guía de [TechnoTim para traefik 3](https://technotim.live/posts/traefik-3-docker-certificates/), simplemente sigo los pasos que indica la guia y dejo seleccionar algunos aspectos para que la instalacion sea tuya propia.


## Futuro

Por el momento no tengo nada en mente para seguir añadiendo, simplemente ir acabado y puliendolo, segun vaya necesitando mas cosas las ire añadiendo o si me las piden