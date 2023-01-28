from os import system, name
from components.individuals import calcIndividuals

# from random import uniform
# print(uniform(1, 5))

def clearConsole():
  system("cls" if name == "nt" else "clear")

def main():
  clearConsole()
  print("Welcome")
  mode = input("Do you want to calculate score for teams or individuals? ")

  if mode == "individuals":
    calcIndividuals()
  elif mode == "teams":
    pass
  else:
    exit("Error: invalid input")

if __name__ == "__main__":
  main()

