# Atttendence-System using flask framework and openCV library in python language.

# frontend web technology used
HTML, CSS, JAVASCRIPT, JQUERY, BOOTSTRAP FRAMEWORK

# Backend Technology
Python language, flask web framework

# Libraries used
os, flask, opencv, numpy etc.

# How to use database
install xampp software and start apache and mysql
<<<create a database and import .sql file
<<<now create a db_connection
hostname=localhost, username=root, password=none ,db_name=your_db_name
and run app.py file.
change url and add /add path on main url
fill a sample form 
on submitting form data will upload in the database

# How to test the recognizer
Step 1. **'dataset'** folder must exist in your working directory. Here all sample images will be stored. <br>
Step 2. Run the file **datasetcapture.py**. For each person, this file has to be run again and it will create folder containing 50 sample images of a person stored id-wise in folder 'dataset'. <br>
Step 3. Run **train.py** to train and save the recognizer. <br>
Step 4. Run **recognize.py** for recognizing the person and displaying the id number

