import pandas as pd


class ExcelPivotEngine:

    def __init__(self, dataframe):

        self.df = dataframe

        self.report = []

    # ---------------------------------------------------
    # Basic Pivot
    # ---------------------------------------------------

    def pivot(

        self,

        index,

        values,

        aggfunc="sum"

    ):

        table = pd.pivot_table(

            self.df,

            index=index,

            values=values,

            aggfunc=aggfunc,

            fill_value=0

        )

        self.report.append(

            f"Pivot created using {aggfunc}"

        )

        return table

    # ---------------------------------------------------
    # Row + Column Pivot
    # ---------------------------------------------------

    def pivot_matrix(

        self,

        rows,

        columns,

        values,

        aggfunc="sum"

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            columns=columns,

            values=values,

            aggfunc=aggfunc,

            fill_value=0

        )

        self.report.append(

            "Pivot Matrix Created"

        )

        return table

    # ---------------------------------------------------
    # Multi Index Pivot
    # ---------------------------------------------------

    def multi_index(

        self,

        rows,

        values,

        aggfunc="sum"

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            values=values,

            aggfunc=aggfunc,

            fill_value=0

        )

        self.report.append(

            "Multi Index Pivot"

        )

        return table

    # ---------------------------------------------------
    # Count Pivot
    # ---------------------------------------------------

    def count(

        self,

        rows,

        values

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            values=values,

            aggfunc="count",

            fill_value=0

        )

        self.report.append(

            "Count Pivot"

        )

        return table

    # ---------------------------------------------------
    # Average Pivot
    # ---------------------------------------------------

    def average(

        self,

        rows,

        values

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            values=values,

            aggfunc="mean",

            fill_value=0

        )

        self.report.append(

            "Average Pivot"

        )

        return table

    # ---------------------------------------------------
    # Minimum Pivot
    # ---------------------------------------------------

    def minimum(

        self,

        rows,

        values

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            values=values,

            aggfunc="min",

            fill_value=0

        )

        self.report.append(

            "Minimum Pivot"

        )

        return table

    # ---------------------------------------------------
    # Maximum Pivot
    # ---------------------------------------------------

    def maximum(

        self,

        rows,

        values

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            values=values,

            aggfunc="max",

            fill_value=0

        )

        self.report.append(

            "Maximum Pivot"

        )

        return table

    # ---------------------------------------------------
    # Median Pivot
    # ---------------------------------------------------

    def median(

        self,

        rows,

        values

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            values=values,

            aggfunc="median",

            fill_value=0

        )

        self.report.append(

            "Median Pivot"

        )

        return table

    # ---------------------------------------------------
    # Standard Deviation
    # ---------------------------------------------------

    def std(

        self,

        rows,

        values

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            values=values,

            aggfunc="std",

            fill_value=0

        )

        self.report.append(

            "Standard Deviation Pivot"

        )

        return table

    # ---------------------------------------------------
    # Variance
    # ---------------------------------------------------

    def variance(

        self,

        rows,

        values

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            values=values,

            aggfunc="var",

            fill_value=0

        )

        self.report.append(

            "Variance Pivot"

        )

        return table

    # ---------------------------------------------------
    # Crosstab
    # ---------------------------------------------------

    def cross_tab(

        self,

        row,

        column

    ):

        table = pd.crosstab(

            self.df[row],

            self.df[column]

        )

        self.report.append(

            "Cross Tab Created"

        )

        return table

    # ---------------------------------------------------
    # Export
    # ---------------------------------------------------

    def export(

        self,

        dataframe,

        output_path

    ):

        dataframe.to_excel(

            output_path,

            index=True

        )

        self.report.append(

            f"Exported -> {output_path}"

        )

            # ---------------------------------------------------
    # Multiple Aggregations
    # ---------------------------------------------------

    def multiple_aggregations(

        self,

        rows,

        values,

        aggregations

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            values=values,

            aggfunc=aggregations,

            fill_value=0

        )

        self.report.append(

            "Multiple Aggregations"

        )

        return table

    # ---------------------------------------------------
    # Grand Totals
    # ---------------------------------------------------

    def pivot_with_totals(

        self,

        rows,

        values,

        aggfunc="sum"

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            values=values,

            aggfunc=aggfunc,

            margins=True,

            margins_name="Grand Total",

            fill_value=0

        )

        self.report.append(

            "Grand Totals Added"

        )

        return table

    # ---------------------------------------------------
    # Row and Column Totals
    # ---------------------------------------------------

    def matrix_with_totals(

        self,

        rows,

        columns,

        values,

        aggfunc="sum"

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            columns=columns,

            values=values,

            aggfunc=aggfunc,

            margins=True,

            margins_name="Grand Total",

            fill_value=0

        )

        self.report.append(

            "Matrix Totals"

        )

        return table

    # ---------------------------------------------------
    # Percentage of Grand Total
    # ---------------------------------------------------

    def percent_of_total(

        self,

        rows,

        values

    ):

        pivot = pd.pivot_table(

            self.df,

            index=rows,

            values=values,

            aggfunc="sum",

            fill_value=0

        )

        pivot["Percent"] = (

            pivot[values]

            /

            pivot[values].sum()

        ) * 100

        self.report.append(

            "Percent Of Total"

        )

        return pivot

    # ---------------------------------------------------
    # Percentage Within Group
    # ---------------------------------------------------

    def percent_by_group(

        self,

        group,

        values

    ):

        result = (

            self.df

            .groupby(group)[values]

            .sum()

            .pipe(

                lambda x:

                x / x.sum() * 100

            )

            .to_frame("Percent")

        )

        self.report.append(

            "Percent By Group"

        )

        return result

    # ---------------------------------------------------
    # Running Total
    # ---------------------------------------------------

    def running_total(

        self,

        group,

        values

    ):

        data = self.df.copy()

        data["Running Total"] = (

            data

            .groupby(group)[values]

            .cumsum()

        )

        self.report.append(

            "Running Total"

        )

        return data

    # ---------------------------------------------------
    # Ranking
    # ---------------------------------------------------

    def ranking(

        self,

        group,

        values,

        ascending=False

    ):

        result = (

            self.df

            .groupby(group)[values]

            .sum()

            .rank(

                ascending=ascending,

                method="dense"

            )

        )

        self.report.append(

            "Ranking"

        )

        return result

    # ---------------------------------------------------
    # Top N
    # ---------------------------------------------------

    def top_n(

        self,

        group,

        values,

        n=10

    ):

        result = (

            self.df

            .groupby(group)[values]

            .sum()

            .sort_values(

                ascending=False

            )

            .head(n)

        )

        self.report.append(

            f"Top {n}"

        )

        return result

    # ---------------------------------------------------
    # Bottom N
    # ---------------------------------------------------

    def bottom_n(

        self,

        group,

        values,

        n=10

    ):

        result = (

            self.df

            .groupby(group)[values]

            .sum()

            .sort_values(

                ascending=True

            )

            .head(n)

        )

        self.report.append(

            f"Bottom {n}"

        )

        return result

    # ---------------------------------------------------
    # Multiple Value Columns
    # ---------------------------------------------------

    def multi_values(

        self,

        rows,

        values,

        aggfunc="sum"

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            values=values,

            aggfunc=aggfunc,

            fill_value=0

        )

        self.report.append(

            "Multiple Value Pivot"

        )

        return table
    
        # ---------------------------------------------------
    # Hierarchical Pivot
    # ---------------------------------------------------

    def hierarchical_pivot(

        self,

        rows,

        columns,

        values,

        aggfunc="sum"

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            columns=columns,

            values=values,

            aggfunc=aggfunc,

            fill_value=0,

            sort=True

        )

        self.report.append(

            "Hierarchical Pivot"

        )

        return table

    # ---------------------------------------------------
    # Multi-Level Columns
    # ---------------------------------------------------

    def multi_level_columns(

        self,

        rows,

        columns,

        values,

        aggregations

    ):

        table = pd.pivot_table(

            self.df,

            index=rows,

            columns=columns,

            values=values,

            aggfunc=aggregations,

            fill_value=0

        )

        self.report.append(

            "Multi-Level Columns"

        )

        return table

    # ---------------------------------------------------
    # Group by Multiple Columns
    # ---------------------------------------------------

    def group_multiple(

        self,

        groups,

        values,

        aggfunc="sum"

    ):

        result = (

            self.df

            .groupby(groups)[values]

            .agg(aggfunc)

            .reset_index()

        )

        self.report.append(

            "Grouped Multiple Columns"

        )

        return result

    # ---------------------------------------------------
    # Drill Down
    # ---------------------------------------------------

    def drill_down(

        self,

        filters

    ):

        data = self.df.copy()

        for column, value in filters.items():

            data = data[data[column] == value]

        self.report.append(

            "Drill Down"

        )

        return data

    # ---------------------------------------------------
    # Drill Up
    # ---------------------------------------------------

    def drill_up(

        self,

        group,

        values,

        aggfunc="sum"

    ):

        table = (

            self.df

            .groupby(group)[values]

            .agg(aggfunc)

            .reset_index()

        )

        self.report.append(

            "Drill Up"

        )

        return table

    # ---------------------------------------------------
    # Filter Pivot
    # ---------------------------------------------------

    def filter_pivot(

        self,

        rows,

        values,

        filter_column,

        filter_value,

        aggfunc="sum"

    ):

        filtered = self.df[

            self.df[filter_column] == filter_value

        ]

        table = pd.pivot_table(

            filtered,

            index=rows,

            values=values,

            aggfunc=aggfunc,

            fill_value=0

        )

        self.report.append(

            "Filtered Pivot"

        )

        return table

    # ---------------------------------------------------
    # Sort Pivot
    # ---------------------------------------------------

    def sort_pivot(

        self,

        dataframe,

        column,

        ascending=False

    ):

        self.report.append(

            "Sorted Pivot"

        )

        return dataframe.sort_values(

            by=column,

            ascending=ascending

        )

    # ---------------------------------------------------
    # Year Grouping
    # ---------------------------------------------------

    def group_year(

        self,

        date_column

    ):

        data = self.df.copy()

        data[date_column] = pd.to_datetime(

            data[date_column]

        )

        data["Year"] = data[date_column].dt.year

        self.report.append(

            "Year Group"

        )

        return data

    # ---------------------------------------------------
    # Quarter Grouping
    # ---------------------------------------------------

    def group_quarter(

        self,

        date_column

    ):

        data = self.df.copy()

        data[date_column] = pd.to_datetime(

            data[date_column]

        )

        data["Quarter"] = data[date_column].dt.quarter

        self.report.append(

            "Quarter Group"

        )

        return data

    # ---------------------------------------------------
    # Month Grouping
    # ---------------------------------------------------

    def group_month(

        self,

        date_column

    ):

        data = self.df.copy()

        data[date_column] = pd.to_datetime(

            data[date_column]

        )

        data["Month"] = data[date_column].dt.month_name()

        self.report.append(

            "Month Group"

        )

        return data

    # ---------------------------------------------------
    # Week Grouping
    # ---------------------------------------------------

    def group_week(

        self,

        date_column

    ):

        data = self.df.copy()

        data[date_column] = pd.to_datetime(

            data[date_column]

        )

        data["Week"] = data[date_column].dt.isocalendar().week

        self.report.append(

            "Week Group"

        )

        return data

    # ---------------------------------------------------
    # Day Grouping
    # ---------------------------------------------------

    def group_day(

        self,

        date_column

    ):

        data = self.df.copy()

        data[date_column] = pd.to_datetime(

            data[date_column]

        )

        data["Day"] = data[date_column].dt.day_name()

        self.report.append(

            "Day Group"

        )

        return data
    
        # ---------------------------------------------------
    # Calculated Field
    # ---------------------------------------------------

    def calculated_field(

        self,

        new_column,

        formula

    ):

        data = self.df.copy()

        data[new_column] = data.eval(formula)

        self.report.append(

            f"Calculated Field : {new_column}"

        )

        return data

    # ---------------------------------------------------
    # Profit Margin
    # ---------------------------------------------------

    def profit_margin(

        self,

        revenue_column,

        cost_column

    ):

        data = self.df.copy()

        data["Profit"] = (

            data[revenue_column]

            -

            data[cost_column]

        )

        data["Profit Margin (%)"] = (

            data["Profit"]

            /

            data[revenue_column]

        ) * 100

        self.report.append(

            "Profit Margin Calculated"

        )

        return data

    # ---------------------------------------------------
    # Growth Rate
    # ---------------------------------------------------

    def growth_rate(

        self,

        column

    ):

        data = self.df.copy()

        data["Growth Rate (%)"] = (

            data[column]

            .pct_change()

            * 100

        )

        self.report.append(

            "Growth Rate"

        )

        return data

    # ---------------------------------------------------
    # Percentage Difference
    # ---------------------------------------------------

    def percent_difference(

        self,

        column1,

        column2

    ):

        data = self.df.copy()

        data["Percent Difference"] = (

            (

                data[column1]

                -

                data[column2]

            )

            /

            data[column2]

        ) * 100

        self.report.append(

            "Percentage Difference"

        )

        return data

    # ---------------------------------------------------
    # Running Average
    # ---------------------------------------------------

    def running_average(

        self,

        column

    ):

        data = self.df.copy()

        data["Running Average"] = (

            data[column]

            .expanding()

            .mean()

        )

        self.report.append(

            "Running Average"

        )

        return data

    # ---------------------------------------------------
    # Cumulative Percentage
    # ---------------------------------------------------

    def cumulative_percentage(

        self,

        column

    ):

        data = self.df.copy()

        cumulative = data[column].cumsum()

        data["Cumulative %"] = (

            cumulative

            /

            data[column].sum()

        ) * 100

        self.report.append(

            "Cumulative Percentage"

        )

        return data

    # ---------------------------------------------------
    # Contribution Analysis
    # ---------------------------------------------------

    def contribution(

        self,

        column

    ):

        data = self.df.copy()

        total = data[column].sum()

        data["Contribution (%)"] = (

            data[column]

            /

            total

        ) * 100

        self.report.append(

            "Contribution Analysis"

        )

        return data

    # ---------------------------------------------------
    # Difference From Average
    # ---------------------------------------------------

    def difference_from_average(

        self,

        column

    ):

        data = self.df.copy()

        average = data[column].mean()

        data["Difference From Average"] = (

            data[column]

            -

            average

        )

        self.report.append(

            "Difference From Average"

        )

        return data

    # ---------------------------------------------------
    # Z Score
    # ---------------------------------------------------

    def z_score(

        self,

        column

    ):

        data = self.df.copy()

        mean = data[column].mean()

        std = data[column].std()

        data["Z Score"] = (

            data[column]

            -

            mean

        ) / std

        self.report.append(

            "Z Score"

        )

        return data

    # ---------------------------------------------------
    # Normalize
    # ---------------------------------------------------

    def normalize(

        self,

        column

    ):

        data = self.df.copy()

        minimum = data[column].min()

        maximum = data[column].max()

        data["Normalized"] = (

            data[column]

            -

            minimum

        ) / (

            maximum

            -

            minimum

        )

        self.report.append(

            "Normalization"

        )

        return data

    # ---------------------------------------------------
    # Weighted Average
    # ---------------------------------------------------

    def weighted_average(

        self,

        value_column,

        weight_column

    ):

        weighted = (

            self.df[value_column]

            *

            self.df[weight_column]

        ).sum()

        total_weight = self.df[weight_column].sum()

        self.report.append(

            "Weighted Average"

        )

        return weighted / total_weight

    # ---------------------------------------------------
    # Ratio
    # ---------------------------------------------------

    def ratio(

        self,

        numerator,

        denominator

    ):

        data = self.df.copy()

        data["Ratio"] = (

            data[numerator]

            /

            data[denominator]

        )

        self.report.append(

            "Ratio"

        )

        return data
    
        # ---------------------------------------------------
    # Round Numeric Values
    # ---------------------------------------------------

    def round_values(

        self,

        dataframe,

        decimals=2

    ):

        self.report.append(

            f"Rounded To {decimals} Decimal Places"

        )

        return dataframe.round(decimals)

    # ---------------------------------------------------
    # Sort Index
    # ---------------------------------------------------

    def sort_index(

        self,

        dataframe,

        ascending=True

    ):

        self.report.append(

            "Sorted Index"

        )

        return dataframe.sort_index(

            ascending=ascending

        )

    # ---------------------------------------------------
    # Sort Columns
    # ---------------------------------------------------

    def sort_columns(

        self,

        dataframe,

        ascending=True

    ):

        self.report.append(

            "Sorted Columns"

        )

        return dataframe.sort_index(

            axis=1,

            ascending=ascending

        )

    # ---------------------------------------------------
    # Rename Columns
    # ---------------------------------------------------

    def rename_columns(

        self,

        dataframe,

        mapping

    ):

        self.report.append(

            "Columns Renamed"

        )

        return dataframe.rename(

            columns=mapping

        )

    # ---------------------------------------------------
    # Rename Index
    # ---------------------------------------------------

    def rename_index(

        self,

        dataframe,

        mapping

    ):

        self.report.append(

            "Index Renamed"

        )

        return dataframe.rename(

            index=mapping

        )

    # ---------------------------------------------------
    # Reset Index
    # ---------------------------------------------------

    def reset_index(

        self,

        dataframe

    ):

        self.report.append(

            "Index Reset"

        )

        return dataframe.reset_index()

    # ---------------------------------------------------
    # Fill Missing Values
    # ---------------------------------------------------

    def fill_missing(

        self,

        dataframe,

        value=0

    ):

        self.report.append(

            "Missing Values Filled"

        )

        return dataframe.fillna(value)

    # ---------------------------------------------------
    # Export CSV
    # ---------------------------------------------------

    def export_csv(

        self,

        dataframe,

        output_path

    ):

        dataframe.to_csv(

            output_path,

            index=True

        )

        self.report.append(

            f"CSV Exported -> {output_path}"

        )

    # ---------------------------------------------------
    # Export Excel
    # ---------------------------------------------------

    def export_excel(

        self,

        dataframe,

        output_path

    ):

        dataframe.to_excel(

            output_path,

            index=True

        )

        self.report.append(

            f"Excel Exported -> {output_path}"

        )

    # ---------------------------------------------------
    # Export Multiple Sheets
    # ---------------------------------------------------

    def export_multiple_sheets(

        self,

        sheets,

        output_path

    ):

        with pd.ExcelWriter(output_path) as writer:

            for name, data in sheets.items():

                data.to_excel(

                    writer,

                    sheet_name=name,

                    index=True

                )

        self.report.append(

            "Workbook Exported"

        )

    # ---------------------------------------------------
    # Excel Style Object
    # ---------------------------------------------------

    def style(

        self,

        dataframe

    ):

        self.report.append(

            "Style Generated"

        )

        return (

            dataframe.style

            .format("{:,.2f}")

            .set_caption("Analyse Pivot Table")

        )

    # ---------------------------------------------------
    # Summary Information
    # ---------------------------------------------------

    def summary(

        self,

        dataframe

    ):

        info = {

            "Rows": dataframe.shape[0],

            "Columns": dataframe.shape[1],

            "Missing Values": int(

                dataframe.isna().sum().sum()

            ),

            "Memory Usage (Bytes)": int(

                dataframe.memory_usage(

                    deep=True

                ).sum()

            )

        }

        self.report.append(

            "Summary Generated"

        )

        return info

    # ---------------------------------------------------
    # Save Report
    # ---------------------------------------------------

    def save_report(

        self,

        output_path

    ):

        with open(

            output_path,

            "w",

            encoding="utf-8"

        ) as file:

            for item in self.report:

                file.write(item + "\n")


    # ---------------------------------------------------
    # Report
    # ---------------------------------------------------

    def get_report(self):

        return self.report