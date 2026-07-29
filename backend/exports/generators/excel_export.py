import pandas as pd
import os


def generate_excel_file(file_path: str):

    df = pd.read_csv(file_path)

    df = df.drop_duplicates()

    df = df.fillna(method='ffill')

    output_path = "exports/cleaned_data.xlsx"

    os.makedirs("exports", exist_ok=True)

    df.to_excel(output_path, index=False)

    return output_path