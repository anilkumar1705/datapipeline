# Data Pipeline Task
<h3>The data pipeline task is developed by using the following steps.</h3>
<h4>Step1:</h4>
<text>By using Requests library’s GET method to call  API which is an open source data and ingested the content.
Created panadas data frame by using Pandas library
Imported io library to covert the raw byte data to pandas readable format and decoded by using Utf-8 protocol</text>
<h4>Step2:</h4>
<text>We need to create the sever and database in PGADMIN manually and where we will use the connection string parameters in further data base connections in this data pipeline python libraries psycopg2 and SQLAlchemy</text>
Step3: 
<text>Using psycopg2 library I’ve connected to database with the postgres connection string and created the required table with columns.</text>
<h4>Step 4:</h4>
<text>To load the pandas data frame into the postgres database we need to use the from SQLAlchemy by this we connect to the database using the postgres connection string this will be passed as the database connection engine as argument in to the to_sql  method which loads/appends the data frame into postgres database.</text>
<h4>Step 5:</h4>
<text>To convert the database table into the CSV, I’ve used the psycopg2 database connection to execute the query which we used to create the tables previously.<text>
