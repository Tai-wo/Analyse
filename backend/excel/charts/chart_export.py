import os

import plotly.graph_objects as go

from .chart_utils import ChartUtils


class ChartExporter:
    """
    Handles exporting Plotly charts into multiple formats.
    """

    SUPPORTED_FORMATS = {
        "html",
        "png",
        "jpg",
        "jpeg",
        "svg",
        "pdf",
        "json"
    }

    @staticmethod
    def export(
        fig: go.Figure,
        output_folder: str,
        chart_name: str,
        report: list,
        export_format: str = "html"
    ):
        """
        Export a Plotly chart.

        Parameters
        ----------
        fig : go.Figure

        output_folder : str

        chart_name : str

        report : list

        export_format : str

        Returns
        -------
        str
            Output filepath.
        """

        export_format = export_format.lower()

        if export_format not in ChartExporter.SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported export format: {export_format}"
            )

        ChartUtils.create_output_directory(
            output_folder
        )

        filepath = ChartUtils.generate_filepath(
            output_folder,
            chart_name,
            export_format
        )

        if export_format == "html":

            fig.write_html(filepath)

        elif export_format == "json":

            fig.write_json(filepath)

        else:
            # PNG, PDF, SVG, JPG, JPEG
            # Requires:
            # pip install kaleido
            fig.write_image(filepath)

        report.append(
            {
                "chart": chart_name,
                "format": export_format,
                "output": filepath
            }
        )

        return filepath