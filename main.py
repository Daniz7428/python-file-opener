#python3 -m pip install invoke
#invoke build-cmult

"""class compileCppPrograms:
   print("Put the program name --> ")
   programToOpen = input()
   program = open(programToOpen,"r")
   readedProgram = programToOpen.read()
   print"""
  
import os

print("Atraves de este python ejecuto programas ejecutables hechos con c++")
print("elige un archivo")
archivo = input()
comando = "./" + archivo
os.system(comando)