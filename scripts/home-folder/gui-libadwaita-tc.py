#!/bin/python3

import os
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

class ThemeChangerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Libadwaita Theme Changer")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Constants
        self.home_dir = os.getenv('HOME')
        self.config_dir = os.path.join(self.home_dir, ".config")
        self.theme_dirs = {
            "Local Share Themes": os.path.join(self.home_dir, ".local/share/themes"),
            "Dot Themes": os.path.join(self.home_dir, ".themes"),
            "System Themes": "/usr/share/themes",
        }
        self.theme_items = ["gtk-4.0/gtk.css", "gtk-4.0/gtk-dark.css", "gtk-4.0/assets", "assets"]

        # Selected values
        self.selected_theme_dir = tk.StringVar(value="Please select a directory")  # Placeholder for no default
        self.themes = []
        self.selected_theme = tk.StringVar()

        # Styles
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), padding=10, relief="flat", background="#4CAF50", foreground="white")
        self.style.configure('TLabel', font=('Helvetica', 12), background="#f5f5f5")
        self.style.map('TButton', background=[('active', '#45a049')], relief=[('active', 'raised')])
        self.style.configure('Red.TButton', font=('Helvetica', 12), padding=10, relief="flat", background="#F44336", foreground="white")
        
        self.style.configure('TOptionMenu', font=('Helvetica', 12), relief="flat", background="#f0f0f0", foreground="black")

        # Spawn GUI
        self.create_widgets()

    def create_widgets(self):
        # Background
        frame = tk.Frame(self.root, bg="#f5f5f5", padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        # Title label
        title_label = ttk.Label(frame, text="Libadwaita Theme Changer", font=("Helvetica", 16, "bold"), anchor="center")
        title_label.pack(pady=20)

        # Theme directory selection
        ttk.Label(frame, text="Select Theme Directory:").pack(pady=10)

        # OptionMenu for theme directory selection
        dir_menu = ttk.OptionMenu(frame, self.selected_theme_dir, "Please select a directory", *self.theme_dirs.keys(), command=self.update_themes)
        dir_menu.pack(pady=5, fill="x")

        # Theme selection
        ttk.Label(frame, text="Select Theme:").pack(pady=10)
        self.theme_menu = ttk.OptionMenu(frame, self.selected_theme, "No Themes Available")
        self.theme_menu.pack(pady=5, fill="x")
        
        self.style.map('Red.TButton', background=[('active', '#e53935')])

        # Buttons
        ttk.Button(frame, text="Apply Theme", command=self.apply_theme).pack(pady=15, fill="x")
        ttk.Button(frame, text="Reset Theme", command=self.reset_theme, style='Red.TButton').pack(pady=5, fill="x")

    def update_themes(self, _):
        """Update the theme list when a directory is selected."""
        selected_dir = self.selected_theme_dir.get()

        # Ensure a valid directory is selected
        if selected_dir == "Please select a directory":
            messagebox.showwarning("Warning", "Please select a theme directory first!")
            return

        theme_dir = self.theme_dirs[selected_dir]
        if os.path.exists(theme_dir):
            self.themes = os.listdir(theme_dir)
            if self.themes:
                self.selected_theme.set(self.themes[0])  # Set default theme if available
                menu = self.theme_menu["menu"]
                menu.delete(0, "end")
                for theme in self.themes:
                    menu.add_command(label=theme, command=lambda value=theme: self.selected_theme.set(value))
            else:
                self.selected_theme.set("No Themes Available")
        else:
            messagebox.showerror("Error", f"Directory not found: {theme_dir}")
            
    def remove_gtk_assets(self):
        """Remove gtk assets and gtk.css files."""
        try:
            # Define the paths to the assets directory and gtk.css file
            assets_path = os.path.join(self.home_dir, '.config/gtk-4.0/assets/')
            gtk_css_path = os.path.join(self.home_dir, '.config/gtk-4.0/gtk.css')

            # Remove the assets directory
            subprocess.run(['rm', '-rf', assets_path], check=True)

            # Remove the gtk.css file
            subprocess.run(['rm', '-rf', gtk_css_path], check=True)

        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e}")
            messagebox.showerror("Error", f"Failed to prep by removing assets: {e}")

    def remove_current_theme(self):
        """Remove current theme links in the config directory."""
        for item in self.theme_items:
            path = os.path.join(self.config_dir, item)
            if os.path.islink(path):
                os.remove(path)

    def set_new_theme(self, theme_path):
        """Set the new theme by creating symbolic links."""
        for item in self.theme_items:
            os.symlink(os.path.join(theme_path, item), os.path.join(self.config_dir, item))

    def apply_theme(self):
        """Apply the selected theme."""
        if self.selected_theme.get() in ["", "No Themes Available"]:
            messagebox.showwarning("Warning", "No theme selected!")
            return

        theme_dir = self.theme_dirs[self.selected_theme_dir.get()]
        theme_path = os.path.join(theme_dir, self.selected_theme.get())
        if not os.path.exists(theme_path):
            messagebox.showerror("Error", f"Theme not found: {theme_path}")
            return

        # Apply theme
        try:
            self.remove_gtk_assets()
            self.remove_current_theme()
            self.set_new_theme(theme_path)
            os.system(f'gsettings set org.gnome.desktop.interface gtk-theme "{self.selected_theme.get()}"')
            os.system(f'gsettings set org.gnome.desktop.wm.preferences theme "{self.selected_theme.get()}"')
            messagebox.showinfo("Success", f"Theme '{self.selected_theme.get()}' applied successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply theme: {e}")

    def reset_theme(self):
        """Reset to the default theme."""
        try:
            self.remove_current_theme()
            os.system('gsettings reset org.gnome.desktop.interface gtk-theme')
            os.system('gsettings reset org.gnome.desktop.wm.preferences theme')
            messagebox.showinfo("Success", "Theme reset to default successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to reset theme: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ThemeChangerApp(root)
    root.mainloop()

