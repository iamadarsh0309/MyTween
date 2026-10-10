from zenml import pipeline

from steps.dataset import generate_instruction_dataset


@pipeline
def dataset_pipeline():
    generate_instruction_dataset()