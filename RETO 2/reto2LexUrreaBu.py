# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QXz9wxkXyjabI-52Jqt121rFw9EVn2Zx
"""



productos_aseo="XNO"
productos_belleza="UTX"
productos_vendidos="OUXYTU"
productos_belleza_vendidos = 0
productos_aseo_vendidos = 0 

print(productos_aseo)
print(productos_belleza)
print(productos_vendidos)

for productov in productos_vendidos:
  if (productov in productos_aseo):
      productos_aseo_vendidos +=1
  if(productov in productos_belleza):
        productos_belleza_vendidos +=1
    
  if (productos_aseo_vendidos == productos_belleza_vendidos):
        print("E", end="")
  elif (productos_aseo_vendidos > productos_belleza_vendidos):
        print("A", end="")
  elif (productos_aseo_vendidos < productos_belleza_vendidos):
        print("B", end="")