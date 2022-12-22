from os import name, system

def clearConsole():
  system("cls" if name == "nt" else "clear")
