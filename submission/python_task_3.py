#question 5
import pandas as pd

def multiply_matrix(input_dataframe):
# Create a copy of the input DataFrame to avoid modifying the original data
modified_dataframe = input_dataframe.copy()

# Apply the specified logic to modify values in the DataFrame
modified_dataframe = modified_dataframe.applymap(
    lambda x: x * 0.75 if x > 20 else x * 1.25
)

# Round the values to 1 decimal place
modified_dataframe = modified_dataframe.round(1)

return modified_dataframe
result = multiply_matrix(resulting_dataframe)
print(result)
