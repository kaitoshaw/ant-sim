# Ant Simulation Program

In this repository, the files used for the plotting based on the ants intelligence is located in intelligenceLevels folder. Inside the folder, there are three files named after each intelligence level. It will give you the visualisation of how the ants work gather the food back to their base based on their intelligence Level


## Intelligence Levels

The intelligence level of the ants are differentiated into three levels: 0, 1, and 2. 

- Intelligence 0 means that the ants have no Pheromone skill and Chemosense to help them gathering the food
- Intelligence 1 means that the ants have Chemosense to sense nearby food and have the idea of the food location. However, they are not sharing the food location information to the ants within the same colony
- Intelligence 2 means that the ants have both Pheromone, a skill to leave trails to make other ants know where to get the food, and the Chemosense to sense the nearby food.

## Running Program Guide

To run this program, you can install the files in zip or clone the repository. To run the ant simulation, you can run the python files inside intelligenceLevel Folder by running either of these commands.
- `python ../intelligenceLevel/intelligence_0.py`
- `python ../intelligenceLevel/intelligence_1.py`
- `python ../intelligenceLevel/intelligence_2.py`
<br><br>
### Other files that may be relevant
- `main.ipynb` is the file that manually stores the versioning of the code inside a jupyter notebook file
- `ant_main.py` is the file to modify the newest code development. 

**Note: however, I was experiencing a github bug where I lost a week worth of project upon the last commit. So both main.ipynb and ant_main.py are not updated**
