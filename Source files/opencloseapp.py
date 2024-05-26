import os
import webbrowser

def open_application(query):
    # Get the application name from the voice command
    app_name = query.split()[-1]
    
    # Try to open the application
    try:
        os.startfile(f"start {app_name}.exe")
        # print(f"{app_name} opened successfully!")
    except Exception as e:
        print(f"{app_name} not found. Searching online...")
        webbrowser.open_new_tab(f"(https://www.google.com/{app_name})")

def close_application(query):
    # Get the application name from the voice command
    app_name = query.split()[-1]
    
    # Try to close the application
    try:
        os.system(f"taskkill /im {app_name}.exe")
        print(f"{app_name} closed successfully!")
    except Exception as e:
        print(f"Error closing {app_name}: {str(e)}")


