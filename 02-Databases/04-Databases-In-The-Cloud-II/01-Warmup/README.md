## Objective

The goal of this challenge is to introduce partitioned tables.

## Specs

Let's query some partitioned tables. Open the *Political advertisement on Google* dataset available within Big Query public datasets. There, you will find an *advertiser_geo_spend* table. 

1. What type of partition does the *advertiser_geo_spend* table have?
2. Create a query that allows you to see the value of the partition column used.

# SOLUTIONS

1. It is an ingestion-time partitioned table. As we can see by clicking on the table Details and seeing the time pseudo-column `_PARTITIONTIME` (typical from ingestion-time partitioning)

2. 

```sql
SELECT *,_PARTITIONTIME as pt
 FROM `bigquery-public-data.google_political_ads.advertiser_geo_spend`
```