import csv
import pandas as pd

data = [("101", 90), ("102", 80)]

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["StudentID", "Score"])
    writer.writerows(data)

try:
    df = pd.read_csv("results.csv")
    print(df)
except:
    print("File error")
