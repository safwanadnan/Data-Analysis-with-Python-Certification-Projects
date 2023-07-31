# Mean-Variance-Standard Deviation Calculator

This project is a part of the Data Analysis with Python certification from freeCodeCamp.org. The objective is to create a Python function called `calculate()` that utilizes NumPy to calculate and return various statistical measures for a 3x3 matrix.

## Prerequisites

Before starting the project, make sure you have the following:

1. Access to the freeCodeCamp.org YouTube channel videos:
   - [Python for Everybody Video Course (14 hours)](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGpfAfDBiblRfl5p)
   - [How to Analyze Data with Python Pandas (10 hours)](https://www.youtube.com/watch?v=8y8Z6S0is3U)

2. Import the project on [Replit](https://replit.com/github/freeCodeCamp/boilerplate-mean-variance-standard-deviation-calculator) and set up the environment as instructed.

3. Familiarity with Python programming and the NumPy library.

## Project Description

### Task
Create a function named `calculate()` in `mean_var_std.py` that takes a list containing 9 digits as input. The function should convert the list into a 3x3 NumPy array and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

### Input
The input to the `calculate()` function should be a list containing exactly 9 digits.

### Output
The returned dictionary should follow this format:

```python
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
```

### Exception Handling
If a list containing less than 9 elements is passed into the function, it should raise a `ValueError` exception with the message: "List must contain nine numbers."

### Example
For example, `calculate([0,1,2,3,4,5,6,7,8])` should return:

```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## Development

### Testing
To test your implementation, you can use `main.py`. Click the "run" button, and `main.py` will execute the `calculate()` function.

### Submitting
Once you have completed the project, copy your project's URL from Replit and submit it to freeCodeCamp to complete the certification requirements.

Happy coding!
