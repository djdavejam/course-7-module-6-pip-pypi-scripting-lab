import os
import pytest
from datetime import datetime
from lib.generate_log import generate_log

@pytest.fixture
def log_data():
    return ["Entry one", "Entry two", "Entry three"]

@pytest.fixture
def generated_file(log_data):
    """Fixture that creates a log file and cleans it up after the test."""
    filename = generate_log(log_data)
    yield filename
    # Cleanup: remove the file after the test
    if os.path.exists(filename):
        os.remove(filename)

def test_log_file_created(generated_file):
    """Test that the log file is created with today's date in the filename."""
    assert os.path.exists(generated_file), f"{generated_file} not found."

def test_log_file_name_format(generated_file):
    """Test that the filename follows the expected naming convention."""
    today = datetime.now().strftime("%Y%m%d")
    expected_filename = f"log_{today}.txt"
    assert generated_file == expected_filename, "Filename does not match expected format."

def test_log_file_content_matches_input(generated_file, log_data):
    """Test that the content written to the log file matches the input list."""
    with open(generated_file, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    assert lines == log_data, "Log file contents do not match input data."

def test_generate_log_raises_error_on_invalid_input():
    """Test that the function raises a ValueError when input is not a list."""
    with pytest.raises(ValueError):
        generate_log("This should be a list")

def test_empty_log_list_creates_empty_file():
    """Test that passing an empty list still creates an empty log file."""
    filename = generate_log([])
    try:
        with open(filename, "r") as file:
            content = file.read()
        assert content == "", "Empty list should create empty file."
    finally:
        # Cleanup
        if os.path.exists(filename):
            os.remove(filename)

def test_log_file_contains_newlines():
    """Test that each log entry is written on a separate line."""
    test_data = ["Line 1", "Line 2", "Line 3"]
    filename = generate_log(test_data)
    try:
        with open(filename, "r") as file:
            content = file.read()
        
        # Check that the file ends with newlines for each entry
        expected_content = "Line 1\nLine 2\nLine 3\n"
        assert content == expected_content, "Log entries should be separated by newlines."
    finally:
        # Cleanup
        if os.path.exists(filename):
            os.remove(filename)

def test_generate_log_returns_filename():
    """Test that the function returns the generated filename."""
    test_data = ["Test entry"]
    filename = generate_log(test_data)
    try:
        today = datetime.now().strftime("%Y%m%d")
        expected_filename = f"log_{today}.txt"
        assert filename == expected_filename, "Function should return the generated filename."
    finally:
        # Cleanup
        if os.path.exists(filename):
            os.remove(filename)

def test_multiple_calls_overwrite_same_file():
    """Test that multiple calls on the same day overwrite the same file."""
    first_data = ["First call"]
    second_data = ["Second call", "Additional entry"]
    
    # First call
    filename1 = generate_log(first_data)
    
    # Second call (should overwrite)
    filename2 = generate_log(second_data)
    
    try:
        # Should be the same filename
        assert filename1 == filename2, "Both calls should generate the same filename."
        
        # File should contain only the second data
        with open(filename2, "r") as file:
            lines = [line.strip() for line in file.readlines()]
        assert lines == second_data, "Second call should overwrite the first."
    finally:
        # Cleanup
        if os.path.exists(filename1):
            os.remove(filename1)