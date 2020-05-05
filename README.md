# Continue watching with Cortana
A script that will check the last episode of the chosen show from your computer and open the new episode just by talking with cortana.

How does it work?

First, you create a string list with the names of your TV shows that is inside a chosen folder. Then batCreator.py script creates the necessary .bat files for Cortana to execute when given the command such as "Hey Cortana, Launch Seinfeld". Script creates .bat files with the shows' name and puts them in the "Programs" folder where Cortana can locate and execute them.
main.py script checks the recently played files from Media Player Classic program and if it founds an episode of the show, it plays the next episode from the folder.
If it cannot find from media player classic, it checks whether there is a .txt files that saved the latest watched episode.
Else all fails it starts the first episode of the chosen show.
