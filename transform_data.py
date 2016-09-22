import pandas as pd
file_name = 'data_england_test.csv'
fields = ['Result','Toss','Bat']
df = pd.read_csv(file_name,skipinitialspace=True,usecols=fields)
df.to_csv('data_england_test_filter.csv',index=False)

# Convert features and labels into digits
df_replace = df.replace(['lost','draw','won','1st','2nd'],[-1,0,1,-1,1])
dataset_length = len(df_replace)
# 67% of training data
ratio = 0.67
train_data_df = df_replace[:round(dataset_length*ratio)] # first 67% of data
test_data_df = df_replace[-(1-round(dataset_length*ratio)):] # rest for testing

# Create Respected CSV
train_data_df.to_csv('train.csv',index=False)
test_data_df.to_csv('test.csv',index=False)