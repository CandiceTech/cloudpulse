from app.aws.mock_data import MOCK_S3_BUCKETS
from app.config import use_mock_data


def analyze_s3_buckets():
    if use_mock_data():
        return MOCK_S3_BUCKETS

    return {
        "error": "S3 live analysis is not implemented yet",
        "hint": "Set CLOUDPULSE_USE_MOCKS=true for local demo mode."
    }
