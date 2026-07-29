from dataset_manager.models import Dataset


def build_workspace_data(
    dataset: Dataset
):

    return {

        "dataset_id": dataset.id,

        "dataset_name": dataset.name,

        "rows": dataset.rows,

        "columns": dataset.columns,

        "modules": {

            "profiling": True,

            "cleaning": True,

            "charts": True,

            "pivot_tables": True,

            "code_generation": True

        }

    }