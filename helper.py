import os 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

def directory():
	return os.getcwd()

def assets_directory():
	return directory() + '/90kDICT32px'

def store_dataframe_to_csv(df, filename, columns):
    df.to_csv(filename, columns = columns)