import os
    2 from ucsc_student_portal_official_api import PortalClient
    3
    4 def check_hostel_room():
    5     # It's best practice to use environment variables for credentials
    6     username = os.getenv("UCSC_USERNAME")
    7     password = os.getenv("UCSC_PASSWORD")
    8
    9     if not username or not password:
   10         print("Error: Please set UCSC_USERNAME and UCSC_PASSWORD environment variables.")
   11         return
   12
   13     try:
   14         # Initialize the portal client
   15         client = PortalClient()
   16
   17         # Log in to the student portal
   18         print("Logging in...")
   19         client.login(username, password)
   20
   21         # Fetch profile or specific hostel information
   22         # Note: Method names like 'get_hostel_info' are common guesses
   23         hostel_info = client.get_hostel_info()
   24
   25         if hostel_info:
   26             print("\n--- Hostel Information ---")
   27             print(f"Hostel Name: {hostel_info.get('name', 'N/A')}")
   28             print(f"Room Number: {hostel_info.get('room_number', 'Not assigned')}")
   29             print(f"Status: {hostel_info.get('status', 'N/A')}")
   30         else:
   31             print("No hostel information found for this account.")
   32
   33     except Exception as e:
   34         print(f"An error occurred: {e}")
   35
   36 if __name__ == "__main__":