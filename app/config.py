import os


def use_mock_data() -> bool:
    return os.getenv("CLOUDPULSE_USE_MOCKS", "true").lower() in {
        "1",
        "true",
        "yes",
        "on"
    }
