import pandas as pd

week1='/Users/kanumadhok/Desktop/UChicago/nfl_project/NFL_Tackling_Analysis/tracking_week_1.csv'
week2='/Users/kanumadhok/Desktop/UChicago/nfl_project/NFL_Tackling_Analysis/tracking_week_2.csv'
week3='/Users/kanumadhok/Desktop/UChicago/nfl_project/NFL_Tackling_Analysis/tracking_week_3.csv'
week4='/Users/kanumadhok/Desktop/UChicago/nfl_project/NFL_Tackling_Analysis/tracking_week_4.csv'
week5='/Users/kanumadhok/Desktop/UChicago/nfl_project/NFL_Tackling_Analysis/tracking_week_5.csv'
week6='/Users/kanumadhok/Desktop/UChicago/nfl_project/NFL_Tackling_Analysis/tracking_week_6.csv'
week7='/Users/kanumadhok/Desktop/UChicago/nfl_project/NFL_Tackling_Analysis/tracking_week_7.csv'
week8='/Users/kanumadhok/Desktop/UChicago/nfl_project/NFL_Tackling_Analysis/tracking_week_8.csv'
week9='/Users/kanumadhok/Desktop/UChicago/nfl_project/NFL_Tackling_Analysis/tracking_week_9.csv'
from pyarrow import csv, parquet
from datetime import datetime


# Week 1
table1 = csv.read_csv(week1)
parquet.write_table(table1, 'week1.parquet')

# Week 2
table2 = csv.read_csv(week2)
parquet.write_table(table2, 'week2.parquet')

# Week 3
table3 = csv.read_csv(week3)
parquet.write_table(table3, 'week3.parquet')

# Week 4
table4 = csv.read_csv(week4)
parquet.write_table(table4, 'week4.parquet')

# Week 5
table5 = csv.read_csv(week5)
parquet.write_table(table5, 'week5.parquet')

# Week 6
table6 = csv.read_csv(week6)
parquet.write_table(table6, 'week6.parquet')

# Week 7
table7 = csv.read_csv(week7)
parquet.write_table(table7, 'week7.parquet')

# Week 8
table8 = csv.read_csv(week8)
parquet.write_table(table8, 'week8.parquet')

# Week 9
table9 = csv.read_csv(week9)
parquet.write_table(table9, 'week9.parquet')