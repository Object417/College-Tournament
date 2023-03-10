from modules.clearConsole import clearConsole
from modules.constants import MAX_INDIVIDUALS, MAX_TEAMS, MAX_TEAM_MEMBERS, MIN_EVENTS, MAX_EVENTS
from modules.tools import createList, getMember, mapMember, mapEvent, printMembers

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

# TODO: Could be replaced by universal function
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
      errMsg = f"None or many individuals were found by provided ID: '{individualID}'"

      individual = getMember(individualID, individuals, errMsg)
      individual.score += (MAX_INDIVIDUALS - index) * event.scoreMultiplier
  
  individuals.sort(key = lambda individual: individual.score, reverse = True)
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
  
  teams.sort(key = lambda team: team.score, reverse = True)
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
