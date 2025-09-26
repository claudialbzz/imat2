import pandas as pd
import numpy as np
import re

def airbnb_read(path_to_file):
	df = pd.read_csv(path_to_file)
	return df

def airbnb_size(df):
	return df.shape

def airbnb_columns(df):
	return df.columns

def airbnb_countries(df):
	s = df['country'].astype(str).str.strip().str.title()
	return s.value_counts()

def airbnb_boroughs(df):
	s = df['neighbourhood group'].astype(str).str.strip().str.title()
	return s.value_counts()

def airbnb_price(df):
	df_new = df.copy()
	df_new['price'] = (
		df_new['price']
		.astype(str)
		.str.replace(r'[^0-9.]', '', regex=True)  # deja solo dígitos y punto
	)
	df_new['price'] = pd.to_numeric(df_new['price'], errors='coerce')
	df_new = df_new.dropna(subset=['price'])
	
	return df_new

def airbnb_aggregate(df):
    df_new = df.copy()
    df_new.columns = df_new.columns.str.strip().str.lower()
    df_new['price'] = (
        df_new['price']
        .astype(str)
        .str.replace(r'[^0-9.]', '', regex=True)
    )
    df_new['price'] = pd.to_numeric(df_new['price'], errors='coerce')
    df_new = df_new.dropna(subset=['price'])
    result = df_new.groupby(
        ['neighbourhood group', 'neighbourhood'], as_index=False
    ).agg(
        mean_price=('price', 'mean'),
        min_price=('price', 'min'),
        max_price=('price', 'max')
    )

    return result

def airbnb_totals():
	

#def population_totals():

#def airbnb_population():

if __name__ == "__main__":
	file_path_airbnb = '/Users/claudialbombin/Desktop/2025 -2026/Practicas/Adquisicion/P2/airbnb.csv'
	df = airbnb_read(file_path_airbnb)
	print(airbnb_aggregate(df))