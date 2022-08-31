#!/bin/bash
# Script para ligar os leds do teclado
# ver. 0.001 - primeira versão do script

# Importa modulos do sistema
import os
import getpass

# Solicita a senha sudo para rodar os comandos com elevação
password = getpass.getpass("Digite a senha de super usuário: ")

# Resgata o dispositivo que está associado ao led
commandLed = os.popen("brightnessctl | grep Device | awk '{print $2}' | cut -d ':' -f 1 | cut -c2-")
# Utiliza o rstrip para remover a quebra de linha no final do comando anterior
inputLed = commandLed.read().rstrip('\n')

# Passa a senha sudo, e o device para o comando que liga as luzes do teclado
os.system("echo " + password + " | sudo -S brightnessctl --device='" + inputLed + "::scrolllock' set 1")


