from components.methods import fillArray
from random import randrange
from dotmap import DotMap

MAX_EVENTS = 5
MIN_EVENTS = 1

def validateEvents(events):
  if len(events) == MIN_EVENTS or len(events) == MAX_EVENTS:
    return [True]
  else:
    return [False, f"There must be only {MIN_EVENTS} or {MAX_EVENTS} events"]

def setEventValue(answer, obj, attribute, index: int):
  if attribute == "name":
    obj[attribute] = answer
  elif attribute == "scoreMultiplier":
    obj[attribute] = randrange(1, 5)
  elif attribute == "id":
    obj[attribute] = index

def createEvents():
  return fillArray(DotMap({
    "message": f"Enter {MIN_EVENTS} or {MAX_EVENTS} events' names: ",
    "attributes": ["name", "id", "scoreMultiplier"],
    "validateAnswer": validateEvents,
    "setValue": setEventValue
  }))
