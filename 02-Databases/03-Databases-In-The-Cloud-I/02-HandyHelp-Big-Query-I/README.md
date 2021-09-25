### Background

*HandyHelp* is a NYC based startup that aims at revolutionizing the tradesman help on-demand industry. Having something to fix at home? Then you open HandyHelp app or browse to their website and find an electrician, carpenter, builder… that will address your issue in less than 5 hours. As a part of their expansion roadmap, they are planning to partner with local authorities to provide tradesman help on-demand.

### Objectives

To better seize the market and to distribute their workforce accordingly, they want to analyze what is the NYC demand of tradesman personnel. 

Moreover, the CTO has decided to start migrating all the data to GCP. Along with the CEO, and as a first point of contact, they have asked you, a skilled Data Analyst working in *HandyHelp*, to use the NYC 311 dataset available in Google Big Query to understand better the market.

**What is the 311?**

> In USA , *it is a non-emergency phone number that people can call in many cities to find information about services, make complaints, or report problems like graffiti or road damage*… (source: [govtech.com](https://www.govtech.com/dc/articles/what-is-311.html))

You can find the NYC 311 dataset in the public datasets in Big Query: `bigquery-public-data.new_york_311.311_service_requests` **Each row represents a call made to 311**.

---

### Specs

**IMPORTANT**: To deliver your solution write all queries in the same Big Query script. The queries should not be commented ( **NO** `- -`  or `/* */` ). To separate each query **don't forget to add; at the end of each one**. When you are finished, make sure that the script runs properly. Several successful jobs should appear in the Query results tab:

![https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/02-Databases/03-Databases-In-The-Cloud-I/02-HandyHelp-Big-Query-I/succefuls_run.png](https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/02-Databases/03-Databases-In-The-Cloud-I/02-HandyHelp-Big-Query-I/succefuls_run.png)

 Then save the script as we learned in class with a personal Visibility:

![https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/02-Databases/03-Databases-In-The-Cloud-I/02-HandyHelp-Big-Query-I/Captura.png](https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/02-Databases/03-Databases-In-The-Cloud-I/02-HandyHelp-Big-Query-I/Captura.png)

Finally, go to your **Saved Queries**, click on the saved script and **activate the Link Sharing** option:

![https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/02-Databases/03-Databases-In-The-Cloud-I/02-HandyHelp-Big-Query-I/link-on.png](https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/02-Databases/03-Databases-In-The-Cloud-I/02-HandyHelp-Big-Query-I/link-on.png)

Your deliverable is the **Query URL** that appears there. Please share it on Slack with your lead instructor right away.

---

As we are planning for the 2021 workforce allocation, **filter** in all your queries calls/complaints **from 2020**. Answer the following questions writing SQL queries in a Big Query script.

1. What is the NYC borough calling the most to 311?
2. What is the month with more 311 calls?
3. What about the borough with more 311 calls in August 2020?
4. What is the day of the week where the total number of calls is higher? (Assuming that *created_date* is the call date)
5. What is the day of the week with a highest average number of calls? 
    Need help?

    <details><summary markdown='span'>Hint 💡
    </summary>
      Maybe you could use the `WITH` clause that you learned in the previous units
    </details>

6. What is the average number of calls during the weekends (Saturday & Sunday)?
7. How has this average weekend number of calls evolved over the years? 

---

### Key learning points

- Learn how to query Google public datasets
- Apply your SQL knowledge to solve analytical questions
- Use date/timestamp/time functions in your queries
