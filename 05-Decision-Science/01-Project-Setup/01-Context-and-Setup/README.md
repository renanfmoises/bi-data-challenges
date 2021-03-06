## Objectives of the week

We will analyze a dataset imported from [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce) that was provided by a Brazilian e-commerce marketplace calledΒ [Olist](https://www.olist.com)Β to answer the following CEOβs question:


> How to increase profit margin (focusing on customer satisfaction) while maintaining a healthy order volume?

## About Olist π§π·

<img src="https://raw.githubusercontent.com/lewagon/data-images/master/best-practices/olist.png" width="500"/>

Olist is a leading e-commerce service that connects merchants to main marketplaces in Brazil. They provide a wide range of offers including inventory management, dealing with reviews and customer contacts to logistic services.

Olist charges sellers a monthly fee. This fee is progressive with the volume of orders.

Here are the seller and customer workflows:

**Seller:**

- Seller joins Olist
- Seller uploads products catalogue
- Seller gets notified when a product is sold
- Seller hands over an item to the logistic carrier

π Note that multiple sellers can be involved in one customer order!

**Customer:**

- Browses products on the marketplace
- Purchases products from Olist.store
- Gets an expected date for delivery
- Receives the order
- Leaves a review about the order

π A review can be left as soon as the order is sent, meaning that a customer can leave a review for a product he did not receive yet!

## Dataset

The dataset consists of 100k orders from 2016 and 2018 that were made on the Olist store, available as a csv on [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce)

β Download the 9 datasets and store them in your `~/code/<user.github_nickname>/data-challenges/04-Decision-Science/data` folder.

## Setup

### 1 - Project Structure
Go to your local `04-Decision-Science` folder.
This will be your project structure for the week.

```bash
.
βββ 01 - Project-Setup             # your notebooks & analyses, day-by-day
βββ 02 - Excel and Power Query
βββ 03 - Power Pivot Model
βββ 04 - Creating a Dashboard
βββ 05 - Communicate
|
βββ data                        # Your data source (git ignored)
|   βββ csv
|   |   βββ olist_customers_dataset.csv
|   |   βββ olist_orders_dataset.csv
|   |   βββ ...
|   βββ README.md   # database documentation

```

