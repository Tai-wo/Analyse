import os
import uuid
import pandas as pd
import numpy as np


class ExcelCleaningEngine:

    def __init__(self, file_path: str):

        self.file_path = file_path

        self.report = {}

        self.df = self._load_file()

    def _load_file(self):

        extension = os.path.splitext(self.file_path)[1].lower()

        if extension == ".csv":

            return pd.read_csv(self.file_path)

        if extension in [".xlsx", ".xls"]:

            return pd.read_excel(self.file_path)

        raise Exception("Unsupported file type")

    def remove_duplicates(self):

        before = len(self.df)

        self.df = self.df.drop_duplicates()

        after = len(self.df)

        self.report["duplicates_removed"] = before - after

    def remove_blank_rows(self):

        before = len(self.df)

        self.df = self.df.dropna(how="all")

        after = len(self.df)

        self.report["blank_rows_removed"] = before - after

    def remove_blank_columns(self):

        before = len(self.df.columns)

        self.df = self.df.dropna(axis=1, how="all")

        after = len(self.df.columns)

        self.report["blank_columns_removed"] = before - after

    def trim_spaces(self):

        object_columns = self.df.select_dtypes(include="object").columns

        for column in object_columns:

            self.df[column] = self.df[column].astype(str).str.strip()

        self.report["spaces_trimmed"] = True

    def lowercase(self):

        object_columns = self.df.select_dtypes(include="object").columns

        for column in object_columns:

            self.df[column] = self.df[column].astype(str).str.lower()

        self.report["lowercase_applied"] = True

    def uppercase(self):

        object_columns = self.df.select_dtypes(include="object").columns

        for column in object_columns:

            self.df[column] = self.df[column].astype(str).str.upper()

        self.report["uppercase_applied"] = True

    def proper_case(self):

        object_columns = self.df.select_dtypes(include="object").columns

        for column in object_columns:

            self.df[column] = self.df[column].astype(str).str.title()

        self.report["proper_case_applied"] = True

    def fill_missing_values(self):

        numeric_columns = self.df.select_dtypes(include=np.number).columns

        text_columns = self.df.select_dtypes(exclude=np.number).columns

        for column in numeric_columns:

            self.df[column] = self.df[column].fillna(self.df[column].median())

        for column in text_columns:

            self.df[column] = self.df[column].fillna("Unknown")

        self.report["missing_values_filled"] = True

    def standardize_dates(self):

        for column in self.df.columns:

            try:

                self.df[column] = pd.to_datetime(self.df[column])

            except Exception:

                pass

        self.report["dates_standardized"] = True

    def remove_outliers_iqr(self):

        numeric = self.df.select_dtypes(include=np.number).columns

        removed = 0

        for column in numeric:

            q1 = self.df[column].quantile(0.25)

            q3 = self.df[column].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - (1.5 * iqr)

            upper = q3 + (1.5 * iqr)

            before = len(self.df)

            self.df = self.df[
                (self.df[column] >= lower) &
                (self.df[column] <= upper)
            ]

            removed += before - len(self.df)

        self.report["outliers_removed"] = removed

    def generate_summary(self):

        return {

            "rows": len(self.df),

            "columns": len(self.df.columns),

            "missing_values":

                self.df.isna().sum().sum(),

            "duplicates":

                self.df.duplicated().sum(),

            "memory":

                round(

                    self.df.memory_usage(deep=True).sum()

                    / 1024,

                    2

                )

        }

    def save(self):

        os.makedirs("generated_excel", exist_ok=True)

        filename = f"{uuid.uuid4().hex}.xlsx"

        output = os.path.join(

            "generated_excel",

            filename

        )

        self.df.to_excel(

            output,

            index=False

        )

        return output

    def get_report(self):

        return self.report