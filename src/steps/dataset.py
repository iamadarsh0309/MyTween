from typing import Annotated, Any

from zenml import ArtifactConfig, get_step_context, step


@step
def generate_instruction_dataset() -> Annotated[
    dict,
    ArtifactConfig(
        name="instruct_datasets",
        tags=["dataset", "instruct", "cleaned"],
    ),
]:
    # Temporary dataset
    datasets = {
        "train": {
            "articles": 100,
            "posts": 50,
            "repositories": 25,
        },
        "test": {
            "articles": 20,
            "posts": 10,
            "repositories": 5,
        },
    }

    step_context = get_step_context()

    step_context.add_output_metadata(
        output_name="instruct_datasets",
        metadata=_get_metadata_instruct_dataset(datasets),
    )

    return datasets


def _get_metadata_instruct_dataset(
    datasets: dict,
) -> dict[str, Any]:
    train = datasets["train"]
    test = datasets["test"]

    return {
        "data_categories": list(train.keys()),
        "train_num_samples_per_category": train,
        "test_num_samples_per_category": test,
    }