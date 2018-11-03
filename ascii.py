#!/usr/bin/python
import sys

ascii_chars = ' abcdefghijklmnopqrstuvwxyz'
count = 97
ascii_table = []
for letter in ascii_chars:
  values = {'char':letter,'dec':'','hex':''}
  if(letter == ' '):
    values['char'] = 'SPACE'
    values['dec'] = 32
  else: 
    values['dec'] = count
    count+=1
  values['hex'] = hex(values['dec'])[2:]
  ascii_table.append(values)  

def stringToHex(msg):
  hexmessage = ''
  for letter in msg:
    if(letter == ' '):
      letter = 'SPACE'
    ascii_position = 0
    while (ascii_position < len(ascii_table)):
      if(ascii_table[ascii_position]['char'] == letter):
        hexmessage += '\\x%s' %ascii_table[ascii_position]['hex']
      ascii_position += 1
  return hexmessage
if (len(sys.argv) == 2):
  print(stringToHex("%s" %sys.argv[1].lower()))
else:
  print('Parametros incorretos!')
  print('Modo de usar: ./ascii.py "mensagem"')
#print(stringToHex(input("Digite a mensagem que voce quer... ")))
