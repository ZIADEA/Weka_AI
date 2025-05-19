import pandas as pd

def csv_to_arff(csv_file, arff_file, relation_name="relation"):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Open the ARFF file for writing
    with open(arff_file, 'w') as f:
        # Write the relation name
        f.write(f"@relation {relation_name}\n\n")
        
        # Write the attribute section
        for column in df.columns:
            if df[column].dtype == 'object':
                # Nominal attribute
                unique_values = df[column].unique()
                values = ",".join([f"'{v}'" for v in unique_values])
                f.write(f"@attribute {column} {{{values}}}\n")
            elif df[column].dtype in ['int64', 'float64']:
                # Numeric attribute
                f.write(f"@attribute {column} numeric\n")
            else:
                # Handle other data types if necessary
                f.write(f"@attribute {column} string\n")
        
        f.write("\n@data\n")
        
        # Write the data section
        for _, row in df.iterrows():
            row_data = ",".join([f"'{v}'" if isinstance(v, str) else str(v) for v in row])
            f.write(f"{row_data}\n")

# Example usage
csv_to_arff("Dataset.csv", "Dataset.arff", relation_name="my_relation")


