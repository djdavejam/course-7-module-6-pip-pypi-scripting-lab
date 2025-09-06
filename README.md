# Python Log Generator

A simple Python automation tool that generates daily log files with timestamps.

## What it does

- Creates log files with today's date (e.g., `log_20250906.txt`)
- Writes log entries to the file, one per line
- Validates input data and handles errors
- Optionally fetches data from an API

## Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the script
```bash
python lib/generate_log.py
```

### 3. Run tests
```bash
python -m pytest testing/ -v
```

## Usage Example

```python
from lib.generate_log import generate_log

# Create a log file
log_entries = ["User logged in", "Data processed", "Task completed"]
filename = generate_log(log_entries)
print(f"Log saved to: {filename}")
```

## Features

✅ **Date-based filenames** - Automatic YYYYMMDD format  
✅ **Input validation** - Ensures data is a list  
✅ **File I/O** - Writes each entry on a new line  
✅ **Error handling** - Graceful failure for invalid input  
✅ **API integration** - Optional external data fetching  
✅ **Testing** - Complete test suite with pytest

## Dependencies

- `pytest` - For running tests
- `requests` - For API calls (optional)

## Learning Goals Achieved

- ✅ Automate Python tasks using command-line scripts
- ✅ Use pip to install and manage external packages  
- ✅ Write modular Python scripts with clean entry points
- ✅ Track dependencies using requirements.txt
- ✅ Generate structured outputs using file I/O techniques