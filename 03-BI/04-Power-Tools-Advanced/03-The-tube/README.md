## Background & Objectives

The goal of this challenge is to create an advanced report using a map chart and slicers.

## Import file

Create a new Power BI report, and load in the data from this file:

[subway.csv](https://wagon-public-datasets.s3.eu-west-1.amazonaws.com/bi-data/subway.csv)

## Data visualization

In this report, we want to create a map displaying the numbers of passengers by ticket type, changing the region and the total passengers thanks to slicers. Here are the regions we will use:

- London
- West Midlands
- Scotland
- Yorkshire and the Humber

![https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/03-BI/04-Power-Tools-Advanced/03-The-tube/Untitled.png](https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/03-BI/04-Power-Tools-Advanced/03-The-tube/Untitled.png)

## Create a raw report

We will design the skeleton of our report.

First, as mentioned previously, we only need 4 regions. 

Add a global filter on your report for the right regions.

Second, this report has 3 charts:

- 1 map, with the following information:
    - Coordinates of the subway stations
    - Number of passengers split into ticket type
    - A tooltip field so that you can see which station you're looking at

<details><summary markdown='span'>Hint 💡</summary>
![https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/03-BI/04-Power-Tools-Advanced/03-The-tube/Untitled%201.png](https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/03-BI/04-Power-Tools-Advanced/03-The-tube/Untitled%201.png)
</details>

- 2 slicers
    1. Region
    2. Estimated passengers

![https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/03-BI/04-Power-Tools-Advanced/03-The-tube/Untitled%202.png](https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/03-BI/04-Power-Tools-Advanced/03-The-tube/Untitled%202.png)

*Chart expected* 👆

## Format your report

Once the data charts and settings are ok, we will format our report.

For each chart add/modify the title (designation and background) and add a small border.

<details><summary markdown='span'>Hint 💡
</summary>
  - You can use the "Format painter" function
</details>


Let's go further.

- Region slicer:
    - Modify the orientation to get buttons: vertical ⇒ horizontal
    - Check "Single select"
- Map:
    - Change legend position
    - Increase the bubble size

Add a title to your report and save your file as **The tube**. 💾
