## Background and Objectives

The goal of this challenge is to practice partitioning and clustering.

*Airfaster* is a SaaS that uses machine learning to improve air cargo operations and airport logistics. They have been relying on several GCP services for a while. Recently, the CTO has triggered a red alert: the way that some team members are using Big Query is highly inefficient. This has led to a high processing cost/month. In order to reduce this amount, the CTO has asked you to partition some tables and assess the improvement.

## Specs

As a starting point, you are planning to work with data stored in a Google Cloud Storage bucket. To do so, create a project called *airfaster,* a dataset called *analysis* and a table called *flights* (by ingesting the data coming from the following Google Cloud Storage bucket: `gs://cloud-training/CPB200/BQ/lab4/domestic_2014_flights_*.json` ).  While creating the table, don’t use the source data partitioning and don’t select any partitioning  for the moment.

**IMPORTANT:** Write all your queries in the same script separated each of them by a ;  (like in the previous exercises). **BUT**, when you create and query the partitioned tables, skip the project name (only the dataset & table). For example:

```sql
-- For table creation, instead of: 
CREATE TABLE `airfaster-xxxx.analysis.partition_flights_2014` ...
--use :
CREATE TABLE `analysis.partition_flights_2014` ...
--and for querying, Instead of: 
    SELECT * FROM `airfaster-xxxx.analysis.flights`;
--use:
    SELECT * FROM `analysis.flights`;

```

Your deliverable will be the **shared URL** to your script.

Answer the following questions:

1. First, you have decided to create a time-unit column-partitioned table. Use the `FULL_DATE` column to implement the time filter partitioning.
2. Now, run a query against the partitioned table and describe the output.
3. Why is this happening?
4. Let’s do a small data manipulation change. We will change all the 2014 records in the `FULL_DATE` column for the current year. E.g. As I am working in the exercise in 2021, for a specific row, instead of having '2014-13-12' I will add 7 years to have '2021-13-12'. Create a column to store this new date (called `FORMATTED_DATE`) and use it to partition over this new date column. Call this new partitioned table `partition_flights_xxxx` ( where *xxxx* = current year).
    <details><summary markdown='span'>Hint 💡
    </summary>
      Take a look to the [date functions](https://cloud.google.com/bigquery/docs/reference/standard-sql/date_functions) wiki
    </details>

5. What is the oldest record stored in the new time partitioned table?
6. What is the departure airport (`ORIGIN`) with more flights? Filter dates between the oldest date stored in your partitioned table and that date +30 days.
7. Using the previous query, you want to check what is the processing improvement from the partitioned table vs. the non-partitioned one. Run the previous query in the non-partitioned table (Attach the SQL query) and compare the processing (MB or GB) of partitioned & non-partitioned queries. How much processing are you saving?
8. Create a new time-unit partitioned table, but this time in terms of MONTH (call it `monthly_partition_flights_xxxx`). It must have a description and require a partition filter. Add a clustering to the origin, destination and airline operator (`CARRIER`).
9. Create an integer partitioned table using the `DISTANCE` column (distance in miles between `ORIGIN` and `DESTINATION`).(call it `integer_partition_flights`). It must have a description and require a partition filter. Add a clustering to the origin, destination and airline operator (`CARRIER`).
    <details><summary markdown='span'>Hint 💡
    </summary>
      First, I recommend to estimate the min and max values of the DISTANCE column. Then you can map the values so that they fall within a range. E.g.: If the min. and max. distance values are 100 and 500 miles then all the mile values could fall in the interval: [100,200,400,500]
    </details>

10. Use the previous integer partitioned table for this task. What are the top 5 airline (`CARRIER`) that has longest average departure delays in sort distance flights ( short distance flights = between the shortest distance and 1000 miles) ? 
    <details><summary markdown='span'>Note
    </summary>
      There are negative values of departure delays (flights that leave the airport before schedule). You should not consider them for the analysis.

      If you are curious about getting the airlines names from its IATA code take a look [here](https://en.wikipedia.org/wiki/List_of_airlines_of_the_United_States)
    </details>

11. What are the airlines with longest arrival delays in each airport in medium length trips (1000 to 3000 miles)? Rank them and see the top 2 in each airport. What is the airline experiencing the second longest delay in New York - JFK airport?

## Key learning points

- Ingest data from a Google Cloud storage bucket
- Apply your SQL knowledge to solve analytical questions
- Practice time-unit and integer partitioning
- Practice clustering
