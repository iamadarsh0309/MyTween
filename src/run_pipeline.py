from pipelines.digital_data_etl import digital_data_etl

digital_data_etl.with_options(
    config_path="src/configs/digital_data_etl_maxime_labonne.yaml"
)()

