import pandas as pd
from difflib import get_close_matches


class ExcelLookupEngine:

    def __init__(self, dataframe):

        self.df = dataframe

        self.report = []

    # ---------------------------------------------------
    # Exact Lookup
    # ---------------------------------------------------

    def exact_lookup(

        self,

        lookup_column,

        lookup_value,

        return_column

    ):

        result = self.df.loc[

            self.df[lookup_column] == lookup_value,

            return_column

        ]

        self.report.append(

            f"Exact Lookup : {lookup_value}"

        )

        if len(result) == 0:

            return None

        return result.iloc[0]

    # ---------------------------------------------------
    # Contains Search
    # ---------------------------------------------------

    def contains(

        self,

        column,

        text

    ):

        result = self.df[

            self.df[column]

            .astype(str)

            .str.contains(

                text,

                case=False,

                na=False

            )

        ]

        self.report.append(

            f"Contains Search : {text}"

        )

        return result

    # ---------------------------------------------------
    # Starts With
    # ---------------------------------------------------

    def starts_with(

        self,

        column,

        value

    ):

        result = self.df[

            self.df[column]

            .astype(str)

            .str.startswith(value)

        ]

        self.report.append(

            f"Starts With : {value}"

        )

        return result

    # ---------------------------------------------------
    # Ends With
    # ---------------------------------------------------

    def ends_with(

        self,

        column,

        value

    ):

        result = self.df[

            self.df[column]

            .astype(str)

            .str.endswith(value)

        ]

        self.report.append(

            f"Ends With : {value}"

        )

        return result

    # ---------------------------------------------------
    # Fuzzy Search
    # ---------------------------------------------------

    def fuzzy_search(

        self,

        column,

        keyword

    ):

        values = self.df[column].dropna().astype(str).tolist()

        matches = get_close_matches(

            keyword,

            values,

            n=10,

            cutoff=0.5

        )

        result = self.df[

            self.df[column].isin(matches)

        ]

        self.report.append(

            f"Fuzzy Search : {keyword}"

        )

        return result

    # ---------------------------------------------------
    # Duplicate Finder
    # ---------------------------------------------------

    def duplicates(

        self,

        column

    ):

        result = self.df[

            self.df.duplicated(

                subset=[column],

                keep=False

            )

        ]

        self.report.append(

            f"Duplicate Finder"

        )

        return result

    # ---------------------------------------------------
    # Unique Values
    # ---------------------------------------------------

    def unique_values(

        self,

        column

    ):

        self.report.append(

            "Unique Values"

        )

        return self.df[column].unique()

    # ---------------------------------------------------
    # Value Count
    # ---------------------------------------------------

    def frequency(

        self,

        column

    ):

        self.report.append(

            "Frequency Table"

        )

        return self.df[column].value_counts()

    # ---------------------------------------------------
    # Missing Values
    # ---------------------------------------------------

    def missing_rows(

        self,

        column

    ):

        result = self.df[

            self.df[column].isna()

        ]

        self.report.append(

            "Missing Rows"

        )

        return result

    # ---------------------------------------------------
    # Report
    # ---------------------------------------------------

    def get_report(self):

        return self.report