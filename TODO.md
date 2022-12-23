# To Do

- `calcIndividuals` and `calcTeams` do the same, so can be replaced by universal function
- `mapMember` and `mapEvent` do the same, so can be replaced by universal function with a flag
- `MIN_LEN` argument should be optional
- `create(Individuals|Teams|Events)` do almost the same, so could be replaced by universal function

## Notes

- I think the code is pretty good now and does not need extra optimization
  because it will likely hurt readability.

## Requirements

- ~~Participants may enter the tournament as individuals or as part of a team.~~
- ~~It is expected that will be 4 teams each with 5 members~~
  ~~and there will be 20 spaces for individual competitors.~~
- ~~Each team or individual will complete 5 events.~~

- Each event will be defined as a team or individual event.

  > Events are created after selecting individuals/teams.

- The events will vary in type, from sporting to academic challenges.

  > The user is able to name events as he wants but all events are same
  > and have random score multiplier.

- ~~Individuals and teams will be awarded points according to their rank within each event.~~
- ~~The points awarded for each event are yet undecided~~
  ~~and the college are willing to hear any suggestions you may have.~~
- ~~Also, the college would like to include the possibility of entering for one event only.~~
