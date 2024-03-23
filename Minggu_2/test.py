import pandas as pandas

# Create a sample dataframe
df = pd.DataFrame({'Name': ['John','Emma','Peter','Maria'],
                    'Age': [25,30,20,35],
                    'Gender': ['Male', 'Female', 'Male', 'Female']})

# Print the dataframe
print(df)

# Read a CSV file into a dataframe
csv_df = pd.read_csv('sample.csv')

# Print the dataframe
print(csv_df)

#Group the dataframe by Gender and calculate the mean age
grouped_df = df.groupby('Gender').mean()

# Print the grouped dataframe
print(grouped_df)