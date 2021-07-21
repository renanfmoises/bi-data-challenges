### Background

The goal of this challenge is to learn about Big Query pricing.

*HandyHelp* is growing. Your platform is driving more users, new services will be added soon and this will highly impact your current data storage capabilities. Maintaining and scaling in-house servers has become a costly issue. To cope with the growth that you will face in the following months, your company has decided to fully move their data storage to the cloud. The tech team has opted for GCP as a cloud storage solution. Additionally they want to have up-to-date data insights and have chosen Big Query as a data warehousing tool. 

### Objectives

But wait! The CFO has asked you to **make an estimate** on what is the cost of Google Big Query. Your current data warehousing needs are: 5 TB of active data storage. You have a team of 10 data people (Data Scientists & Analysts) doing an average of 500 queries/person in a month. Each query requires an average of 50MB of processing. Additionally, you grant access to Big Query to 10 non-technical stakeholders (marketing, sales…) and they will do an average of 10 queries/person in a month. Assume the same 50MB of processing/query.  

### Specs

**Task I**

Given the above specifications, what is the monthly cost (in USD) of Google Big Query ?

<details><summary markdown='span'>Assumptions and notes
</summary>
  For the analysis pricing estimation assume an On-demand pricing & US Multi-region location.

  For the storage pricing estimation assume a US Multi-region location.

  Assume analysis and storing pricing as the only 2 costs associated to this use case (no associated data ingestion or extraction prices).

  Notes: 1TB = 1000GB; 1GB = 1000MB
</details>

**Task II**

Your company plans to increase its initial 5TB active data storage in Big Query at a pace of 2% per month. Your data & non-technical team will grow 120% all over the year. Assume the same processing MBs/query & queries/person than in the previous exercise. What will be the yearly expense of GCP?

### Key learning points

- Learn how to estimate a Big Query storage and analysis pricing given a company case.
