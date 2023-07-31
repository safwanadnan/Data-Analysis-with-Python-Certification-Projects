# Medical Data Visualizer

In this project, you will be working with medical examination data using Matplotlib, Seaborn, and Pandas. The dataset contains information about patients' body measurements, blood test results, and lifestyle choices. Your task is to visualize the data and make some calculations to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

## Prerequisites

Before starting the project, make sure you have the following:

1. Access to the freeCodeCamp.org YouTube channel videos:
   - [Python for Everybody Video Course (14 hours)](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGpfAfDBiblRfl5p)
   - [How to Analyze Data with Python Pandas (10 hours)](https://www.youtube.com/watch?v=8y8Z6S0is3U)

2. Import the project on [Replit](https://replit.com/github/freeCodeCamp/boilerplate-medical-data-visualizer) and set up the environment as instructed.

3. Familiarity with Python programming, Matplotlib, Seaborn, and the Pandas library.

## Project Description

### Dataset

The dataset, `medical_examination.csv`, contains the following features:

- Age: age of the patient in days (int)
- Height: height of the patient in centimeters (int)
- Weight: weight of the patient in kilograms (float)
- Gender: gender of the patient (categorical code)
- Systolic blood pressure: examination feature, ap_hi (int)
- Diastolic blood pressure: examination feature, ap_lo (int)
- Cholesterol: examination feature, cholesterol (1: normal, 2: above normal, 3: well above normal)
- Glucose: examination feature, gluc (1: normal, 2: above normal, 3: well above normal)
- Smoking: subjective feature, smoke (binary)
- Alcohol intake: subjective feature, alco (binary)
- Physical activity: subjective feature, active (binary)
- Presence or absence of cardiovascular disease: target variable, cardio (binary)

### Tasks

You are required to complete the following tasks in `medical_data_visualizer.py`:

1. Create a chart similar to `examples/Figure_1.png`, showing the counts of good and bad outcomes for the `cholesterol`, `gluc`, `alco`, `active`, and `smoke` variables for patients with `cardio=1` and `cardio=0` in different panels.

2. Add an `overweight` column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25, then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.

3. Normalize the data by making 0 always good and 1 always bad. If the value of `cholesterol` or `gluc` is 1, make the value 0. If the value is more than 1, make the value 1.

4. Convert the data into long format and create a chart that shows the value counts of the categorical features using Seaborn's `catplot()`. The dataset should be split by 'Cardio', so there is one chart for each cardio value. The chart should look like `examples/Figure_1.png`.

5. Clean the data by filtering out incorrect data segments:
   - Diastolic pressure is higher than systolic (Keep the correct data with `(df['ap_lo'] <= df['ap_hi'])`)
   - Height is less than the 2.5th percentile (Keep the correct data with `(df['height'] >= df['height'].quantile(0.025))`)
   - Height is more than the 97.5th percentile
   - Weight is less than the 2.5th percentile
   - Weight is more than the 97.5th percentile

6. Create a correlation matrix using the dataset and plot it using Seaborn's `heatmap()`. Mask the upper triangle. The chart should look like `examples/Figure_2.png`.

### Development

#### Testing
To test your implementation, you can use `main.py`. Click the "run" button, and `main.py` will execute the functions defined in `medical_data_visualizer.py`.

### Submitting
Once you have completed the project, copy your project's URL from Replit and submit it to freeCodeCamp to complete the certification requirements.

Happy visualizing!
