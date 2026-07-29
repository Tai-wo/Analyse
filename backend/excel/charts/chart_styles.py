import plotly.graph_objects as go


class ChartStyleManager:
    """
    Centralized styling manager for Plotly charts.
    """

    DEFAULT_WIDTH = 1000
    DEFAULT_HEIGHT = 650
    DEFAULT_TEMPLATE = "plotly_white"

    @staticmethod
    def default(
        fig: go.Figure,
        title: str = None,
        width: int = DEFAULT_WIDTH,
        height: int = DEFAULT_HEIGHT,
        template: str = DEFAULT_TEMPLATE
    ) -> go.Figure:
        """
        Apply the default Analyse chart style.
        """

        fig.update_layout(
            template=template,
            width=width,
            height=height,
            title=title,
            title_x=0.5,
            font=dict(
                family="Arial",
                size=14
            ),
            paper_bgcolor="white",
            plot_bgcolor="white",
            margin=dict(
                l=60,
                r=40,
                t=80,
                b=60
            ),
            hovermode="closest",
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            )
        )

        fig.update_xaxes(
            showgrid=True,
            gridcolor="#ECECEC",
            zeroline=False
        )

        fig.update_yaxes(
            showgrid=True,
            gridcolor="#ECECEC",
            zeroline=False
        )

        return fig

    @staticmethod
    def dashboard(
        fig: go.Figure
    ) -> go.Figure:
        """
        Style for dashboard widgets.
        """

        fig.update_layout(
            height=450,
            margin=dict(
                l=40,
                r=30,
                t=50,
                b=40
            ),
            legend=dict(
                orientation="h"
            )
        )

        return fig

    @staticmethod
    def dark(
        fig: go.Figure
    ) -> go.Figure:
        """
        Dark mode style.
        """

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#121212",
            plot_bgcolor="#121212",
            font=dict(
                color="white"
            )
        )

        return fig

    @staticmethod
    def presentation(
        fig: go.Figure
    ) -> go.Figure:
        """
        Style for presentations.
        """

        fig.update_layout(
            font=dict(
                family="Arial",
                size=18
            ),
            title_font=dict(
                size=26
            ),
            legend=dict(
                font=dict(size=16)
            )
        )

        return fig

    @staticmethod
    def print_ready(
        fig: go.Figure
    ) -> go.Figure:
        """
        High-quality print style.
        """

        fig.update_layout(
            width=1400,
            height=900,
            font=dict(
                family="Times New Roman",
                size=18
            )
        )

        return fig