# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W8wT538yeOPlPA5FZWPco4ffgYiD3X9e
"""

import ast
actividades = input()
convert_acti = ast.literal_eval(actividades)
seleccion = input().split(" ")

contador = 0
lista_select = ""

for key in seleccion:
    if key in convert_acti.keys():
      lista_select += key+" "
      contador += convert_acti[key] 

print(contador) 
print(lista_select, end=" ")