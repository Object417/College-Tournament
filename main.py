from modules.clearConsole import clearConsole
from dotmap import DotMap
from random  import randrange

# Constants2
MAX_INDIVIDUALS = 5
MIN_EVENTS = 1
MAX_EVENTS = 5
MAX_TEAMS = 4
MAX_TEAM_MEMBERS = 5

# Create functions
def createList(inputMessage, validator, mapFunc):
  list = input(inputMessage).split(",")

  validationResult = validator(list)
  if not validationResult[0]:
    exit(validationResult[1])
  else:
    return list(map(mapFunc, list))

def createEvents():
  inputMessage = f"\nEnter {MIN_EVENTS} or {MAX_EVENTS} events: "

  def validator(events):
    errMessage = f"There must be only {MIN_EVENTS} or {MAX_EVENTS} but got {len(events)}"

    if len(events) != MIN_EVENTS or len(events) != MAX_EVENTS:
      return [False, errMessage]
    else:
      return [True]
  
  def mapFunc(indexAndName):
    return DotMap({
      "id": indexAndName[0],
      "name": indexAndName[1].strip(),
      "scoreMultiplier": randrange(1, 5)
  })

  return createList(inputMessage, validator, mapFunc)

def createIndividuals():
  inputMessage = f"\nEnter {MAX_INDIVIDUALS} individuals' names: "

  def validator(individuals):
    errMessage = f"There must be {MAX_INDIVIDUALS} individuals but got {len(individuals)}"

    if len(individuals) != MAX_INDIVIDUALS:
      return [False, errMessage]
    else:
      return [True]
  
  def mapFunc(indexAndName):
    return DotMap({
      "id": indexAndName[0],
      "name": indexAndName[1].strip(),
      "score": 0
    })
  
  return createList(inputMessage, validator, mapFunc)

def createTeams():
  inputMessage = f"\nEnter {MAX_TEAMS} teams' names: "
  
  def validator(teams):
    errMessage = f"There must be {MAX_TEAMS} teams but got {len(teams)}"

    if len(teams) != MAX_TEAMS:
      return [False, errMessage]
    else:
      return [True]
  
  def mapFunc(indexAndName):
    return DotMap({
      "id": indexAndName[0],
      "name": indexAndName[1].strip(),
      "score": 0
    })
  
  teams = createList(inputMessage, validator, mapFunc)
  for team in teams:
    inputMessage = f"Enter {MAX_TEAM_MEMBERS} members' names of team '{team.name}': "

    def validator(members):
      errMessage = f"Each team must have {MAX_TEAM_MEMBERS} members but got {len(members)}"

      if len(members) != MAX_TEAM_MEMBERS:
        return [False, errMessage]
      else:
        return [True]
    
    def mapFunc(indexAndName):
      return indexAndName[1].strip()

    team.members = createList(inputMessage, validator, mapFunc)
  else:
    return teams

def createTakenPlaces(inputMessage, constant):
  takenPlaces = input(inputMessage).split(",")

  if len(takenPlaces) != constant:
    exit(f"There must be {constant} IDs provided but got {len(takenPlaces)}")
  else:
    return list(map(lambda memberID: int(memberID), takenPlaces))

# Get functions
def getMember(memberID, members, errMessage):
  foundMember = [member for member in members if member.id == memberID]

  if len(foundMember) != 1:
    exit(errMessage)
  else:
    return foundMember[0]

# Calculate functions
def calcIndividuals():
  individuals = createIndividuals()

  print("\nIndividuals:")
  for individual in individuals:
    print(f"ID: {individual.id}, {individual.name} ({individual.score})")

  events = createEvents()

  print("\nEvents:")
  for event in events:
    print(f"ID: {event.id}, {event.name} ({event.scoreMultiplier})")
  
  print("\nTaken places:")
  for event in events:
    inputMessage = f"Enter individuals' IDs in the order of taken place in '{event.name}': "
    takenPlaces = createTakenPlaces(inputMessage, MAX_INDIVIDUALS)

    for index, individualID in enumerate(takenPlaces):
      errMessage = f"None or many individuals were found by provided ID: {individualID}"
      individual = getMember(individualID, individuals, errMessage)
      individual.score += (MAX_INDIVIDUALS - index) * event.scoreMultiplier
  
  individuals.sort(key=lambda individual: individual.score, reverse=True)

  print("\nScoreboard:")
  for individual in individuals:
    print(f"ID: {individual.id}, {individual.name} ({individual.score})")
  
def calcTeams():
  teams = createTeams()

  print("\nTeams")
  for team in teams:
    print(f"ID: {team.id}, {team.name} ({', '.join(team.members)})")
  
  events = createEvents()

  print("\nEvents:")
  for event in events:
    print(f"ID: {event.id}, {event.name} ({event.scoreMultiplier})")
  
  for event in events:
    message = f"Enter teams' IDs in the order of taken place in '{event.name}': "
    takenPlaces = createTakenPlaces(message, MAX_TEAMS)

    for index, teamID in enumerate(takenPlaces):
      errMessage = f"None or many teams were found by provided ID: {teamID}"
      team = getMember(teamID, teams, errMessage)
      team.score += (MAX_TEAMS - index) * event.scoreMultiplier
  
  teams.sort(key=lambda team: team.score, reverse=True)

  print("\nScoreboard")
  for team in teams:
    print(f"ID: {team.id}, {team.name} ({team.score})")

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
