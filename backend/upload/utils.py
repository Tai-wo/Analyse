import os
import pandas as pd


def load_dataframe(file_path):

    extension = os.path.splitext(
        file_path
    )[1].lower()

    if extension == ".csv":

        try:

            df = pd.read_csv(
                file_path,
                encoding="utf-8"
            )

        except UnicodeDecodeError:

            df = pd.read_csv(
                file_path,
                encoding="latin1"
            )

    elif extension == ".xlsx":

        df = pd.read_excel(
            file_path,
            engine="openpyxl"
        )

    elif extension == ".xls":

        df = pd.read_excel(
            file_path
        )

    else:

        raise Exception(
            f"Unsupported file format: {extension}"
        )

    return df


def analyze_file(file_path):

    df = load_dataframe(
        file_path
    )

    rows = len(df)

    columns = len(df.columns)

    return rows, columns