import tkinter as tk
import markovify
import time
import os

def slow_print(text, delay=0.02):
    for char in text:
        lyrics_text.insert(tk.END, char)
        lyrics_text.see(tk.END)  # Scrolls to the end of the text
        time.sleep(delay)  # Adjust the delay for the desired printing speed
        lyrics_text.update()  # Update the text widget

def generate_lyrics():
    # Load a text file as a corpus
    with open(r"C:\Users\Subhra Chakraborti\OneDrive\Desktop\New folder (2)\lyrics.txt") as f:
        text = f.read()

    # Build a Markov model
    text_model = markovify.NewlineText(text)

    # Generate 30 unique sentences
    unique_sentences = set()
    while len(unique_sentences) < 20:
        generated_sentence = text_model.make_sentence()
        if generated_sentence is not None:
            unique_sentences.add(generated_sentence)

    # Group sentences into 4 paragraphs
    sentences_per_paragraph = 7
    paragraphs = [list(unique_sentences)[i:i+sentences_per_paragraph] for i in range(0, len(unique_sentences), sentences_per_paragraph)]

    # Print the paragraphs like a song
    for i, paragraph in enumerate(paragraphs, start=1):
        slow_print("\n")
        slow_print(f"Verse {i}:\n")
        for sentence in paragraph:
            slow_print(sentence + '\n')
        slow_print('\n')

        # Add horizontal rule after every third verse
        if i % 3 == 0:
            lyrics_text.insert(tk.END, "\n----------------------------------------\n")
            lyrics_text.see(tk.END)  # Scrolls to the end of the text
            lyrics_text.update()  # Update the text widget

    # Add information about class members before the last line
    lyrics_text.insert(tk.END, "BY CLASS XI A (2023-24)\nISHIRAJ PALCHAUDHURI [18]\nSUBHRA CHAKRABORTI [40]\nSWARNABHA CHANDA [42]\nTITAS GURIA [43]\n")
    lyrics_text.insert(tk.END, "-------------------------------------------------------------\n\n")

def open_custom_lyrics():
    # Open a text file with a given location
    file_path = r"C:\Users\Subhra Chakraborti\OneDrive\Desktop\New folder (2)\lyrics.txt"  # Replace with the actual path to your text file
    if os.path.exists(file_path):
        os.startfile(file_path)
    else:
        print("File not found.")

# Create Tkinter window
root = tk.Tk()
root.title("Lyrics Generator")

# Set window size to 1000x800 pixels
root.geometry("800x700")

# Introduction
intro = "Once upon a time, in land of words, lived the Songwriter!\n"
intro += "Welcome, traveler, to the realm of Sentence Sorcerer: The Textual Tinkerer!\n"
intro += "Prepare to embark on an enchanting journey through the art of lyrics generation!\n"
intro += "\n-------------------------------------------------------------\n"
lyrics_text = tk.Text(root, width=80, height=20, font=("Times New Roman", 15))  # Set font size to 15
lyrics_text.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)  # Pack lyrics_text widget
slow_print(intro)  # Call slow_print after lyrics_text is defined

# Customize button style
button_style = {
    "bg": "gold",
    "fg": "dark blue",
    "activebackground": "dark blue",
    "activeforeground": "white",
    "font": ("Josefin Sans", 18),
    "borderwidth": 2,
    "relief": "raised"
}

# Button to generate lyrics
generate_button = tk.Button(root, text="Generate Lyrics", command=generate_lyrics, **button_style)
generate_button.pack(side=tk.TOP, padx=10, pady=10)

# Button to enter custom lyrics
custom_button = tk.Button(root, text="Enter Your Own Lyrics", command=open_custom_lyrics, **button_style)
custom_button.pack(side=tk.TOP, padx=10, pady=10)

# Additional text below the button
additional_text = "Class XI A - Ishiraj, Subhra, Swarnabha & Titas"
additional_label = tk.Label(root, text=additional_text, fg="black", font=("Times New Roman", 12), bg="white")
additional_label.pack(side=tk.TOP, padx=10, pady=(0, 20), fill=tk.X)

# Run the Tkinter event loop
root.mainloop()
