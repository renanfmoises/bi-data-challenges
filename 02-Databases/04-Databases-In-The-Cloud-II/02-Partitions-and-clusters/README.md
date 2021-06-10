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

1.  First, you have decided to create a time-unit column-partitioned table. Use the column `FULL_DATE` to implement the time filter partitioning. 
2. Now, run a query against the partitioned table and describe the output.
3. Why this is happening?
4. Let’s do a small data manipulation change. We will change all the 2014 records in the `FULL_DATE` column for the current year. E.g. : As I am working in the exercise in 2021, for a specific row, instead of having '2014-13-12' I will add 7 years to have '2021-13-12'. Create a column to store this new date (called `FORMATTED_DATE`) and use it to partition over this new date column. Call this new partitioned table  *partition_flights_xxxx* ( where *xxxx* = current year). 
- Trick

    Take a look to the [date functions](https://cloud.google.com/bigquery/docs/reference/standard-sql/date_functions) wiki

5. What is the oldest record stored in the new time partitioned table?

6. What is the departure airport (`ORIGIN`) with more flights? Filter dates between the oldest date stored in your partitioned table and that date +30 days. 

7. Using the previous query, you want to check what is the processing improvement from the partitioned table vs. the non-partitioned one. Run the previous query in the non-partitioned table (Attach the SQL query) and compare the processing (MB or GB) of partitioned & non-partitioned queries.  How much processing are you saving?

8. Create a new time-unit partitioned table, but this time in terms of MONTH (call it *monthly_partition_flights_xxxx*). It must have a description and require a partition filter. Add a clustering to the origin, destination and airline operator (`CARRIER`). 

9. Create an integer partitioned table using the DISTANCE column (distance in miles between `ORIGIN` and `DESTINATION`).(call it  *integer_partition_flights*). It must have a description and require a partition filter. Add a clustering to the origin, destination and airline operator (`CARRIER`). 

- Trick

    First, I recommend to estimate the min and max values of the DISTANCE column. Then you can map the values so that they fall within a range. E.g.: If the min. and max. distance values are 100 and 500 miles then all the mile values could fall in the interval: [100,200,400,500]

10. Use the previous integer partitioned table for this task. What are the top 5 airline (`CARRIER`) that has longest average departure delays in sort distance flights ( short distance flights = between the shortest distance and 1000 miles) ? 

- Note

    There are negative values of departure delays (flights that leave the airport before schedule). You should not consider them for the analysis.

    If you are curious about getting the airlines names from its IATA code take a look [here](https://en.wikipedia.org/wiki/List_of_airlines_of_the_United_States)

11. What are the airlines with longest arrival delays in each airport in medium length trips (1000 to 3000 miles)? Rank them and see the top 2 in each airport. What is the airline experiencing the second longest delay in New York - JFK airport?

## Key learning points

- Ingest data from a Google Cloud storage bucket
- Apply your SQL knowledge to solve analytical questions
- Practice time-unit and integer partitioning
- Practice clustering

# SOLUTION

**Challenge**

You can find all the queries in this script: [https://console.cloud.google.com/bigquery?sq=209365008754:638b90d6f61f438dac9d7c0250784eb2](https://console.cloud.google.com/bigquery?sq=209365008754:638b90d6f61f438dac9d7c0250784eb2)

1.

```sql
CREATE TABLE `analysis.partition_flights_2014`
   PARTITION BY FULL_DATE    
 AS 
    SELECT * FROM `analysis.flights`;
```

2.

It returned no results.

3.

As we are using the Big Query Sandbox we are [limited](https://cloud.google.com/bigquery/docs/sandbox#limits) to a 60 days partition expiration period:

*“All datasets have the default table expiration time and the default partition expiration set to 60 days. Any tables, views, or partitions in partitioned tables automatically expire after 60 days.”*

As all the records in the `FULL_DATE` column are from 2014 the data is “expired” and therefore not added to partitioned table.

4. 

```sql
CREATE TABLE `analysis.partition_flights_2021`
   PARTITION BY FORMATTED_DATE    
 AS 
    SELECT *,DATE_ADD(FULL_DATE, INTERVAL 7 YEAR) as FORMATTED_DATE
 FROM `analysis.flights` as flights;
```

5.

It has to be current date minus 60 days. If I had created the partitioned table and run this query on 2021-05-13 then the oldest record is from: 2021-03-14.

6. In my specific period of time, the airport with more departure flights is ATL (Atlanta airport)

```sql
SELECT ORIGIN,COUNT(*) count_origins
FROM `analysis.partition_flights_2021`
WHERE FORMATTED_DATE BETWEEN '2021-03-14' AND DATE_ADD('2021-03-14', INTERVAL 30 DAY) 
GROUP BY ORIGIN
ORDER BY count_origins DESC;
```

7. 

```sql
-- same query than 6. but for non partitioned table.
SELECT ORIGIN, COUNT(*) count_origins
FROM `analysis.flights`
WHERE DATE_ADD(FULL_DATE, INTERVAL 7 YEAR) BETWEEN '2021-03-14' AND DATE_ADD('2021-03-14', INTERVAL 30 DAY)
--WHERE FULL_DATE BETWEEN '2014-03-14' AND DATE_ADD('2014-03-14', INTERVAL 30 DAY)
GROUP BY ORIGIN
ORDER BY count_origins DESC

/*You can use both the DATE_ADD function to format the FULL_DATE
 column and the original FULL_DATE column and check on 2014 values.*/
```

Processing time (for my given time range):

8.8 MB with partitioning vs 78.1 MB without partitioning. We are saving 69,3 MB of  processing( Aprox. **90%** smaller processing). On this small queries it might not look significant but on a "heavier" query it does.

For example, if we had to query all columns in the given date range ( see following queries):

Partitioned (143.6 MB processing)

```sql
SELECT *
FROM `analysis.partition_flights_2021`
WHERE FORMATTED_DATE BETWEEN '2021-03-14' AND DATE_ADD('2021-03-14', INTERVAL 30 DAY);
```

Non-partitioned (1.1 GB non partitioned)

```sql
SELECT *
FROM `analysis.flights`
WHERE DATE_ADD(FULL_DATE, INTERVAL 7 YEAR) BETWEEN '2021-03-14' AND DATE_ADD('2021-03-14', INTERVAL 30 DAY) ;
--WHERE FULL_DATE BETWEEN '2014-03-14' AND DATE_ADD('2014-03-14', INTERVAL 30 DAY);
```

**The difference is huge:**

143.6 MB vs. 1.1 GB (**956 MB saved** !!).

Note: MBs in my solution might differ from your solution. However, you have to experience a big improvement when partitioning. 

8. 

```sql
CREATE TABLE `analysis.monthly_partition_flights_2021`
   PARTITION BY DATE_TRUNC(FORMATTED_DATE , MONTH) 
   CLUSTER BY
  ORIGIN,
  DESTINATION,
  CARRIER
   OPTIONS(
  description='This a a monthly partitioned table of flights table',
  require_partition_filter=true
)
 AS 
    SELECT *, DATE_ADD(FULL_DATE, INTERVAL 7 YEAR) as FORMATTED_DATE
 FROM `analysis.flights`;
```

9.

The max. and min. distance of flights are 4983 (New York to Honolulu) and 24 miles ( between 2 different Washington airports) respectively. See query:

```sql
SELECT MAX(DISTANCE), MIN(DISTANCE) FROM `analysis.flights`
```

To create the partitioned table:

```sql
CREATE TABLE `analysis.integer_partition_flights`
   PARTITION BY RANGE_BUCKET(DISTANCE ,GENERATE_ARRAY(24, 4983, 200))
      CLUSTER BY
  ORIGIN,
  DESTINATION,
  CARRIER
   OPTIONS (
  description='This is an integer partitioned table of flights table',
  require_partition_filter=true
)
 AS 
    SELECT *,RANGE_BUCKET(DISTANCE ,GENERATE_ARRAY(24, 4983, 200)) as integer_partition
 FROM `analysis.flights`;
```

10.

```sql
SELECT CARRIER, ROUND(AVG(DEPARTURE_DELAY)) as longest_delays
 FROM `analysis.integer_partition_flights`
WHERE DISTANCE BETWEEN 24 AND 1000
AND DEPARTURE_DELAY >0
GROUP BY CARRIER
ORDER BY longest_delays DESC
LIMIT 5;
```

[Airlines with the longest average departure delays for sort distance flights](https://www.notion.so/4e5c284f5bed4947a3570ce2feeba2a0)

11.

```sql
WITH ranked_delays_airport AS (
   SELECT DESTINATION,CARRIER, ROUND(AVG(ARRIVAL_DELAY)) as longest_delays ,
RANK () OVER ( 
			PARTITION BY DESTINATION
			ORDER BY ROUND(AVG(ARRIVAL_DELAY)) DESC
            ) delay_rank
FROM `analysis.integer_partition_flights`
WHERE DISTANCE BETWEEN 1000 AND 3000
AND ARRIVAL_DELAY > 0
GROUP BY DESTINATION,CARRIER )

SELECT * FROM ranked_delays_airport
WHERE delay_rank IN (1,2)
--AND DESTINATION ='JFK'
```

The airline experiencing the second longest delay in New York (JFK airport)  is UA (United Airlines).