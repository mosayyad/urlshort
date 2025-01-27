# Code written by SayyadN
# Date: 2025-1-26
# Purpose: Download YouTube videos using Python
# Version: 1.1
# Code Starts here

# Importing the required libraries
from pytube import YouTube
import os
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *

# Function to check if the provided path exists
def check_path():
    vid_path = path_entry.get()
    if os.path.exists(vid_path):
        messagebox.showinfo("Success", "Your Path Exists!")
    elif vid_path == "":
        messagebox.showerror("Error", "Please enter the path where you want to save the video.")
    else:
        messagebox.showerror("Error", "Your Path Does Not Exist!")
        os.mkdir(vid_path)
        messagebox.showwarning("Creating Your Path", "Path created successfully.")

# Function to update the progress bar
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    progress_bar['value'] = percentage
    root.update_idletasks()

# Function to download the video
def download_video():
    video_url = url_entry.get()
    vid_save_path = path_entry.get()

    if not video_url or not vid_save_path:
        messagebox.showerror("Error", "Please enter both the URL and the save path.")
        return

    try:
        # Creating a YouTube object
        yt = YouTube(video_url, on_progress_callback=on_progress)

        # Ask the user for resolution choice
        resolution_choice = resolution_var.get().upper()

        if resolution_choice == 'H':
            video = yt.streams.get_highest_resolution()
        elif resolution_choice == 'L':
            video = yt.streams.get_lowest_resolution()
        else:
            messagebox.showerror("Error", "Invalid option selected. Please choose 'H' or 'L'.")
            return

        # Start downloading
        messagebox.showinfo("Downloading Video", f"Downloading {yt.title}...")
        video.download(vid_save_path)
        messagebox.showinfo("Success", f"Video '{yt.title}' downloaded successfully at {vid_save_path}")

        # Reset progress bar
        progress_bar['value'] = 0
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while downloading the video. Error: {str(e)}")

# Setting up the GUI
root = tk.Tk()
root.geometry("600x300")
root.title("YT Downloader By SayyadN")
root.configure(bg="black")
root.resizable(False, False)

# Add widgets
url_label = tk.Label(root, text="Enter the URL of the video: ", bg="black", fg="white")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

path_label = tk.Label(root, text="Enter the path where you want to save the video: ", bg="black", fg="white")
path_label.pack()
path_entry = tk.Entry(root, width=50)
path_entry.pack()

check_path_button = tk.Button(root, text="Check Your Path", command=check_path)
check_path_button.pack(pady=5)

resolution_var = tk.StringVar(value="H")  # Default resolution choice
resolution_label = tk.Label(root, text="Choose resolution (H for Highest, L for Lowest): ", bg="black", fg="white")
resolution_label.pack()
resolution_highest = tk.Radiobutton(root, text="Highest (H)", variable=resolution_var, value="H", bg="black", fg="white")
resolution_highest.pack()
resolution_lowest = tk.Radiobutton(root, text="Lowest (L)", variable=resolution_var, value="L", bg="black", fg="white")
resolution_lowest.pack()

download_button = tk.Button(root, text="Download Your Video", command=download_video)
download_button.pack(pady=10)

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

# Run GUI
root.mainloop()

# Code Ends here
# Thank you
# Written By SayyadN