from pydantic_settings import BaseSettings, SettingsConfigDict

class ResultSettings(BaseSettings):
    output_name: str

    model_config = SettingsConfigDict(
        json_file="config.json", json_file_encoding="utf-8"
    )

settings = ResultSettings(output_name="some_value")
