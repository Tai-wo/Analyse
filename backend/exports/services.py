from dataset_manager.models import Dataset

from exports.generators.python_export import generate_python_code
from exports.generators.excel_export import generate_excel_file
from exports.generators.pdf_export import generate_pdf_report


def export_python(dataset: Dataset):

    return {
        "dataset_id": dataset.id,
        "code": generate_python_code(dataset.file_path)
    }


def export_excel(dataset: Dataset):

    file_path = generate_excel_file(dataset.file_path)

    return {
        "dataset_id": dataset.id,
        "message": "Excel file generated successfully",
        "file_path": file_path
    }


def export_pdf(dataset: Dataset):

    file_path = generate_pdf_report(dataset.file_path)

    return {
        "dataset_id": dataset.id,
        "message": "PDF report generated successfully",
        "file_path": file_path
    }