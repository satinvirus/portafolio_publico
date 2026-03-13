#!/bin/bash
# Script de alerta en Bash

ROJO='\033[0;31m'
SIN_COLOR='\033[0m'

echo -e "${ROJO}####################################"
echo -e "#     ¡ALERTA DE SISTEMA CRÍTICA!   #"
echo -e "# EL USO DE CPU HA SUPERADO EL 80%  #"
echo -e "####################################${SIN_COLOR}"

# Aquí podrías agregar comandos reales, como:
# df -h >> log_de_error.txt (para ver espacio en disco)