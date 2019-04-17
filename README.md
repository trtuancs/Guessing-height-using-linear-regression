
# **Guessing height using linear regression**

## Description data

The table below gives the heights of fathers and their sons, based on a famous experiment by Karl Pearson around 1903. The number of cases is 1078. Random noise was added to the original data, to produce heights to the nearest 0.1 inch.

## Target

Guiessing son's height from father's height.

## Using Algorithm

Linear regression

## Steps to implement

1. Process data  
   - X: has shape: (1078,1) description son's height
   - Y: has shape: (1078,1) description father's height
2. Using linear regression algorithm
    - Calculation by formula: w = (X*X.T)^-1 *X*Y
    - Using Sklearn library : 
        - Using class linear_model.LinearRegression()
        - Using function fir in  linear_model.LinearRegression() : regr.fit(X,Y)

## Description project:

### src: containing file code (linear-regression.py)

### data: containing file data (Pearson.txt)