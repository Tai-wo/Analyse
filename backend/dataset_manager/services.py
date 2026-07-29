from dataset_manager.models import Dataset


def get_all_datasets(db):

    return db.query(
        Dataset
    ).all()


def get_dataset_by_id(
    db,
    dataset_id
):

    return db.query(
        Dataset
    ).filter(
        Dataset.id == dataset_id
    ).first()


# Compatibility wrapper
def get_dataset(
    db,
    dataset_id
):

    return get_dataset_by_id(
        db,
        dataset_id
    )


def delete_dataset(
    db,
    dataset_id
):

    dataset = get_dataset_by_id(
        db,
        dataset_id
    )

    if dataset:

        db.delete(dataset)

        db.commit()

    return dataset