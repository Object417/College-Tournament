from components.methods import fillArray, calculateScore
from components.events import createEvents
from dotmap import DotMap

MAX_INDIVIDUALS = 5

def validateIndividuals(individuals):
  if len(individuals) == MAX_INDIVIDUALS:
    return [True]
  else:
    return [False, f"There must be {MAX_INDIVIDUALS} individuals"]

def setIndividualValue(answer, obj, attribute, index: int):
  if attribute == "name":
    obj[attribute] = answer
  elif attribute == "score":
    obj[attribute] = 0
  elif attribute == "id":
    obj[attribute] = index

def setIndividualScore(individual, index: int, event):
  individual.score += (MAX_INDIVIDUALS - index) * event.scoreMultiplier

def calcIndividuals():
  individuals = fillArray(DotMap({
    "message": f"Enter all the {MAX_INDIVIDUALS} individuals' names: ",
    "attributes": ["name", "id", "score"],
    "validateAnswer": validateIndividuals,
    "setValue": setIndividualValue
  }))

  print("Individuals:")
  for individual in individuals:
    print(f"ID: {individual.id}, {individual.name} {individual.score}")
  
  events = createEvents()

  print("Events:")
  for event in events:
    print(f"ID: {event.id}, {event.name} {event.scoreMultiplier}")
  
  calculateScore(DotMap({
    "message": "Enter the individuals' IDs in the order of taken place (1, 2, 3, etc.)",
    "members": individuals,
    "events": events,
    "setScore": setIndividualScore
  }))

  print("Scoreboard")
  for individual in individuals:
    print(f"ID: {individual.id}, {individual.name}, {individual.score}")
