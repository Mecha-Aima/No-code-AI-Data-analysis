import pandas as pd
import numpy as np

# Read the csv file
df = pd.read_csv('fraudTest.csv')

# Select the is_fraud column and assign a value of 1 to half of its cells chosen at random
df['is_fraud'] = np.where(np.random.rand(len(df)) < 0.5, 1, df['is_fraud'])

# Write the dataframe to a new csv file
df.to_csv('fraudDetect.csv', index=False)
    
    
    
    
