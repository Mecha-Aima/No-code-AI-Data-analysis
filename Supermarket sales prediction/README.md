

# Supermarket Sales Forecasting with Akkio
=====================================

This use case explores the application of Akkio, a no-code AI tool, to predict supermarket sales based on customer and product-specific information.

## Dataset
----------

The dataset used for this project is a publicly available CSV file from Kaggle, containing approximately 10,000 rows of data. The dataset includes the following features:

* Customer ID
* Customer segment
* Shipment mode
* Customer name
* Region
* Category
* ...and others

The target variable is the **Sales** column, which is a continuous value.

## Methodology
--------------

Using Akkio's visual interface, I:

1. Loaded the CSV dataset into Akkio
2. Configured the model settings for regression
3. Trained the model on the dataset
4. Evaluated the model's performance using metrics such as mean absolute error (MAE) and mean squared error (MSE)
5. Generated predictions for the sales values

## Results
----------

Unfortunately, the model's predictions were not satisfactory, with a significant margin of error. This is likely due to the complexity of the problem and the limited amount of data cleaning and preprocessing performed.

## Challenges
------------

1. **Regression problem**: Estimating the exact sales value proved to be challenging, as the relationship between the features and target variable is complex.
2. **Large dataset**: With approximately 10,000 rows of data, the model's performance may have been impacted by the sheer volume of data.
3. **Limited data cleaning**: Further data cleaning and preprocessing may have improved the model's performance.
