### Background and objectives

The goal of this challenge is to create your first Data Studio report.

Let's come back to the *HandyHelp* case! The COO is interested into taking a look at **complaints made in the last 60 days**. We will create a Data Studio report to help non-technical stakeholders in business decision-making. 

### Specs

1. First create a new partitioned table per MONTH (call it `partition_nyc_311`) and cluster by *borough*. You are mostly interested in the following fields: `agency`, `agency_name`, `borough`, `created_date`, `closed_date`, `complaint_type`, `status`. 
2. Create a Data Studio dashboard and use `partition_nyc_311` as a data source. 

    Here are the insights to monitor:

    1. Chart with the nb of complaints per borough.
    2. Chart with the nb of complaints over time.
    3. Counter with the total nb of complaints.
    4. Counter with the average resolution time of an issue.
    5. Chart with the complaint status in each borough.
    6. Chart to see who handles (agency) the complaints.
    7. Chart of  the evolution over time of complaints segmented by complaint type.
    8. Chart of avg. resolution time by complaint type.
    9. Feel free to add any other insight that you find interesting!!

    Make your dashboard **accessible to everybody** (view access permission) and share the URL.

### More requirements (optional)

The dashboard should incorporate 2 control filters:

- A Date range control. This control affects charts 2, 3, 4, 5, 6.
- A dropdown list control where I can filter a list of  4 targeted complaints. These complaints are: Noise - Residential, HEAT/HOT WATER, Illegal Parking and Blocked Driveway. This control affects graphs 7 and 8

Note that the chart 1. is independent of any filter.

Feel free to choose the type of chart that better suits each question.

### Key learning points

- Visualize insights in Data Studio
- Import data sources
- Use of filters & grouping of charts
