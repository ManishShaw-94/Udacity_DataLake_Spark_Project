# Udacity_DataLake_Spark_Project

### Introduction

STEDI Human Balance Analytics team wants to build a data lakehouse solution for sensor data that trains a machine learning model. The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used.

### Project Details
The STEDI Team has been hard at work developing a hardware STEDI Step Trainer that:

* trains the user to do a STEDI balance exercise;
* and has sensors on the device that collect data to train a machine-learning algorithm to detect steps;
* has a companion mobile app that collects customer data and interacts with the device sensors.
STEDI has heard from millions of early adopters who are willing to purchase the STEDI Step Trainers and use them.

Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. The Step Trainer is just a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions.

### Project Datasets
1. Customer Records (from fulfillment and the STEDI website):

AWS S3 Bucket URI - s3://cd0030bucket/customers/

contains the following fields:

 * serialnumber
 * sharewithpublicasofdate
 * birthday
 * registrationdate
 * sharewithresearchasofdate
 * customername
 * email
 * lastupdatedate
 * phone
 * sharewithfriendsasofdate
 
2. Step Trainer Records (data from the motion sensor):

AWS S3 Bucket URI - s3://cd0030bucket/step_trainer/

contains the following fields:

 * sensorReadingTime
 * serialNumber
 * distanceFromObject
3. Accelerometer Records (from the mobile app):

AWS S3 Bucket URI - s3://cd0030bucket/accelerometer/

contains the following fields:

 * timeStamp
 * serialNumber
 * x
 * y
 * z
 
 ### Project Instruction:
 
 To simulate the data coming from the various sources, need to create S3 directories for customer_landing, step_trainer_landing, and accelerometer_landing zones, and copy the data there as a starting point.Project Template include following files:
 * two Glue tables for the two landing zones. customer_landing.sql and accelerometer_landing.sql
 * Query these tables using Athena, and screenshot of each one showing the resulting data - customer_landing.jpeg and accelerometer_landing.jpeg
 
 Create 2 AWS Glue Jobs that do the following:
 1. Sanitize the Customer data from the Website (Landing Zone) and only store the Customer Records who agreed to share their data for research purposes (Trusted Zone) - creating a Glue Table called customer_trusted.
 2. Sanitize the Accelerometer data from the Mobile App (Landing Zone) - and only store Accelerometer Readings from customers who agreed to share their data for research purposes (Trusted Zone) - creating a Glue Table called accelerometer_trusted.
 3. Verify the Glue job is successful and only contains Customer Records from people who agreed to share their data. Query the Glue customer_trusted table with Athena and take a screenshot of the data - customer_trusted.jpeg
 
 Write a Glue job that does the following:
 1. Sanitize the Customer data (Trusted Zone) and create a Glue Table (Curated Zone) that only includes customers who have accelerometer data and have agreed to share their data for research called customers_curated.
 2. Read the Step Trainer IoT data stream (S3) and populate a Trusted Zone Glue Table called step_trainer_trusted that contains the Step Trainer Records data for customers who have accelerometer data and have agreed to share their data for research (customers_curated).
 3. Create an aggregated table that has each of the Step Trainer Readings, and the associated accelerometer reading data for the same timestamp, but only for customers who have agreed to share their data, and make a glue table called machine_learning_curated.
