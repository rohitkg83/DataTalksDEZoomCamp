# SQL Queries used for homework

Question 1: What is count of records for the 2022 Green Taxi Data??

SELECT count(*) FROM `ny-rides-rohitg.ny_taxi.green_taxi_data_2022`

Question 2: Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

SELECT count(distinct(PULocationID)) FROM `ny-rides-rohitg.ny_taxi.green_taxi_data_2022`

SELECT count(distinct(PULocationID)) FROM `ny-rides-rohitg.ny_taxi.bq_green_taxi_data_2022`;

Question 3: How many records have a fare_amount of 0?

select count(*) from `ny-rides-rohitg.ny_taxi.green_taxi_data_2022` where fare_amount = 0

Question 4: What is the best strategy to make an optimized table in Big Query if your query will always order the results by PUlocationID and filter based on lpep_pickup_datetime? (Create a new table with this strategy)

CREATE OR REPLACE TABLE ny-rides-rohitg.ny_taxi.green_taxi_data_2022_partitioned_clustered
PARTITION BY DATE(cleaned_pickup_datetime)
CLUSTER BY PULocationID AS
SELECT *, TIMESTAMP_MICROS(CAST(lpep_pickup_datetime / 1000 AS INT64)) AS cleaned_pickup_datetime 
FROM ny-rides-rohitg.ny_taxi.bq_green_taxi_data_2022;


Question 5: Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values?

Choose the answer which most closely matches.


SELECT distinct(PULocationID) FROM `ny-rides-rohitg.ny_taxi.bq_green_taxi_data_2022` 
where DATE(TIMESTAMP_MICROS(CAST(lpep_pickup_datetime / 1000 AS INT64))) >= '2022-06-01'
AND DATE(TIMESTAMP_MICROS(CAST(lpep_pickup_datetime / 1000 AS INT64))) <= '2022-06-30';

SELECT distinct(PULocationID) FROM `ny-rides-rohitg.ny_taxi.green_taxi_data_2022_partitioned_clustered` 
where cleaned_pickup_datetime >= '2022-06-01'
AND cleaned_pickup_datetime <= '2022-06-30';





