import sys
from datetime import datetime

def main():
    # Fetch current Python version and current date/time
    python_version = sys.version
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("=" * 50)
    print("      DOCKERIZED PYTHON APPLICATION REPORT      ")
    print("=" * 50)
    print(f"Current Date and Time : {current_time}")
    print(f"Running Python Version : {python_version.split()[0]}")
    print(f"Full Environment Info  : {python_version}")
    print("=" * 50)

if __name__ == "__main__":
    main()
