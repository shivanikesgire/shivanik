import pandas as pd

def get_type_count(dataframe):
# Add a new column 'car_type' based on the specified conditions
dataframe['car_type'] = pd.cut(dataframe['car'],
bins=[-float('inf'), 15, 25, float('inf')],
labels=['low', 'medium', 'high'],
right=False)

# Calculate the count of occurrences for each 'car_type' category
type_count = dataframe['car_type'].value_counts().to_dict()

# Sort the dictionary alphabetically based on keys
sorted_type_count = dict(sorted(type_count.items()))

return sorted_type_count
result = get_type_count(dataset)
print(result)
