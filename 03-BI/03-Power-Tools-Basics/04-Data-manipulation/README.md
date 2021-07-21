## Background & Objectives

The goal of this challenge is to learn how to manipulate date format.

## Import file

Create a new Power BI report, and load the data from this file:

[First half.xlsx](assets/First_half.xlsx)

![assets/Untitled.png](assets/Untitled.png)

<details><summary markdown='span'>Hint 💡
</summary>
  - Drop 1st top row
  - Use first row as headers
  - Name 1st column ⇒ Task
</details>

## Data cleaning

Use Query Editor to enrich your data:

- Unpivot the monthly data

![assets/Untitled%201.png](assets/Untitled%201.png)

*Output expected* 👆

- Add a conditional column, returning the correct `Month number` for each row (do the corresponding for the 12 months, it will be useful for the rest of this challenge)
- Now, we want to create a real datetime object for this column. Let's say these values were taken the 1st day of each month in 2020. Create a new column `Date task` with a date format.

<details><summary markdown='span'>Hint 💡
</summary>
  - Create an aggregated column you will transform in date format
  - `Date task = "01/" & [Month number] & "/2020"`
</details>

![assets/Untitled%202.png](assets/Untitled%202.png)

*Output expected* 👆

## Data visualization

Once your data is ok, bring it back into your Power BI report, and use it to create some chart.

- We want to visualize `the costs per month and per task` in a column chart.

    ⚠ As you can notice, your "Date task" column is divided into 4 parts (Year/Quarter/Month/Day). This notion will be covered in another course unit.

    For this challenge, just switch from "Date Hierarchy" to "Date task" to display the whole date.

    ![assets/Untitled%203.png](assets/Untitled%203.png)

![assets/Untitled%204.png](assets/Untitled%204.png)

*Chart expected* 👆

## Data automation

We've just received the second half values for this year and we want to display the exact same chart.

[Second half.xlsx](assets/Second_half.xlsx)

In order to refresh your data automatically, you have two ways for a flat file:

1. Name this new file with the **exact** designation of your first import and replace it in the same folder
2. Change the path in your datasource settings

    ![assets/Untitled%205.png](assets/Untitled%205.png)

Then refresh your data. Which method do you prefer?!

Save your file as **Date manipulation**. 💾
