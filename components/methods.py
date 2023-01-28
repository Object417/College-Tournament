from dotmap import DotMap

def fillArray(props):
  result = []
  answers = input("\n" + props.message).split(",")
  answers = list(map(lambda val: val.strip(), answers)) # Trim whitespaces
  validation = props.validateAnswer(answers)

  if not validation[0]:
    exit(validation[1])
  
  for index, answer in enumerate(answers):
    obj = DotMap()

    for attribute in props.attributes:
      props.setValue(answer, obj, attribute, index)
    else:
      result.append(obj)
  else:
    return result

def calculateScore(props):
  for event in props.events:
    answers = input(props.message).split(",")
    answers = list(map(lambda val: int(val.strip()), answers)) # Trim whitespaces

    for index, answer in enumerate(answers):
      member = None

      for member2 in props.members:
        if member2.id == answer:
          member = member2
        
      if member == None:
        exit("Error. Cannot find the member by provided ID")
      
      props.setScore(member, index, event)
