# Adventure Game

Welcome to my adventure game!
This game is designed to create an enjoyable, option-based, adventure and allow users to choose their own path to see if they can get the highest score!

## User Stories
- As a player, I want to be able to see clear rules for the game in order to know the objectives.
- As a player, I want to be able to create my character name at the beginning of the game, that will take me through the adventure.
- As a player, I want to be able to choose my beginning location for the adventure game, Mars or Earth.
- As a player, I want to have a story-driven experience that will take me to new places depending on my choices throughout the game.
- As a player, I want clear descriptions of surroundings and other characters to better immerse myself into the adventure.
- As a player, I want the game to have multiple possible outcomes based on my choices throughout the adventure.
- As a player, I want to be able to pause the game and save my progress to come back to later. 
- As a player, I want to be able to pick up my previous game and begin from the paused point.
- As a player, I want a clear way to be able to exit the game and restart the adventure.
- As a player, I want to be able to see my score tally, depending on my choices, and how far in the game I made it compared to other players.

### Flowchart for story line:
![Lucidchart Diagram](.devcontainer/assets/readme-images/game-flowchart.png)

## Features

- TBD

## Bugs & Errors

- Commit #80f00d8 was meant to read as follows: "Add functions to story  when user chooses earth"
    - I accidentally pushed the commit without realizing my error of stating "mars" again so I researched on how to change a previous commit message. 
    - I used Slack and this [GitHub Doc](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/changing-a-commit-message) to try to amend the issue with "git rebase -i HEAD~n". This became increasingly confusing.
    - Tutor support was contacted and advised that -'Having an incorrect message is a much smaller problem than trying to change your commit.'- and everything should be working normally, but that Codeanywhere seemed to have a glitch as I wasn't able to save new updates and use the advised "git push --force" command. I was then told to create a new workspace and I was up and running again. 
    - I was not able to rename the commit message and was advised to add a note to my README file.
- While creating the exceptions throughout the story, depending on user input, I began using if/elif/else statements inside while True: loops. This was causing the 'else' statement to print indefinitely as the while loop did not have an end point.
    - I implemented try and except statements within my while loops so that the loop could be exited.

## Testing

## Deployment

## Credits

- The Love Sandwiches walkthrough "Getting Set Up" videos were used to import gspread and google.auth dependencies in order to access the Google Sheet API. The SCOPE was also used from Love Sandwiches.
- The overal concept of how to start an adventure game came from watching [this text-based adventure game YouTube video tutorial](https://www.youtube.com/watch?v=ORsJn-71__0)
- When implementing exception handling, the following resources were used for understanding:
    - [Exception & Error Handling in Python](https://www.datacamp.com/tutorial/exception-handling-python)
    - [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#Exception)
- Python styling guidance was from [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/)
