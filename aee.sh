#!/bin/bash

# Ejecuta aee.py con argumentos si se pasan, o lee desde stdin
if [ $# -eq 2 ]; then
    python3 aee.py "$1" "$2"
else
    python3 aee.py
fi