from datetime import datetime
import os

def generate_log(data):
    """
    Generate a log file with the provided data.
    
    Args:
        data: A list of log entries to write to the file
        
    Returns:
        str: The filename of the created log file
        
    Raises:
        ValueError: If data is not a list
    """
    # STEP 1: Validate input
    # Hint: Check if data is a list
    if not isinstance(data, list):
        raise ValueError("Input data must be a list")
    
    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
    
    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")
    
    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")
    
    return filename

def fetch_data():
    """
    Fetch data from an external API.
    
    Returns:
        dict: JSON response from the API, or empty dict if request fails
    """
    try:
        import requests
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            return response.json()
        return {}
    except ImportError:
        print("Note: 'requests' package not installed. Install with: pip install requests")
        return {}
    except Exception as e:
        print(f"Error fetching data: {e}")
        return {}

if __name__ == "__main__":
    # Sample log data
    log_data = ["User logged in", "User updated profile", "Report exported"]
    
    # Try to fetch additional data from API
    api_data = fetch_data()
    if api_data:
        log_data.append(f"API Data fetched: {api_data.get('title', 'No title found')}")
        print("Fetched Post Title:", api_data.get("title", "No title found"))
    
    # Generate the log file
    generated_filename = generate_log(log_data)
    
    # Confirm the file was created
    if os.path.exists(generated_filename):
        print(f"✅ Successfully created log file: {generated_filename}")
        
        # Show file contents for verification
        print("\n📄 File contents:")
        with open(generated_filename, "r") as file:
            for line_num, line in enumerate(file, 1):
                print(f"  {line_num}. {line.strip()}")
    else:
        print(f"❌ Failed to create log file: {generated_filename}")