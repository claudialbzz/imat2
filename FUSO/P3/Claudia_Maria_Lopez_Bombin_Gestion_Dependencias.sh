#!/bin/bash

# Creamos el entorno 3.12
mkdir -p env312
python3.12 -m venv env312
source env312/bin/activate

# Instalamso los paquetes de requirements4_1.txt
pip install -r requirements4_1.txt

# Ejecutamos plot_color_quantization.py
pyton3.12 plot_color_quantization.py > logColor.txt

# DEsactivamos el entorno
deactivate

# Creamos el entorno 3.11
mkdir -p env311
python3.11 -m venv env311
source env311/bin/activate

# Instlamos los paquetes de requirements4_2.txt
pip install -r requirements4_2.txt

# Ejecutamos plot_face_recognition.py
python3.11 plot_face_recognition.py

# DEsactivamos entorno
deactivate

#Eliminamos los directorios de los entornos
rm -r env312 && rm -r env311

# Hacemos un ls para confirmar que se han eliminado correctamente
ls

# Fin del script
