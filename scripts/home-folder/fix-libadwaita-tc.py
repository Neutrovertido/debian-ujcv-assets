#!/bin/python3
import subprocess

def remove_gtk_assets():
    try:
        # Remove the assets directory
        subprocess.run(['rm', '-rf', '.config/gtk-4.0/assets/'], check=True)
        print("Removed .config/gtk-4.0/assets/ successfully.")
        
        # Remove the gtk.css file
        subprocess.run(['rm', '-rf', '.config/gtk-4.0/gtk.css'], check=True)
        print("Removed .config/gtk-4.0/gtk.css successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    remove_gtk_assets()
