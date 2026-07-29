import os

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import plotly.express as px

import plotly.graph_objects as go

from .chart_styles import ChartStyleManager
from .chart_utils import ChartUtils
from .chart_export import ChartExporter


class ExcelChartEngine:

    def __init__(
        self,
        dataframe,
        export_format="html"
    ):

        self.df = dataframe

        self.output_folder = "generated_charts"

        self.export_format = export_format.lower()

        self.report = []

        os.makedirs(
            self.output_folder,
            exist_ok=True
        )

    # ==========================================================
    # INTERNAL HELPERS
    # ==========================================================
    def _validate_dataframe(self):
        """
        Validate the dataframe.
        """
        ChartUtils.validate_dataframe(self.df)


    def _validate_columns(self, columns):
        """
        Validate that columns exist.
        """
        ChartUtils.validate_columns(
            self.df,
            columns
        )


    def _validate_numeric(self, column):
        """
        Validate numeric columns.
        """
        ChartUtils.validate_numeric(
            self.df,
            column
        )


    def _generate_filepath(self, chart_name):
        """
        Generate output filepath.
        """
        return ChartUtils.generate_filepath(
            self.output_folder,
            chart_name
        )


        def _save_plotly_chart(
        self,
        fig,
        chart_name
    ):
         """
         Save Plotly chart using the ChartExporter.  
         """

        return ChartExporter.export(
            fig=fig,
            output_folder=self.output_folder,
            chart_name=chart_name,
            report=self.report,
            export_format=self.export_format
        )


    def _save_matplotlib_chart(
        self,
        chart_name
    ):
        """
        Save Matplotlib chart.
        """

        return ChartUtils.save_matplotlib_chart(
            self.output_folder,
            chart_name,
            self.report
        )
           # ==========================================================
    # BAR CHART
    # ==========================================================

    def create_bar_chart(
        self,
        x,
        y,
        title="Bar Chart",
        color=None,
        orientation="v",
        sort=False,
        ascending=False,
        template="plotly_white",
        width=1000,
        height=600
    ):
        """
        Create a vertical bar chart.
        """

        self._validate_dataframe()

        required = [x, y]

        if color:
            required.append(color)

        self._validate_columns(required)
        self._validate_numeric(y)

        data = self.df.copy()

        if sort:
            data = data.sort_values(
                by=y,
                ascending=ascending
            )

        fig = px.bar(
            data_frame=data,
            x=x,
            y=y,
            color=color,
            orientation=orientation
        )

        # Apply Analyse default styling
        fig = ChartStyleManager.default(
            fig=fig,
            title=title,
            width=width,
            height=height,
            template=template
        )

        # Chart-specific layout
        fig.update_layout(
            xaxis_title=x,
            yaxis_title=y,
            legend_title=color if color else ""
        )

        fig.update_traces(
            hovertemplate=(
                f"{x}: %{{x}}<br>"
                f"{y}: %{{y}}"
                "<extra></extra>"
            )
        )

        return self._save_plotly_chart(
            fig,
            title
        )
           # ==========================================================
    # HORIZONTAL BAR CHART
    # ==========================================================

    def create_horizontal_bar_chart(
        self,
        x,
        y,
        title="Horizontal Bar Chart",
        color=None,
        sort=False,
        ascending=True,
        template="plotly_white",
        width=1000,
        height=600
    ):
        """
        Create a horizontal bar chart.
        """

        self._validate_dataframe()

        required = [x, y]

        if color:
            required.append(color)

        self._validate_columns(required)
        self._validate_numeric(y)

        data = self.df.copy()

        if sort:
            data = data.sort_values(
                by=y,
                ascending=ascending
            )

        fig = px.bar(
            data_frame=data,
            x=y,
            y=x,
            color=color,
            orientation="h"
        )

        # Apply Analyse default styling
        fig = ChartStyleManager.default(
            fig=fig,
            title=title,
            width=width,
            height=height,
            template=template
        )

        # Chart-specific layout
        fig.update_layout(
            xaxis_title=y,
            yaxis_title=x,
            legend_title=color if color else ""
        )

        fig.update_traces(
            hovertemplate=(
                f"{x}: %{{y}}<br>"
                f"{y}: %{{x}}"
                "<extra></extra>"
            )
        )

        return self._save_plotly_chart(
            fig,
            title
        )
            # ==========================================================
    # LINE CHART
    # ==========================================================

    def create_line_chart(
        self,
        x,
        y,
        title="Line Chart",
        markers=True,
        line_width=3,
        template="plotly_white",
        width=1000,
        height=600
    ):
        """
        Create a line chart.
        """

        self._validate_dataframe()

        if isinstance(y, str):
            y = [y]

        required = [x] + y

        self._validate_columns(required)

        for column in y:
            self._validate_numeric(column)

        data = self.df.copy()

        fig = go.Figure()

        for column in y:

            fig.add_trace(
                go.Scatter(
                    x=data[x],
                    y=data[column],
                    mode="lines+markers" if markers else "lines",
                    name=column,
                    line=dict(width=line_width)
                )
            )

        # Apply Analyse default styling
        fig = ChartStyleManager.default(
            fig=fig,
            title=title,
            width=width,
            height=height,
            template=template
        )

        # Line chart specific settings
        fig.update_layout(
            xaxis_title=x,
            yaxis_title="Value",
            legend_title="Series",
            hovermode="x unified"
        )

        return self._save_plotly_chart(
            fig,
            title
        )
    
        # ==========================================================
    # AREA CHART
    # ==========================================================

    def create_area_chart(
        self,
        x,
        y,
        title="Area Chart",
        stacked=False,
        markers=False,
        opacity=0.6,
        template="plotly_white",
        width=1000,
        height=600
    ):
        """
        Create an area chart.
        """

        self._validate_dataframe()

        if isinstance(y, str):
            y = [y]

        required = [x] + y

        self._validate_columns(required)

        for column in y:
            self._validate_numeric(column)

        data = self.df.copy()

        fig = go.Figure()

        for index, column in enumerate(y):

            trace = go.Scatter(
                x=data[x],
                y=data[column],
                name=column,
                mode="lines+markers" if markers else "lines",
                fill="tozeroy" if not stacked else "tonexty",
                opacity=opacity
            )

            if stacked:
                trace.stackgroup = "stack"

            fig.add_trace(trace)

        # Apply Analyse default styling
        fig = ChartStyleManager.default(
            fig=fig,
            title=title,
            width=width,
            height=height,
            template=template
        )

        # Area chart specific layout
        fig.update_layout(
            xaxis_title=x,
            yaxis_title="Value",
            legend_title="Series",
            hovermode="x unified"
        )

        return self._save_plotly_chart(
            fig,
            title
        )
            # ==========================================================
    # PIE CHART
    # ==========================================================

    def create_pie_chart(
        self,
        names,
        values,
        title="Pie Chart",
        aggregation="sum",
        hole=0.0,
        sort=True,
        top_n=None,
        template="plotly_white",
        width=900,
        height=650
    ):
        """
        Create a pie chart.
        """

        self._validate_dataframe()

        self._validate_columns([names, values])
        self._validate_numeric(values)

        valid_aggs = {
            "sum",
            "mean",
            "count",
            "min",
            "max",
            "median"
        }

        if aggregation not in valid_aggs:
            raise ValueError(
                f"Aggregation must be one of {valid_aggs}"
            )

        data = (
            self.df
            .groupby(names)[values]
            .agg(aggregation)
            .reset_index()
        )

        if sort:
            data = data.sort_values(
                by=values,
                ascending=False
            )

        if top_n is not None and top_n > 0:

            if len(data) > top_n:

                top = data.iloc[:top_n]
                others = data.iloc[top_n:]

                others_value = others[values].sum()

                others_row = pd.DataFrame({
                    names: ["Others"],
                    values: [others_value]
                })

                data = pd.concat(
                    [top, others_row],
                    ignore_index=True
                )

        fig = px.pie(
            data_frame=data,
            names=names,
            values=values,
            hole=hole
        )

        # Apply Analyse default styling
        fig = ChartStyleManager.default(
            fig=fig,
            title=title,
            width=width,
            height=height,
            template=template
        )

        # Pie chart specific layout
        fig.update_layout(
            legend_title=names
        )

        fig.update_traces(
            textposition="inside",
            textinfo="percent+label",
            hovertemplate=(
                "<b>%{label}</b><br>"
                "Value: %{value}<br>"
                "Percentage: %{percent}"
                "<extra></extra>"
            )
        )

        return self._save_plotly_chart(
            fig,
            title
        )
        # ==========================================================
    # DOUGHNUT CHART
    # ==========================================================

    def create_doughnut_chart(
        self,
        names,
        values,
        title="Doughnut Chart",
        aggregation="sum",
        hole=0.5,
        sort=True,
        top_n=None,
        template="plotly_white",
        width=900,
        height=650
    ):
        """
        Create a doughnut chart.

        Parameters
        ----------
        names : str
            Categorical column.

        values : str
            Numeric column.

        title : str
            Chart title.

        aggregation : str
            Aggregation function:
            sum, mean, count, min, max, median.

        hole : float
            Size of the doughnut hole.
            Must be between 0 and 1.

        sort : bool
            Sort slices by value.

        top_n : int | None
            Display only the largest N categories.
            Remaining categories are grouped into "Others".

        template : str
            Plotly template.

        width : int
            Chart width.

        height : int
            Chart height.

        Returns
        -------
        str
            Path to the saved chart.
        """

        if not 0 <= hole < 1:
            raise ValueError(
                "hole must be between 0 and 1."
            )

        return self.create_pie_chart(
            names=names,
            values=values,
            title=title,
            aggregation=aggregation,
            hole=hole,
            sort=sort,
            top_n=top_n,
            template=template,
            width=width,
            height=height
        )
            # ==========================================================
    # SCATTER CHART
    # ==========================================================

    def create_scatter_chart(
        self,
        x,
        y,
        title="Scatter Chart",
        color=None,
        size=None,
        hover_data=None,
        opacity=0.8,
        trendline=False,
        template="plotly_white",
        width=1000,
        height=650
    ):
        """
        Create a scatter chart.
        """

        self._validate_dataframe()

        required = [x, y]

        if color:
            required.append(color)

        if size:
            required.append(size)

        if hover_data:
            required.extend(hover_data)

        self._validate_columns(required)

        self._validate_numeric(x)
        self._validate_numeric(y)

        if size:
            self._validate_numeric(size)

        fig = px.scatter(
            data_frame=self.df,
            x=x,
            y=y,
            color=color,
            size=size,
            hover_data=hover_data,
            opacity=opacity,
            trendline="ols" if trendline else None
        )

        # Apply Analyse default styling
        fig = ChartStyleManager.default(
            fig=fig,
            title=title,
            width=width,
            height=height,
            template=template
        )

        # Scatter-specific layout
        fig.update_layout(
            xaxis_title=x,
            yaxis_title=y,
            legend_title=color if color else "",
            hovermode="closest"
        )

        fig.update_traces(
            marker=dict(
                line=dict(
                    width=0.5,
                    color="white"
                )
            )
        )

        return self._save_plotly_chart(
            fig,
            title
        )
           # ==========================================================
    # HISTOGRAM
    # ==========================================================

    def create_histogram(
        self,
        column,
        title="Histogram",
        color=None,
        bins=30,
        histnorm=None,
        cumulative=False,
        marginal=None,
        opacity=0.8,
        template="plotly_white",
        width=1000,
        height=650
    ):
        """
        Create a histogram.
        """

        self._validate_dataframe()

        required = [column]

        if color:
            required.append(color)

        self._validate_columns(required)
        self._validate_numeric(column)

        fig = px.histogram(
            data_frame=self.df,
            x=column,
            color=color,
            nbins=bins,
            histnorm=histnorm,
            marginal=marginal,
            opacity=opacity
        )

        if cumulative:
            fig.update_traces(
                cumulative_enabled=True
            )

        # Apply Analyse default styling
        fig = ChartStyleManager.default(
            fig=fig,
            title=title,
            width=width,
            height=height,
            template=template
        )

        # Histogram-specific layout
        fig.update_layout(
            xaxis_title=column,
            yaxis_title="Frequency",
            bargap=0.05,
            legend_title=color if color else ""
        )

        return self._save_plotly_chart(
            fig,
            title
        )
           # ==========================================================
    # BOX PLOT
    # ==========================================================

    def create_box_plot(
        self,
        y,
        x=None,
        color=None,
        title="Box Plot",
        points="outliers",
        notched=False,
        orientation="v",
        template="plotly_white",
        width=1000,
        height=650
    ):
        """
        Create a box plot.
        """

        self._validate_dataframe()

        required = [y]

        if x:
            required.append(x)

        if color:
            required.append(color)

        self._validate_columns(required)
        self._validate_numeric(y)

        if orientation not in ["v", "h"]:
            raise ValueError(
                "orientation must be 'v' or 'h'."
            )

        if orientation == "v":

            fig = px.box(
                data_frame=self.df,
                x=x,
                y=y,
                color=color,
                points=points,
                notched=notched
            )

        else:

            fig = px.box(
                data_frame=self.df,
                x=y,
                y=x,
                color=color,
                points=points,
                notched=notched,
                orientation="h"
            )

        # Apply Analyse default styling
        fig = ChartStyleManager.default(
            fig=fig,
            title=title,
            width=width,
            height=height,
            template=template
        )

        # Box plot specific layout
        fig.update_layout(
            legend_title=color if color else ""
        )

        return self._save_plotly_chart(
            fig,
            title
        )