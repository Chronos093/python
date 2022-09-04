#!/bin/bash
# Script para ligar os leds do teclado
# ver. 0.01 - primeira versão do script
# ver. 0.02 - adiciona condição para ligar e desligar o led, e renomeado o nome do arquivo para main

# Importa modulos do sistema
import os
import getpass

# Função para ligar as luzes
def functionUp():
# Solicita a senha sudo para rodar os comandos com elevação
    password = getpass.getpass("Digite a senha de super usuário: ")

# Resgata o dispositivo que está associado ao led
    commandLed = os.popen("brightnessctl | grep Device | awk '{print $2}' | cut -d ':' -f 1 | cut -c2-")
# Utiliza o rstrip para remover a quebra de linha no final do comando anterior
    inputLed = commandLed.read().rstrip('\n')

# Passa a senha sudo, e o device para o comando que liga as luzes do teclado
    os.system("echo " + password + " | sudo -S brightnessctl --device='" + inputLed + "::scrolllock' set 1")


# Função para desligar as luzes
def functionDown():
# Solicita a senha sudo para rodar os comandos com elevação
    password = getpass.getpass("Digite a senha de super usuário: ")

# Resgata o dispositivo que está associado ao led
    commandLed = os.popen("brightnessctl | grep Device | awk '{print $2}' | cut -d ':' -f 1 | cut -c2-")
# Utiliza o rstrip para remover a quebra de linha no final do comando anterior
    inputLed = commandLed.read().rstrip('\n')

# Passa a senha sudo, e o device para o comando que desliga as luzes do teclado
    os.system("echo " + password + " | sudo -S brightnessctl --device='" + inputLed + "::scrolllock' set 0")    


def default():
    print("Erro ao consultar o estado do led.")

def switch(case):
    if case == "0":
        return functionUp
    elif case == "1":
        return functionDown
    else:
        return default


if __name__ == "__main__":
    cond = os.popen("sudo brightnessctl --device 'input9::scrolllock' get").read().rstrip('\n')
    
    function = switch(case=cond)
    function()