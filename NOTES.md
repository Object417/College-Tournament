# Notes

## Process flow (pseudocode)

### Individuals mode

```text
> Do you want to calculate score for individuals or teams?
< individuals

props.message: String
props.attributes: Array
props.setValue: Function

function fillArray(props){
  > props.message
  < Jack, Mike, Oleh, Kate, John, Alex, David, Pal, Andrey, Susan, etc.

  const arr
  const answers = "Jack, Mike, Oleh, Kate".split(", ")

  answers.forEach(answer => {
    const obj = {}
    props.attributes.forEach(attribute => {
      props.setValue(answer, obj, attribute)
    })
    arr.push(obj)
  })

  return arr
}

individuals = [
  { name: "Jack", score: 0, ID: 0 },
  { name: "Mike", score: 0, ID: 1 }, etc.
]


> individuals
```

```text
props.message: String
props.events: Array
props.members: Array
props.setScore: Function

function calculateScore(props) {
  events.forEach(event => {
    > props.message
    < 5, 9, 3, 4, 1, 2, 8, 7, 0, 6

    answers = "5, 9, 3, 4, etc.".split(", ")
    answers.forEach(id => {
      get member from members by id

      setScore(member, event)
    })
  })

}
```

```text
> Enter all the events
< Football, basketball, 30m, Line swimming, Chess

events = [
  { name: "Football", scoreMultiplier: Math.random(), ID: 0 },
  { name: "basketball", scoreMultiplier: Math.random(), ID: 1 }, etc.
]

> events

for event of events:
  > Enter individuals' IDs in the order of taken place (ascending)
  < 5, 9, 3, 4, 1, 2, 8, 7, 0, 6

  for each (id, index):
    get individual by id
    set individual.score += (20 - index) * event.scoreMultiplier

> individuals

end
```

### Teams mode

```text
< teams

teams = fillArray()

> teams

for each team of teams:
team.members = fillArray()

> teams

events = fillArray()

> events

calculateScore()

> teams

end
```

### Functions

```js
fillArray(props)
props.message // message that will be shown when asking user to enter the data
props.attributes = [
  { name: "attributeName", value: "defaultValue" || "indexValue" }
]

calculateScore(props)
props.source // array with objects where data should be put
props.attributeName // attribute where data should be put
props.scoreMultiplier // event.scoreMultiplier
```
