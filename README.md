# AS-Level-Capstone-Project
Text-based Keyword Question maker for AS and A Level Computer Science key terms and their corresponding definitions\
[Checkpoints](https://github.com/202248SD/AS-Level-Capstone-Project/tree/main/checkpoints) refers to all of the saves i've made whilst working on my project.\
[Keyword Question Maker](https://github.com/202248SD/AS-Level-Capstone-Project/tree/main/Keyword%20Question%20maker) contains all of the necessary files for the finished project.\

## Features
[Glossary](https://github.com/202248SD/AS-Level-Capstone-Project/blob/main/Keyword%20Question%20maker/Glossary.tsv) contains all of the keywords and definitions, as well as their topic name/number\
[Highscore](https://github.com/202248SD/AS-Level-Capstone-Project/blob/main/Keyword%20Question%20maker/HighScore.txt) contains a single integer value representing the highest score achieved\
[functions](https://github.com/202248SD/AS-Level-Capstone-Project/blob/main/Keyword%20Question%20maker/functions.py) and [modules](https://github.com/202248SD/AS-Level-Capstone-Project/blob/main/Keyword%20Question%20maker/modules.py) contains the modules and functions used for the project\
[main](https://github.com/202248SD/AS-Level-Capstone-Project/blob/main/Keyword%20Question%20maker/main.py) is the main file for running the project\
[users](https://github.com/202248SD/AS-Level-Capstone-Project/blob/main/Keyword%20Question%20maker/users.tsv) contains the username and their password (hashed with sha256) for all of the registered users, as well as their personal best score. The column mistakes contains the question ID for all of the questions the user had gotten wrong, which is used to increase the weight of a question, so that questions that a user had gotten wrong is more likely to come up again.\

## Download
Download all of the files in [AS-Level-Capstone-Project/Keyword Question maker/](https://github.com/202248SD/AS-Level-Capstone-Project/tree/main/Keyword%20Question%20maker)\
You can either do this by downloading each individual file in the folder or using a community tool (eg. [Download Directory](https://download-directory.github.io/))\
Install all required packages (numpy, pandas) (random, csv & hashlib are all from the Python Standard Library)\
