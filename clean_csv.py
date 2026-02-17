import pandas as pd

def clean_csv(input_file, output_file):
    df = pd.read_csv(input_file)
    df_clean = df.dropna()
    df_clean.to_csv(output_file, index=False)
    print("CSV cleaned and saved as:", output_file)

# Example usage:
# clean_csv("data.csv", "cleaned_data.csv")
