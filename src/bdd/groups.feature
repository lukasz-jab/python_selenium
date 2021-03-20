Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header> and <footer>
  When I add a group to the list
  Then a new group list is equal to the old list with added a new group

  Examples:
  | name   | header   | footer   |
  | name1  | header1  | footer   |
  | #name? | @header> | !footer/ |
