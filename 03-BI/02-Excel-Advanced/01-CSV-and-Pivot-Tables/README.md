Now that you become more and more familiar with Excel, let's work on another case study!

As a senior business analyst in an international retail company, you were asked to analyze the Myanmar market and build a report.

## Background & Objectives

The goal of this challenge is to create your first Pivot Table analysis, using a CSV file.

## Importing a CSV file

Please download [supermarket_sales.csv](https://wagon-public-datasets.s3.eu-west-1.amazonaws.com/bi-data/supermarket_sales.csv) and [supermarket_study.xlsx](https://wagon-public-datasets.s3.eu-west-1.amazonaws.com/bi-data/supermarket_study.xlsx).

Open `supermarket_study.xlsx`. It will be your main workbook.

<details><summary markdown='span'>Hint 💡
</summary>
  We could assume that `supermarket_sales.csv` can be opened directly, isn't it ? After all there is an Excel logo on it.

  Yes it can, but it won't always work depending on .csv source. The import CSV tool is always to be chosen to avoid formatting issues!
</details>

Import `supermarket_sales.csv` (do not forget to check the preview!) and load it as seen during our lesson. The tab should be named `Raw Data`.

⚠️ Immediately check for number format. Depending of the regional settings of your computer, Excel may have not recognized dot decimal separators as it should.

🚧 To verify that dot decimals were interpreted the right way, just select some cells on what should be a numbered column. If an average and a sum are displayed at the bottom of your window, you can just continue. 

![https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/03-BI/02-Excel-Advanced/01-CSV-and-Pivot-Tables/Untitled.png](https://raw.githubusercontent.com/lewagon/data-images/master/bi-data/03-BI/02-Excel-Advanced/01-CSV-and-Pivot-Tables/Untitled.png)

You'll learn how to get along with that problem in the Query Editor unit (basically, force a change on separator).

In case of troubles, you can unhide then copy `challenge_1_solution_1` tab and use it as `Raw Data` tab.

Format Date column as "yyyy-mm-dd" and transform gross margin percentage in real percentage (%) with two digits.

Unhide `challenge_1_solution_1` to see or copy the solution.

## Playing with Pivot Tables

Remember the powerful Pivot Tables? Time to use it! 

You have many columns and it will allow you to create some insights on all that data. 

Go to Insert > Pivot Table and create a new Pivot Table on a new sheet. Call that tab `Cities Study`.

Let's try a first calculation:

- On the right ribbon, check fields `Total` and `City`: you should have the total revenue per city. Amazingly easy, no?
- Now check `Gender`. Move it from Rows to Columns: what do you notice?
<details><summary markdown='span'>Hint 💡
</summary>
  Avoid as much as possible to add more than one field on the Rows area.

  Nested rows tables are not easily workable when exported or used in reports.
</details>

- Check `Date`, Years, Quarters and Date appearing in Rows. Delete Quarters and Date, and move Years to the Filter area. You can now select a specific year to get the Grand Total.

You now understand why Pivot Tables are a must know. It improves greatly your productivity at the time of examining a dataset.

Check the solution in `challenge_1_table_1`.

## Your turn!

Create the following tables:

- Total revenue and average rating by product lines (solution in `challenge_1_table_2`)
- Average basket by customer types per year (solution in `challenge_1_table_3`)
- Count of quantities and average 5% tax per month (solution in `challenge_1_table_4`)
- Quarterly total for female clients per payment type (solution in `challenge_1_table_5`)
