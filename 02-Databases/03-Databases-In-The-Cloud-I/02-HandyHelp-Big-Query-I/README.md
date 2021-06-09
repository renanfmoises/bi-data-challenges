# HandyHelp Big Query analysis I

### Background

*HandyHelp* is a NYC based startup that aims at revolutionizing the tradesman help on-demand industry. Having something to fix at home? Then you open HandyHelp app or browse to their website and find an electrician, carpenter, builder… that will address your issue in less than 5 hours. As a part of their expansion roadmap, they are planning to partner with local authorities to provide tradesman help on-demand.

### Objectives

To better seize the market and to distribute their workforce accordingly, they want to analyze what is the NYC demand of tradesman personnel. 

Moreover, the CTO has decided to start migrating all the data to GCP. Along with the CEO, and as a first point of contact, they have asked you, a skilled Data Analyst working in *HandyHelp*, to use the NYC 311 dataset available in Google Big Query to understand better the market.

- What is the 311?

    > In USA , *it is a non-emergency phone number that people can call in many cities to find information about services, make complaints, or report problems like graffiti or road damage*… (source: [govetech.com](http://govetech.com/))

You can find the NYC 311 dataset in the public datasets in Big Query: `bigquery-public-data.new_york_311.311_service_requests` **Each row represents a call made to 311**.

---

### Specs

**IMPORTANT**: To deliver your solution write all queries in the same Big Query script. The queries should not be commented ( **NO** - -  or /* */ ). To separate each query **don't forget to add; at the end of each one**. When you are finished, make sure that the script runs properly. Several successful jobs should appear in the Query results tab:

![assets/succefuls_run.png](HandyHelp%20Big%20Query%20analysis%20I%20a9c78f9605a24ebd982042c041b8afee/succefuls_run.png)

 Then save the script as we learned in class with a personal Visibility:

![assets/Captura.png](HandyHelp%20Big%20Query%20analysis%20I%20a9c78f9605a24ebd982042c041b8afee/Captura.png)

Finally, go to your **Saved Queries**, click on the saved script and **activate the Link Sharing** option:

![assets/link-on.png](HandyHelp%20Big%20Query%20analysis%20I%20a9c78f9605a24ebd982042c041b8afee/link-on.png)

Your deliverable is the **Query URL** that appears there. Please share it on Slack with your lead instructor right away.

---

As we are planning for the 2021 workforce allocation, **filter** in all your queries calls/complaints **from 2020**. Answer the following questions writing SQL queries in a Big Query script.

1. What is the NYC borough calling the most to 311?
2. What is the month with more 311 calls?
3. What about the borough with more 311 calls in August 2020?
4. What is the day of the week where the total number of calls is higher? (Assuming that *created_date* is the call date)
5. What is the day of the week with a highest average number of calls? 
    - Trick

        Maybe you could use the `WITH` clause that you learned in the previous units

6. What is the average number of calls during the weekends (Saturday & Sunday)?
7. How has this average weekend number of calls evolved over the years? 

---

### Key learning points

- Learn how to query Google public datasets
- Apply your SQL knowledge to solve analytical questions
- Use date/timestamp/time functions in your queries

# SOLUTIONS

You can see all the queries in the following script: [https://console.cloud.google.com/bigquery?sq=209365008754:5d435d3c53fb49518b8f1427f3abbdee](https://console.cloud.google.com/bigquery?sq=209365008754:5d435d3c53fb49518b8f1427f3abbdee)

1. Top 3 with more calls: 1.Brooklyn, 2.Queens, 3.Bronx

```sql
SELECT 
borough,
COUNT(*) AS count_requests
FROM 
`bigquery-public-data.new_york_311.311_service_requests` 
WHERE EXTRACT (YEAR FROM created_date)= 2020
GROUP BY borough
ORDER BY count_requests DESC;
```

2.  August: 309713 calls

```sql
SELECT 
EXTRACT( MONTH FROM created_date) AS month_of_requests,
COUNT(*) AS count_requests
FROM 
`bigquery-public-data.new_york_311.311_service_requests` 
WHERE EXTRACT (YEAR FROM created_date)= 2020
GROUP BY month_of_requests
ORDER BY count_requests DESC;
```

3. Queens

```sql
SELECT 
borough,
COUNT(*) AS count_requests
FROM 
`bigquery-public-data.new_york_311.311_service_requests` 
WHERE FORMAT_DATE("%b-%Y", created_date) = 'Aug-2020'
GROUP BY borough
ORDER BY count_requests DESC;
```

4. Saturday (7) : 382119 calls

```sql
SELECT 
 EXTRACT(DAYOFWEEK FROM created_date) AS DayofWeek,
 COUNT(*) AS total_requests
FROM 
`bigquery-public-data.new_york_311.311_service_requests` 
WHERE EXTRACT (YEAR FROM created_date)= 2020
GROUP BY DayofWeek
order by total_requests DESC;
```

5. Saturday (7) :  ~7348 calls of average

```sql
WITH count_per_day AS (
SELECT 
FORMAT_DATE('%F',created_date) AS creation_date,#Returns an String.
COUNT(*) AS count_requests
FROM
`bigquery-public-data.new_york_311.311_service_requests` 
WHERE EXTRACT (YEAR FROM created_date) = 2020
GROUP BY creation_date
) 
SELECT EXTRACT(DAYOFWEEK FROM DATE(creation_date)) AS DayofWeek,
AVG(count_requests) AS avg_requests_day
FROM count_per_day
GROUP BY DayofWeek
ORDER BY avg_requests_day DESC;
```

6.  ~7284 calls

```sql
WITH count_per_day AS (
    SELECT 
FORMAT_DATE('%F',created_date) AS creation_date,#Returns an String.
COUNT(*) AS count_requests
FROM
`bigquery-public-data.new_york_311.311_service_requests` 
WHERE (EXTRACT (YEAR FROM created_date) = 2020 ) AND
      (EXTRACT (DAYOFWEEK FROM created_date) IN (1,7))
GROUP BY creation_date
) 
SELECT 
AVG(count_requests) AS avg_requests_day
FROM count_per_day;
```

7. See query result in BQ

```sql
WITH count_per_day AS (
    SELECT 
FORMAT_DATE('%F',created_date) AS creation_date,#Returns an String.
COUNT(*) AS count_requests
FROM
`bigquery-public-data.new_york_311.311_service_requests` 
WHERE EXTRACT (DAYOFWEEK FROM created_date) IN (1,7)
GROUP BY creation_date
) 
SELECT EXTRACT (YEAR FROM DATE(creation_date)) AS Year, 
AVG(count_requests) AS avg_requests_day
FROM count_per_day
GROUP BY Year
ORDER BY Year;
```
