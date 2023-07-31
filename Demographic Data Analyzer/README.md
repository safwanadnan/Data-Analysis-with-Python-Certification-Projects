# Demographic Data Analyzer

This project involves analyzing demographic data using Pandas. The dataset used for analysis is extracted from the 1994 Census database. The goal is to answer various questions based on the dataset using Pandas operations.

## Prerequisites

Before starting the project, make sure you have the following:

1. Access to the freeCodeCamp.org YouTube channel videos:
   - [Python for Everybody Video Course (14 hours)](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGpfAfDBiblRfl5p)
   - [How to Analyze Data with Python Pandas (10 hours)](https://www.youtube.com/watch?v=8y8Z6S0is3U)

2. Import the project on [Replit](https://replit.com/github/freeCodeCamp/boilerplate-demographic-data-analyzer) and set up the environment as instructed.

3. Familiarity with Python programming and the Pandas library.

## Project Description

### Dataset

The dataset contains demographic data with the following columns:

|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |

### Questions to Answer

You must use Pandas to answer the following questions based on the dataset:

1. How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels (race column).
2. What is the average age of men?
3. What is the percentage of people who have a Bachelor's degree?
4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
5. What percentage of people without advanced education make more than 50K?
6. What is the minimum number of hours a person works per week?
7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
8. What country has the highest percentage of people that earn >50K, and what is that percentage?
9. Identify the most popular occupation for those who earn >50K in India.

### Starter Code

You will find the starter code in the file `demographic_data_analyzer.py`. Update the code so all variables set to "None" are set to the appropriate calculation or code. Round all decimals to the nearest tenth.

## Development

### Testing
To test your implementation, you can use `main.py`. Click the "run" button, and `main.py` will execute the functions defined in `demographic_data_analyzer.py`.

### Submitting
Once you have completed the project, copy your project's URL from Replit and submit it to freeCodeCamp to complete the certification requirements.

## Dataset Source
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.

Happy analyzing!
