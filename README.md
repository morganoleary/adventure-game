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

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
