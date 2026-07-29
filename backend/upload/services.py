import os

from upload.utils import analyze_file

from dataset_manager.models import Dataset
from workspace.models import Workspace


UPLOAD_DIR = "uploads"


def save_file(file):

    os.makedirs(
        UPLOAD_DIR,
        exist_ok=True
    )

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as f:

        f.write(
            file.file.read()
        )

    return file_path


def create_dataset_record(
    db,
    filename,
    file_path
):

    rows, columns = analyze_file(
        file_path
    )

    dataset = Dataset(

        name=filename,

        file_path=file_path,

        rows=rows,

        columns=columns

    )

    db.add(dataset)

    db.commit()

    db.refresh(dataset)

    workspace = Workspace(

        dataset_id=dataset.id

    )

    db.add(workspace)

    db.commit()

    db.refresh(workspace)

    return dataset