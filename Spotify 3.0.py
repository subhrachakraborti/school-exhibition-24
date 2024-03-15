import webbrowser
import tkinter as tk

# Function to open playlist link
def open_playlist(genre):
    # Fetch playlist link based on selected genre
    playlist_link = get_youtube_playlist(genre)
    if playlist_link.startswith("http"):
        # Open the playlist link in the default web browser
        webbrowser.open(playlist_link)
    else:
        # Display error message if playlist link is not available
        error_label.config(text=playlist_link)

# Function to fetch playlist from YouTube based on genre
def get_youtube_playlist(genre):
    # You can replace this with your own logic to fetch playlists from YouTube
    # For now, let's just return a sample playlist link
    playlists = {
        "ROCK": "https://open.spotify.com/playlist/37i9dQZF1EQpj7X7UK8OOF",
        "POP": "https://open.spotify.com/playlist/37i9dQZF1EQncLwOalG3K7",
        "HIP-HOP/RAP": "https://open.spotify.com/playlist/37i9dQZF1DX48TTZL62Yht",
        "EDM":"https://open.spotify.com/playlist/37i9dQZF1DX3Kdv0IChEm9",
        "JAZZ":"https://open.spotify.com/playlist/37i9dQZF1EQqA6klNdJvwx",
        "BLUES":"https://open.spotify.com/playlist/37i9dQZF1DXd9rSDyQguIk",
        "CLASSICAL":"https://open.spotify.com/playlist/37i9dQZF1DX3LrQBSMX6aK",
        "COUNTRY":"https://open.spotify.com/playlist/37i9dQZF1EQmPV0vrce2QZ",
        "INDIE":"https://open.spotify.com/playlist/37i9dQZF1DX5q67ZpWyRrZ",
        "METAL":"https://open.spotify.com/playlist/37i9dQZF1EQpgT26jgbgRI"
    }
    return playlists.get(genre, "Playlist not found for the given genre on Spotify.")

# Create Tkinter window
root = tk.Tk()
root.title("Genre Selector")
root.geometry("500x600")  # Set window dimensions
root.configure(bg="cyan")  # Set window background color

# Create a frame to hold the header label and buttons
frame = tk.Frame(root, bg="cyan")
frame.pack(expand=True)

# Function to handle genre selection
def select_genre(genre):
    open_playlist(genre)

# List of genres
genres = ["POP","ROCK","HIP-HOP/RAP","EDM","JAZZ","BLUES","CLASSICAL","COUNTRY","INDIE","METAL"]

# Customize button style
button_style = {
    "bg": "black",
    "fg": "gold",
    "activebackground": "silver",
    "activeforeground": "gold",
    "bd": 2,  # Set button border width
    "relief": "raised"  # Set button relief style
}

# Create a label for the header
header_label = tk.Label(frame, text="CHOOSE YOUR GENRE/MOOD", bg="cyan", fg="dark blue", font=("Travel Sans", 16, "bold"))
header_label.pack(side="top", pady=10)

#Create a label for the header
header_label = tk.Label(frame, text="© Class XI A (Ishiraj, Subhra, Swarnabha, Titas)", bg="cyan", fg="dark blue", font=("Arial", 8, "bold"))
header_label.pack(side="bottom", pady=10)

# Create buttons for each genre
for genre in genres:
    button = tk.Button(frame, text=genre, command=lambda g=genre: select_genre(g), **button_style)
    button.pack(side="top", pady=5)

# Customize label style for error messages
error_style = {
    "fg": "white",
    "bg": "cyan"
}

# Label to display error messages
error_label = tk.Label(root, **error_style)
error_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
