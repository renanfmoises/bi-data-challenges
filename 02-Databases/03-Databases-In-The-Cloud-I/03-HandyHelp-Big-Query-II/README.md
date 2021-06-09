# HandyHelp Big Query analysis II

### Background & objectives

Your work to help *HandyHelp* to better seize the market continues. Now you are interested into looking at the types of complaints made in NYC.

### Specs

**IMPORTANT**: You have to **deliver the URL of your script with all your SQL queries.** Same thing than in *HandyHelp Big Query analysis I.* Make sure that the script is running without errors before delivering.

---

Again, as we are planning for the 2021 workforce allocation, **filter** in all your queries calls/complaints **from 2020**. Answer the following questions: 

1. What are New Yorkers complaining the most about (*complaint type*)? Order the complaints in descending order. 
2. You think that this first query might be interesting for other analysis and it will be used by other data team members. Store it as a view (using the Editor commands not the *Save as*... ) in a dataset called `handyhelp`
    - Note

        When you add your SQL code to create the view in your script don't write the name of the project preceding the handyhelp dataset. e.g: instead of `myfirstproject-xxxx.handyhelp.complaints_view` use `handyhelp.complaints_view`(only dataset.table).

3. There are several noise related issues in NYC (Noise-Residential, Noise - Street/Sidewalk…) To appreciate the real scale of it, aggregate all the noise related issues and compare it with the rest of complaints (in %). 
4. What is the average resolution time of problems?
    - Trick

        To obtain the resolution time you could create a column that subtract 'closed_date' to 'opened_date'. Also in the WHERE clause filter out all resolution times = 0.

5. What is the average resolution time of each complaint type? 
6. What is the borough where the complaints are solved faster?
7. You want to asses what complaints take more time to resolve. With that information you can better allocate the offer to the demand per borough. What are the slowest complaints (=longest resolution time) to be solved in each borough? 
- Note

    Filter out boroughs with null  values and Unspecified

7. You want to assess whether to include a pest control professional/fumigator category in the platform. Is there a real demand for that in NYC? To decide about it you analyze how often (times per day) a rodent is reported in NYC.

### Key learning points

- Keep practicing your SQL knowledge to solve analytical questions
- Create Views
- Use date/timestamp/time functions in your queries

# SOLUTIONS

You can see all the queries in the following script: [https://console.cloud.google.com/bigquery?sq=209365008754:cdf58ec8b4734fca87140750e3e72d50](https://console.cloud.google.com/bigquery?sq=209365008754:cdf58ec8b4734fca87140750e3e72d50) 

1. The top 3 complaints in 2020 are: Noise - Residential, Noise - Street/Sidewalk and Illegal Parking. 

```sql
SELECT 
complaint_type,
COUNT(*) AS counter
 FROM 
`bigquery-public-data.new_york_311.311_service_requests`  
WHERE EXTRACT (YEAR FROM created_date) = 2020
GROUP BY complaint_type
ORDER BY counter DESC;
```

2. See query below

```sql
CREATE VIEW `handyhelp.complaints_view` 
AS
SELECT 
complaint_type,
COUNT(*) as counter
 FROM 
`bigquery-public-data.new_york_311.311_service_requests`  
WHERE EXTRACT (YEAR FROM created_date) = 2020
GROUP BY complaint_type
ORDER BY counter DESC;
```

3. 31 % are noise related complaints vs. 69% others

```sql
--Option 1.
SELECT 
    CASE
    WHEN complaint_type LIKE ('Noise%') THEN 'Noise'
    ELSE 'Others'
  END
  AS category,
 COUNT(*) AS count_complaint
 FROM 
`bigquery-public-data.new_york_311.311_service_requests` 
WHERE 
EXTRACT (YEAR FROM created_date) = 2020
GROUP BY category
order by count_complaint DESC;

--Option 2. Same as 1 but we estimate the % in the query.
WITH noise_vs_others AS (
    SELECT 
    CASE
    WHEN complaint_type LIKE ('Noise%') THEN 'Noise'
    ELSE 'Others'
  END
  AS category,
 COUNT(*) AS count_complaint
 FROM 
`bigquery-public-data.new_york_311.311_service_requests` 
WHERE 
EXTRACT (YEAR FROM created_date) = 2020
GROUP BY category
order by count_complaint DESC)
SELECT category,count_complaint,100*(count_complaint/value) FROM noise_vs_others,
(SELECT 
COUNT(*)AS value FROM 
`bigquery-public-data.new_york_311.311_service_requests` 
WHERE EXTRACT (YEAR FROM created_date) = 2020);
```

4. ~311 hours. See query below:   

```sql
SELECT 
AVG(TIMESTAMP_DIFF(closed_date,created_date,HOUR)) AS avg_resolution_time,
FROM 
`bigquery-public-data.new_york_311.311_service_requests` 
WHERE EXTRACT (YEAR FROM created_date) = 2020
AND TIMESTAMP_DIFF(closed_date,created_date,HOUR) > 0;
```

5.  See query result below

```sql
SELECT 
complaint_type,
AVG(TIMESTAMP_DIFF(closed_date,created_date,HOUR)) AS avg_resolution_time,
FROM 
`bigquery-public-data.new_york_311.311_service_requests` 
WHERE EXTRACT (YEAR FROM created_date) = 2020
AND TIMESTAMP_DIFF(closed_date,created_date,HOUR) > 0
GROUP BY complaint_type;
--ORDER BY avg_resolution_time DESC;
```

6. In the Bronx.

```sql
SELECT 
borough,
AVG(TIMESTAMP_DIFF(closed_date,created_date,HOUR)) AS avg_resolution_time,
FROM 
`bigquery-public-data.new_york_311.311_service_requests`
WHERE EXTRACT (YEAR FROM created_date) = 2020
AND TIMESTAMP_DIFF(closed_date,created_date,HOUR) > 0
GROUP BY borough
ORDER BY avg_resolution_time;
```

7. See results in query below. For example in the Bronx the slowest solved complaints are: Miscellaneous Categories, Bike Rack Condition, Cranes and Derricks...

```sql
--Option 1. 
SELECT 
borough,
complaint_type,
AVG(TIMESTAMP_DIFF(closed_date,created_date,HOUR)) AS avg_resolution_time,
FROM 
`bigquery-public-data.new_york_311.311_service_requests` 
WHERE EXTRACT (YEAR FROM created_date) = 2020
AND TIMESTAMP_DIFF(closed_date,created_date,HOUR) > 0
AND( borough is not null or borough!= 'Unspecified')
GROUP BY borough,complaint_type
ORDER BY borough,avg_resolution_time DESC;

--Option 2. Using rank() over partition and filtering top 4 slowest resolution complaints/borough

WITH ranking_query AS ( 
     SELECT 
     borough,
     complaint_type,
     AVG(TIMESTAMP_DIFF(closed_date,created_date,HOUR)) AS avg_resolution_time,
     RANK () OVER ( 
			PARTITION BY borough
			ORDER BY AVG(TIMESTAMP_DIFF(closed_date,created_date,HOUR)) DESC
            ) AS dur_rank 
     FROM 
    `bigquery-public-data.new_york_311.311_service_requests` 
     WHERE EXTRACT (YEAR FROM created_date) = 2020
     AND( borough is not null or borough!= 'Unspecified')
     AND TIMESTAMP_DIFF(closed_date,created_date,HOUR) > 0
     GROUP BY borough,complaint_type)

SELECT * FROM ranking_query WHERE dur_rank IN ( 1,2,3,4)
```

8. An average of ~75 times per day a rodent is reported

```sql
WITH rats_per_day AS (
    SELECT 
    FORMAT_DATE('%F',created_date) AS Day,
    COUNT(*) AS count_complaint
    FROM 
    `bigquery-public-data.new_york_311.311_service_requests` 
    WHERE complaint_type= "Rodent" AND
    EXTRACT (YEAR FROM created_date) = 2020
    GROUP BY Day
    order by count_complaint)
SELECT AVG(count_complaint) FROM rats_per_day;
```