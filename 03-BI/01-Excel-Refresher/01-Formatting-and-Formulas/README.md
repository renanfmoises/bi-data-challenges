## Background & Objectives

The goal of this challenge is to learn how to explore and prepare an unknown dataset for your first analysis.

## Setup

Ready for a real world challenge?

Let's imagine you were just hired as an analyst in a [mall](https://www.youtube.com/watch?v=IY_bhVSGKEg).

The director wants an overview of the indian restaurant installed there for a few years, and gives you its financials from march to december 2016.

Let's work with the `indian_food_corner.xlsx` file.

[indian_food_corner.xlsx](https://wagon-public-datasets.s3.eu-west-1.amazonaws.com/bi-data/indian_food_corner.xlsx)

Open the Excel file, you can find two important tabs here, in red:

- First tab with all orders of the restaurant
- Second tab with price and cost for each product sold

The challenge tabs are where you will input your answers!

## Formatting Data

Order dates of the "orders" tab seem to be displayed the wrong way.

Show them in a "yyyy-mm-dd" format and sort it by ascending date without using Excel Table format.

<details><summary markdown='span'>Hint 💡
</summary>
Look in Data > Filter
</details>

## First Analysis

Let's have an overview of each tab's content.

Using `challenge_1_first_analysis` tab:

**Orders**

- Count the number of entries
- Count the average quantity per entry
- Count the median quantity ordered per entry

**Products**

- What is the average product price? And cost?
- Use this info to calculate the average gross margin rate in %
<details><summary markdown='span'>Hint 💡
</summary>
Gross margin rate = $(price - cost) / cost$
</details>



Check your answers with a right click on any tab, and unhide the tab `challenge_1_solution_1`.

## Let's dig further

The director needs some quick insight on certain products: let's play with *conditions*.

Using `challenge_1_dig_further` tab:

**Orders**

- Count how many entries contain the item `"Curry"`
- Sum-up all quantities of `"Curry"`
- How many entries after 1st of july 2016?
<details><summary markdown='span'>Hint 💡
</summary>
Use `DATE` in your formula
</details>



**Products**

- How many products contain the word `"Naan"`?
<details><summary markdown='span'>Hint 💡
</summary>
Do not forget to [do some research](https://www.google.com/search?q=Countifs+cell+contains+specific+text&rlz=1C1CHBF_frFR926FR926&sxsrf=ALeKk00nnDFK5qBirQY4Qz36htc07xeaag%3A1619446688458&ei=oMuGYM28G-OjgwfZ17-4Bw&oq=Countifs+cell+contains+specific+text&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEMsBMgYIABAIEB46BwgjELADECc6BwgAEEcQsAM6BggAEAcQHjoECAAQEzoKCAAQCBANEB4QE1DDOlisSWC1S2gGcAJ4AIABVYgBnQKSAQE1mAEAoAEBqgEHZ3dzLXdpesgBCcABAQ&sclient=gws-wiz&ved=0ahUKEwjNjOSEjZzwAhXj0eAKHdnrD3cQ4dUDCA4&uact=5) when you're stuck!
</details>

- How many products are sold at a price > $20?
- And between $10 and $20 included?

Check your answers.
