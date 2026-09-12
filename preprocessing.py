import numpy as np
import pandas as pd
# Set option to display all columns
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', none)
# Set display option in pandas to show floats with thousand separators
pd.options.display.float_format = '{:,.1f}'.format
# Display multiple Variables without print() statements
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

df = pd.read_csv("D:/TMDB_all_movies.csv")
# Converting columns
df['revenue'] = df['revenue'].astype(float)
df['budget'] = df['budget'].astype(float)
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
# errors='coerce' will convert invalid parsing to NaT
df['year'] = df['release_date'].dt.year.astype('Int64') # Use 'Int64' to allow for NaN values
threshold = len(df) * 0.5 # Tính toán ngưỡng: 50% của số lượng hàng
df = df.dropna(thresh=threshold, axis=1)
df = df.drop(columns=['original_title'])
df=df.dropna()
# Lọc ra những bộ phim được phát hành từ năm 2000 trở lại
df = df[df["release_date"].dt.year >= 2000]
df.to_csv("Final_TMDB_Movies.csv", index=False)