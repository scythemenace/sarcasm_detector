import csv
import pandas as pd

# Read CSV
df = pd.read_csv("processed_data.csv")

# create new dataframe
new_df = pd.DataFrame()

i = 0
while i < 192:
    key = df.sample()                    # sample random key
    new_df = pd.concat([new_df, key])    # add key to new df
    df = df.drop(index=key.index)        # remove key from old df 
    # print(key.Key.values[0])      
    i+=1    

# Common 192 entries in file 1 and file 2
new_df.to_csv("data_1.csv", index=False) 
new_df.to_csv("data_2.csv", index=False)

# ------------------------------------------------------------------------------------------------------------------------------------------

# create new dataframe
new_df = pd.DataFrame()

i = 0
while i < 48:
    key = df.sample()                    # sample random key
    new_df = pd.concat([new_df, key])    # add key to new df
    df = df.drop(index=key.index)        # remove key from old df 
    # print(key.Key.values[0])      
    i+=1    

# Unique 48 entries in file 1 
new_df.to_csv("data_1.csv", index=False, mode="a", header=False) 

# ------------------------------------------------------------------------------------------------------------------------------------------

# create new dataframe
new_df = pd.DataFrame()

i = 0
while i < 48:
    key = df.sample()                    # sample random key
    new_df = pd.concat([new_df, key])    # add key to new df
    df = df.drop(index=key.index)        # remove key from old df 
    # print(key.Key.values[0])      
    i+=1    

# Unique 48 entries in file 2 
new_df.to_csv("data_2.csv", index=False, mode="a", header=False) 

# ------------------------------------------------------------------------------------------------------------------------------------------

# create new dataframe
new_df = pd.DataFrame()

i = 0
while i < 96:
    key = df.sample()                    
    new_df = pd.concat([new_df, key])    
    df = df.drop(index=key.index)       
    i+=1    

# Common 96 entries in file 3 and file 4
new_df.to_csv("data_3.csv", index=False) 
new_df.to_csv("data_4.csv", index=False) 

# ------------------------------------------------------------------------------------------------------------------------------------------

# create new dataframe
new_df = pd.DataFrame()

i = 0
while i < 144:
    key = df.sample()                    
    new_df = pd.concat([new_df, key])    
    df = df.drop(index=key.index)       
    i+=1    

# Unique 144 entries in file 3  
new_df.to_csv("data_3.csv", index=False, mode="a", header=False) 

# ------------------------------------------------------------------------------------------------------------------------------------------

# create new dataframe
new_df = pd.DataFrame()

i = 0
while i < 144:
    key = df.sample()                    
    new_df = pd.concat([new_df, key])    
    df = df.drop(index=key.index)       
    i+=1    

# Unique 144 entries in file   
new_df.to_csv("data_4.csv", index=False, mode="a", header=False) 

# ------------------------------------------------------------------------------------------------------------------------------------------

# create new dataframe
new_df = pd.DataFrame()

i = 0
while i < 240:
    key = df.sample()                    
    new_df = pd.concat([new_df, key])    
    df = df.drop(index=key.index)       
    i+=1    

# Unique 240 entries in file   
new_df.to_csv("data_5.csv", index=False) 

# ------------------------------------------------------------------------------------------------------------------------------------------

new_df = pd.DataFrame()

i = 0
while i < 240:
    key = df.sample()                    
    new_df = pd.concat([new_df, key])    
    df = df.drop(index=key.index)       
    i+=1    

# Unique 240 entries in file   
new_df.to_csv("data_6.csv", index=False) 

# ------------------------------------------------------------------------------------------------------------------------------------------

new_df = pd.DataFrame()

i = 0
while i < 240:
    key = df.sample()                    
    new_df = pd.concat([new_df, key])    
    df = df.drop(index=key.index)       
    i+=1    

# Unique 240 entries in file   
new_df.to_csv("data_7.csv", index=False) 

# ------------------------------------------------------------------------------------------------------------------------------------------

new_df = pd.DataFrame()

i = 0
while i < 240:
    key = df.sample()                    
    new_df = pd.concat([new_df, key])    
    df = df.drop(index=key.index)       
    i+=1    

# Unique 240 entries in file   
new_df.to_csv("data_8.csv", index=False) 
