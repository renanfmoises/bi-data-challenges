## Background & Objectives

The goal of this challenge is to strenghten your data analyst mindset.

## Setup

It's time for more advanced analysis!

When planning to modify raw tables, creating a new sheet (or a new workbook) is generally a good idea.

Copy-paste the whole `orders` sheet and rename the newly created tab as `analysis`. Ensure that you disabled sorting from your previous challenge first.

<details><summary markdown='span'>Hint 💡
</summary>
  Just right click on the tab you want to copy and click `Move or Copy`.
</details>



## Joining orders and products

Name a new column `Unit Price`.

Using `INDEX MATCH`, write a formula filling this column with the corresponding price of the product, extracted from `products` tab.

Also add the unit cost in a `Unit Cost` column.

<details><summary markdown='span'>Hint 💡
</summary>
  Have you noted that adding a new product is made really easy thanks to this two tables structure? You'll see more about table relationship later.

  Note that we could have used a Merge query, as seen during class, with a larger dataset.
</details>

Check the solution in `challenge_2_solution_1`.

## Adding some calculation

Now that we have our prices and costs, we can do some maths in our `analysis` sheet.

- Add two columns `Revenue` and `Total Cost`, and fill it with the relevant formulas.
- Add a `Margin` column by substracting `Revenue` and `Total Cost`
- Add a `Margin` (%) column, showing the margin in percentage

Check the solution in `challenge_2_solution_2`.

## More analysis

We only did that calculation by row, which is interesting but seems insufficient: you can see that one Order ID can correspond to one or many rows.

So... we need to aggregate those rows in order to have a more precise idea of each order.

Let's build a brand new `order-details` blank sheet (tab).

1. First, select and copy `Order ID` and `Order Date` data together from `analysis`
2. In A1 cell of `order-details` tab, paste it
3. Remove duplicates of those columns at once.

    <details><summary markdown='span'>Hint 💡
    </summary>
      Click Data > Data Tools > Remove Duplicates

      ```
      We can delete duplicate on both columns because each order of the `Order ID` were necessarily placed at the same date!
      ```
    </details>

4. Using `SUMIFS` and your knowledge, create and fill a `Revenue` and `Total Cost` columns
5. Add a `Margin` column by substracting `Revenue` and `Total Cost`
6. Add a `Margin` (%) column, showing the margin in percentage

You now have a complete overview on orders and how much was spent for each of them!

Check the solution in `challenge_2_solution_3`.

## Metrics

Let's give your boss some reliable metrics!

Using `challenge_2_metrics` tab:

- Calculate the total revenue and total margin
- Get the max and min margin (%)
- Count orders
- Get the average order value

Check the solution in `challenge_2_solution_4`.
