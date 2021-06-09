### Background

The goal of this challenge is to learn about Big Query pricing.

*HandyHelp* is growing. Your platform is driving more users, new services will be added soon and this will highly impact your current data storage capabilities. Maintaining and scaling in-house servers has become a costly issue. To cope with the growth that you will face in the following months, your company has decided to fully move their data storage to the cloud. The tech team has opted for GCP as a cloud storage solution. Additionally they want to have up-to-date data insights and have chosen Big Query as a data warehousing tool. 

### Objectives ****

But wait! The CFO has asked you to **make an estimate** on what is the cost of Google Big Query. Your current data warehousing needs are: 5 TB of active data storage. You have a team of 10 data people (Data Scientists & Analysts) doing an average of 500 queries/person in a month. Each query requires an average of 50MB of processing. Additionally, you grant access to Big Query to 10 non-technical stakeholders (marketing, sales…) and they will do an average of 10 queries/person in a month. Assume the same 50MB of processing/query.  

### Specs

**Task I**

Given the above specifications, what is the monthly cost (in USD) of Google Big Query ?

- Assumptions and notes

    For the analysis pricing estimation assume an On-demand pricing & US Multi-region location.

    For the storage pricing estimation assume a US Multi-region location.

    Assume analysis and storing pricing as the only 2 costs associated to this use case (no associated data ingestion or extraction prices).

    Notes: 1TB =1000GB ; 1GB=1000MB

**Task II**

Your company plans to increase its initial 5TB active data storage in Big Query at a pace of 2% per month. Your data & non-technical team will grow 120% all over the year. Assume the same processing MBs/query & queries/person than in the previous exercise. What will be the yearly expense of GCP?

### Key learning points

- Learn how to estimate a Big Query storage and analysis pricing given a company case.

# SOLUTION (readme.md and .xls in a zip archive)

### **Task I**

---

**Storage pricing**

5TB of data = 5000GB. First 10GB per month are free => We pay for 4990 GB => 4990 * 0.020 USD/month = 99.8 USD/month.

**Analysis Pricing**

10 data people * 500 queries/person *50 MB = 250,000 MB

10 non tech people *10 queries/person *50MB = 5000 MB

Total = 255,000 MB/month = 255 GB/month

255GB < 1TB => analysis pricing is free!!!

**TOTAL PRICE OF GBQ/month = 99.8 USD**

### **Task II**

---

**Storage Pricing** 

See excel file "analysis and storage pricing.xlsx".

[analysis and storage pricing.xlsx](assets/analysis_and_storage_pricing.xlsx)

**Analysis Pricing**

At the end of the year each team will have:

20*(1+ 1,2) = 44 new people

After 12 months we will get:

22 data people * 500 queries/person *50 MB = 550,000 MB

22 non tech people *10 queries/person *50MB = 11000 MB

Total = 561000 MB/month = 561 GB/month

**Still below 1TB after 12 months. Over the year they won't experience any charge in Analysis pricing.**
