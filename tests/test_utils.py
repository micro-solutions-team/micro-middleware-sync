import pytest
from src.utils import format_corporate_name, validate_record

def test_format_corporate_name():
    # Test case 1: Standard legacy all-caps
    assert format_corporate_name("PAPADOPOULOS IOANNIS") == "Papadopoulos Ioannis"
    
    # Test case 2: Extra spaces (common in DBs)
    assert format_corporate_name("  SMITH MARIA  ") == "Smith Maria"
    
    # Test case 3: Empty string
    assert format_corporate_name("") == "Unknown"

def test_validate_record_success():
    record = {"id": 1, "name": "Test"}
    is_valid, message = validate_record(record)
    assert is_valid is True

def test_validate_record_failure():
    record = {"id": None, "name": "Broken"}
    is_valid, message = validate_record(record)
    assert is_valid is False
    assert message == "Missing ID"