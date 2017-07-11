Machine Nanodegree Program

Capstone Project Data.

The following text file explains how to obtain the data for the nanodegree project. The project's goal is to predict the time a patient is hospitalized based on the BMI (body mass index) and other additional features extracted from the medical "obesity paradox" previous studies.

We will use the MIMIC-III database to extract the project dataset. The MIMIC-III (‘Medical Information Mart for Intensive Care’) is a large, single-center database comprising information relating to patients admitted to critical care units at a large tertiary care hospital. Data includes vital signs, medications, laboratory measurements, observations and notes charted by care providers, fluid balance, procedure codes, diagnostic codes, imaging reports, hospital length of stay, survival data, and more. Because the database is not open source, it can be access or shared freely; to get access to the database's records, training must be completed, and access has to be requested. The database can be obtained at (https://www.google.com/url?q=https://mimic.physionet.org/&sa=D&ust=1491769209941000&usg=AFQjCNHF2Y_9FzPHejpji9DryoOOfojFyA)

The features and tables’ names that I will use are shown below.

FEATURES

Body Mass Index: CHARTEVENTS table
Sub-Set of Medical Conditions: DIAGNOSESICD table
Age: PATIENT table
Sex: PATIENT table

LABEL
Admission Time Discharge Time (MIMIC admissions table): ADMISSION table

NOTE: The body mass index has to calculated from the height and weight values of the CHARTEVENTS table. MimicIII database doesn't have this stored directly.

INSTRUCTIONS TO CREATED THE DATA SET

1. Install Eclipse BIRT report designer. (http://download.eclipse.org/birt/downloads/)
2. Gain access to the MIMIC-III database by following the steps at “https://mimic.physionet.org/gettingstarted/access/.“
3. Rebuild the database using the instructions at https://mimic.physionet.org/tutorials/install-mimic-locally-ubuntu/.
4. Once the database is up and running, in this package you will find a file called eclipse-birt-mimiciii-dataset-report.zip¨, 
this file contains an ECLIPSE BIRT workbench report design file that can be imported to an ECLIPSE BIRT installation to recreate the dataset used in this project.
You will have to perform a minor modification to the imported eclipse report. The data source needs to point to your instance of the MIMIC-III database, after that just
run it and it will create the dataset used in this project.
5. I replaced some data sets records from 300 to 89 using excel after exporting the Birt report to a CSV file. You can do the same in BIRT before exporting the data or after using Python code, just don’t forget to do it. 
6. Finally, run the Jupiter notebook included in this package.



NOTE: Once the file has been imported, you will have to modify the report "DataSource" object to point to the PostgreSQL installation where the MIMICIII database resides.



