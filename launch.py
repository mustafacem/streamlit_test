import os
import subprocess

# Path to your Streamlit app
app_path = 'main2_test.py'

def main():
    # Ensure Streamlit is installed
    try:
        subprocess.run(['streamlit', '--version'], check=True)
    except subprocess.CalledProcessError:
        print("Streamlit is not installed. Please install it using 'pip install streamlit'.")
        return

    # Run the Streamlit app
    subprocess.run(['streamlit', 'run', app_path])

if __name__ == '__main__':
    main()
