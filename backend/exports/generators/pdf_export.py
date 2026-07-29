import pandas as pd
import os


def generate_pdf_report(file_path: str):

    df = pd.read_csv(file_path)

    summary = df.describe().to_string()

    output_path = "exports/report.txt"

    os.makedirs("exports", exist_ok=True)

    with open(output_path, "w") as f:

        f.write("DATASET REPORT\n\n")

        f.write(summary)

    return output_path