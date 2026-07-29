import os
import re

import pandas as pd
import matplotlib.pyplot as plt


class ChartUtils:
    """
    Utility methods shared across the Excel Chart Engine.
    """

    @staticmethod
    def validate_dataframe(df):
        """
        Ensure dataframe exists and is not empty.
        """

        if df is None:
            raise ValueError(
                "No dataframe supplied."
            )

        if df.empty:
            raise ValueError(
                "The dataframe is empty."
            )

    @staticmethod
    def validate_columns(df, columns):
        """
        Validate that all requested columns exist.
        """

        if isinstance(columns, str):
            columns = [columns]

        missing = [
            column
            for column in columns
            if column not in df.columns
        ]

        if missing:
            raise ValueError(
                f"Column(s) not found: {', '.join(missing)}"
            )

    @staticmethod
    def validate_numeric(df, column):
        """
        Ensure a column contains numeric values.
        """

        ChartUtils.validate_columns(df, column)

        if not pd.api.types.is_numeric_dtype(df[column]):
            raise TypeError(
                f"'{column}' must be numeric."
            )

    @staticmethod
    def create_output_directory(output_folder):
        """
        Create the output directory if it does not exist.
        """

        os.makedirs(
            output_folder,
            exist_ok=True
        )

    @staticmethod
    def sanitize_filename(name):
        """
        Convert a chart title into a safe filename.
        """

        filename = name.lower().strip()

        filename = filename.replace(" ", "_")

        filename = re.sub(
            r"[^a-zA-Z0-9_-]",
            "",
            filename
        )

        return filename

    @staticmethod
    def generate_filepath(
        output_folder,
        chart_name,
        extension="html"
    ):
        """
        Generate a full output filepath.
        """

        filename = (
            ChartUtils.sanitize_filename(chart_name)
            + f".{extension}"
        )

        return os.path.join(
            output_folder,
            filename
        )

    @staticmethod
    def save_plotly_chart(
        fig,
        output_folder,
        chart_name,
        report
    ):
        """
        Save a Plotly chart.
        """

        ChartUtils.create_output_directory(
            output_folder
        )

        filepath = ChartUtils.generate_filepath(
            output_folder,
            chart_name,
            "html"
        )

        fig.write_html(filepath)

        report.append(
            {
                "chart": chart_name,
                "output": filepath
            }
        )

        return filepath

    @staticmethod
    def save_matplotlib_chart(
        output_folder,
        chart_name,
        report
    ):
        """
        Save a Matplotlib chart.
        """

        ChartUtils.create_output_directory(
            output_folder
        )

        filepath = ChartUtils.generate_filepath(
            output_folder,
            chart_name,
            "png"
        )

        plt.tight_layout()

        plt.savefig(
            filepath,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        report.append(
            {
                "chart": chart_name,
                "output": filepath
            }
        )

        return filepath