#question 6
import pandas as pd

def check_time_completeness(dataframe):
# Combine date and time columns to create datetime objects
dataframe['start_datetime'] = pd.to_datetime(dataframe['startDay'] + ' ' + dataframe['startTime'])
dataframe['end_datetime'] = pd.to_datetime(dataframe['endDay'] + ' ' + dataframe['endTime'])

# Check if the time range for each ("id", "id_2") pair covers a full 24-hour period and spans all 7 days
completeness_series = dataframe.groupby(['id', 'id_2']).apply(lambda group: check_time_range(group)).droplevel(2)

return completeness_series
def check_time_range(group):
# Check if the time range covers a full 24-hour period and spans all 7 days
start_time = group['start_datetime'].min().time()
end_time = group['end_datetime'].max().time()

return (end_time > start_time) and (group['start_datetime'].dt.dayofweek.nunique() == 7)
result = check_time_completeness(dataset_2)
print(result)

