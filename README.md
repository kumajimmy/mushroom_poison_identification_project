Made by Master’s students in spring 2024 DSCI551 (Foundations of Data Management):<br>
Allison Chan<br>
Brandyn K. Lee <br>
Eric Crouse <br>

To view streamlit deployment, please visit: https://mushroom-poison-identification.streamlit.app/ <br>

## To run this project:
1. Clone this repository.
2. Create virtual environment for project and activate it.
3. From the cloned repository directory, install the required dependencies found in requirements.txt using “pip3 install -r requirements.txt”
4. Create new project on Firebase console. Under the “Build” drop-down menu, select “Realtime Database.”
5. On the Firebase console, go to the “Rules” tab under the Realtime Database created in step 4. Edit all “false” values to “true" and click “Publish.” 
6. Go tthe “Data” tab and click on the icon with three vertical dots and select “IMPORT JSON.”  Select the "mushroom-default-rtdb-import.json” from the cloned repository.
7. Create 8 additional databases within the same project (only available with Blaze plan) and change the rules of each to below and publish:
```json
{
  "rules": {
    ".read": true,
    ".write": true,
    ".indexOn": ["bruises", "cap-color", "cap-shape", "cap-surface", "gill-attachment", "gill-color", "gill-size", "gill-spacing", "habitat", "odor", "poisonous", "population", "ring-number", "ring-type", "spore-print-color", "stalk-color-above-ring", "stalk-color-below-ring", "stalk-root", "stalk-shape", "stalk-surface-above-ring", "stalk-surface-below-ring", "veil-color", "veil-type"]
  }
}
```
8. In the cloned repository, create a file named config.py and add your default firebase reference URL as “firebase_url = “default_reference/.json” 
<tb><tb><tb>Also in the config.py file, create a dictionary named “DATABASE_URLS”  with the key as the number starting from 0 (ie, 0-7) and the values as the reference URLs for the databases created in step 7.
9. From the cloned repository direcotry as the root and virtual environment activated, from the command line, run “python3 distribute_data.py”; this will populate the databases created in step 7 via a hashing function and requests library utilizing the Firebase REST API. Check Firebase console to confirm population.
10. Push repository to github to deploy on streamlit. Make sure your have an account on Steamlit, and it is connected to pushed github. 


#### Files Included:
1. final_project.py<br>
  This is where the streamlit website is being displayed. 
2. database_backend_mushroom.py<br>
  This file is used by the database manager to run CRUD operations.
3. distribute_data.py<br>
  This file is used for the initial upload of our data to our databases. 
4. mushroom-default-rtdb-import.json<br>
  This file is used in step 6 of how to run this project providing key mapping information for attributes names and values.
5. requirements.txt<br>
  This file is used to install necessary depenedencies to run project in virtual environment.

#### Files to be created if trying to reproduce project:
1. config.py<br>
  This file is created in step 8 and contains the default firebase_url and the 8 additional firebase reference locations.


##### Front End:
Streamlit: In order to view content of final_project.py, please visit https://mushroom-identification.streamlit.app/.

##### Data Base Manager:
1. From the cloned repository directory as the root with the virtual environment actiivated, from the command line, run “python3 database_backend_mushroom.py”
2. Please follow instructions shown in command line terminal to run CRUD operations.


## Contributions:
Brandyn K. Lee
- Wrote the hashing function to distribute data and populate to Firebase databases. Wrote the backend database management python script. Created data visualizations in Plotly. Helped write code for load_df() in front end to more effectively pull initially filtered data (ie, pull only requested data not the entire database); debugged all load_df() issues and fixed all logic to properly load requested data.

Allison
- Worked on obtaining the initial data to be used for this project. Helped with discussing and determining the database to be used, along with strategies on distributing the data. Then helped create and set up the database to be used for when the data is loaded. Set up the front end visualization and interactive components of the streamlit website. Additionally helped debug data cleaning, data loading, and visuals.

Eric
- Along with Brandyn, analyzed and cleaned/preprocessed data, selected an appropriate
database system, and developed code for database population. Created and hosted a key for mapping the single-character values our dataset to their corresponding English words (e.g. ‘n’→’brown’); this can be found on Firebase as well as a json file named “mushroom-default-rtdb-import.json” in the repo. Also designed and implemented the percentage graphic which efficiently calculates intermediate percentage of a mushroom being poisonous/edible after each user-click and displays the final result once edibility is definitively determined.
