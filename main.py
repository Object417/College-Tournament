from dotmap import DotMap
from random  import randrange
from modules.clearConsole import clearConsole
from modules.constants import *

# Create functions
# TODO: mapFunc: callableAny could be replaced by more specific one. E. g. callable -> DotMap
def createList(inputMsg: str, errMsg: str, MIN_LEN: int, MAX_LEN: int, mapFunc: callable):
  theList = input(inputMsg).split(",")

  if len(theList) != MIN_LEN and len(theList) != MAX_LEN:
    exit(errMsg)
  else:
    return list(map(mapFunc, enumerate(theList)))

# TODO: Could be replaced by universal function
def createIndividuals():
  inputMsg = f"\nEnter {MAX_INDIVIDUALS} individuals' names: "
  errMsg = f"There must be {MAX_INDIVIDUALS} individuals"

  return createList(inputMsg, errMsg, MAX_INDIVIDUALS, MAX_INDIVIDUALS, mapMember)

def createTeams():
  inputMsg = f"\nEnter {MAX_TEAMS} teams' names: "
  errMsg = f"There must be {MAX_TEAMS} teams"

  teams = createList(inputMsg, errMsg, MAX_TEAMS, MAX_TEAMS, mapMember)

  for team in teams:
    inputMsg = f"Enter {MAX_TEAM_MEMBERS} members' names of team '{team.name}': "
    errMsg = f"There must be {MAX_TEAM_MEMBERS} members in each team"
    mapFunc = lambda indexAndName: indexAndName[1].strip()

    team.members = createList(inputMsg, errMsg, MAX_TEAM_MEMBERS, MAX_TEAM_MEMBERS, mapFunc)
  
  return teams

def createEvents():
  inputMsg = f"\nEnter {MIN_EVENTS} or {MAX_EVENTS} events: "
  errMsg = f"There must be only {MIN_EVENTS} or {MAX_EVENTS}"

  return createList(inputMsg, errMsg, MIN_EVENTS, MAX_EVENTS, mapEvent)

def getMember(memberID: int, members: list, errMsg: str) -> DotMap:
  foundMember = [member for member in members if member.id == memberID]
  return foundMember[0] if len(foundMember) == 1 else exit(errMsg)

# TODO: Replace by universal function with a flag
def mapMember(indexAndName: tuple):
  return DotMap({
    "id": indexAndName[0],
    "name": indexAndName[1].strip(),
    "score": 0
})

def mapEvent(indexAndName: tuple):
  return DotMap({
    "id": indexAndName[0],
    "name": indexAndName[1].strip(),
    "scoreMultiplier": randrange(1, 5)
  })

def printMembers(title: str, members: list, showScore: bool = False):
  print(title)
  for member in members:
    memberMembers = f"({', '.join(member.members)}) " if member.members else ""
    memberScore = f"({member.score or member.scoreMultiplier})" if showScore else ""

    print(f"ID: {member.id}, {member.name} {memberMembers}{memberScore}")

# TODO: Replace by universal function
def calcIndividuals():
  individuals = createIndividuals()
  printMembers("\nIndividuals:", individuals)

  events = createEvents()  
  printMembers("\nEvents:", events)
  
  print("\nTaken places:")
  for event in events:
    inputMsg = f"Enter individuals' IDs in the order of taken place in '{event.name}': "
    errMsg = f"There must be {MAX_INDIVIDUALS} IDs provided"
    mapFunc = lambda indexAndID: int(indexAndID[1])

    takenPlaces = createList(inputMsg, errMsg, MAX_INDIVIDUALS, MAX_INDIVIDUALS, mapFunc)

    for index, individualID in enumerate(takenPlaces):
      errMsg = f"None or many individuals were found by provided ID: \"{individualID}\""

      individual = getMember(individualID, individuals, errMsg)
      individual.score += (MAX_INDIVIDUALS - index) * event.scoreMultiplier
  
  individuals.sort(key=lambda individual: individual.score, reverse=True)
  printMembers("\nScoreboard:", individuals, True)
  
def calcTeams():
  teams = createTeams()
  printMembers("\nTeams:", teams)
  
  events = createEvents()
  printMembers("\nEvents:", events)
  
  print("\nTaken places:")
  for event in events:
    inputMsg = f"Enter teams' IDs in the order of taken place in '{event.name}': "
    errMsg = f"There must be {MAX_TEAMS} IDs provided"
    mapFunc = lambda indexAndID: int(indexAndID[1])

    takenPlaces = createList(inputMsg, errMsg, MAX_TEAMS, MAX_TEAMS, mapFunc)

    for index, teamID in enumerate(takenPlaces):
      errMsg = f"None or many teams were found by provided ID: '{teamID}'"

      team = getMember(teamID, teams, errMsg)
      team.score += (MAX_TEAMS - index) * event.scoreMultiplier
  
  teams.sort(key=lambda team: team.score, reverse=True)
  printMembers("\nScoreboard:", teams, True)

# main
def main():
  clearConsole()

  inputMessage = "Do you want to calculate the score for individuals or teams? "
  mode = input(inputMessage).lower().strip()

  if mode == "individuals":
    calcIndividuals()
  elif mode == "teams":
    calcTeams()
  else:
    exit(f"Invalid input. Expected 'individuals' or 'teams' but got {mode}")

if __name__ == "__main__":
  main()
