#!/usr/bin/env python3

from os import system
from time import sleep

# import serial

print("Iniciando compilacao...")


# Table of Operations and Hex Codes

operations = {
    "zeroL":    "0",
    "umL":      "1",
    "An":       "2",
    "Bn":       "3",
    "AouB":     "4",
    "AeB":      "5",
    "AxorB":    "6",
    "AnandB":   "7",
    "AnorB":    "8",
    "AxnorB":   "9",
    "AnouB":    "a",
    "AouBn":    "b",
    "AneB":     "c",
    "AeBn":     "d",
    "AnouBn":   "e",
    "AneBn":    "f",
}

operations = {key.lower(): value for key, value in operations.items()}


print("Lendo codigo-fonte .ula...")


# Openning the source code file
with open("testeula.ula", "r") as file:
    sourceCode = file.read().lower()


# Removing indentation and the delimiters
sourceCode = sourceCode.replace('\n', '')
sourceCode = sourceCode.replace("inicio:", '')
sourceCode = sourceCode.replace("fim.", '')


commands = sourceCode.split(';')
commands.remove('')


arduinoCommands = []


print("Processando o codigo...")


for cmd in commands:
    # Testing whether the command is an assingment
    if cmd.find('=') != -1:
        cmd = cmd.split('=')
        if cmd[0] == 'a':
            a = cmd[1]
        if cmd[0] == 'b':
            b = cmd[1]
        continue

    arduinoCommands.append(a + b + operations[cmd])


print("Gerando arquivo .hex para o arduino...")

with open("testeula.hex", "w") as file:
    for arduCmd in arduinoCommands:
        file.write(arduCmd + '\n')
    file.close()

port = "com6"
baud_rate = 9600


print("Conectando a porta serial {0} a {1} bps...".format(port, baud_rate))
# comport = serial.Serial(port[-1:], baud_rate)

sleep(1.8)


print("Enviando o .hex para o Arduino...\n")


with open("testeula.hex", "r") as file:
    arduinoSend = file.read()
    file.close()


arduinoSend = arduinoSend.split('\n')
arduinoSend.remove('')


for arduCmd in arduinoSend:
    print(arduCmd, "(enter) ", end="")
    input()
    print("envia.exe", port, ' '.join(arduCmd))
    # Comunicacao serial direta
    # comport.write(arduCmd)
