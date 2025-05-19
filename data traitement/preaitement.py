import os
import pandas as pd

folder = "C:/Users/DELL/Downloads/1st_test/1st_test"
all_data = []

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    df = pd.read_csv(path, sep="\s+", header=None)  # fichier sans entête
    row_mean = df.mean().values  # moyenne des colonnes du fichier
    all_data.append(row_mean)

result = pd.DataFrame(all_data, columns=[f"sensor_{i}" for i in range(len(all_data[0]))])
result.to_csv("bearing_data1.csv", index=False)

