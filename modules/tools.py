from dotmap import DotMap
from random  import randrange

# TODO: mapFunc: callableAny could be replaced by more specific one. E. g. callable -> DotMap
def createList(inputMsg: str, errMsg: str, MIN_LEN: int, MAX_LEN: int, mapFunc: callable):
  theList = input(inputMsg).split(",")

  if len(theList) != MIN_LEN and len(theList) != MAX_LEN:
    exit(errMsg)
  else:
    return list(map(mapFunc, enumerate(theList)))

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
