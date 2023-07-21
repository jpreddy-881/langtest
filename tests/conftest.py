import pytest
import json


@pytest.fixture(scope="session", autouse=True)
def create_summarization_data():
    """Creates fake data files for summarization task"""
    samples = {
        "summarization_1": [
            {"text": "Hello my name is John", "summary": "John"},
            {"text": "Hello my name is Jules", "summary": "Jules"},
        ]
    }
    for key, value in samples.items():
        with open(f"/tmp/{key}.jsonl", "w") as writer:
            for entry in value:
                json.dump(entry, writer)
                writer.write("\n")