import tkinter
import random
import time

# List of possible colours.
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
highest_score = 0  # Variable to store the highest score
timeleft = 60
total_entries = 0
correct_entries = 0
start_time = None

# Function that will start the game.
def startGame(event=None):
    global timeleft
    global start_time

    if timeleft == 60:
        # Start the countdown timer.
        countdown()
        start_time = time.time()

    # Run the function to choose the next colour.
    nextColour()

# Function to choose and display the next colour.
def nextColour():
    global score
    global timeleft
    global highest_score
    global total_entries
    global correct_entries

    # If a game is currently in play
    if timeleft > 0:
        # Make the text entry box active.
        e.focus_set()

        # If the colour typed is equal to the colour of the text
        if e.get().lower() == colours[1].lower():
            score += 1
            correct_entries += 1

        total_entries += 1

        # Update the highest score if the current score is higher
        if score > highest_score:
            highest_score = score

        # Clear the text entry box.
        e.delete(0, tkinter.END)

        random.shuffle(colours)

        # Change the colour to type, by changing the text _and_ the colour to a random colour value
        label.config(fg=str(colours[1]), text=str(colours[0]))

        # Update the score.
        scoreLabel.config(text="Score: " + str(score))
        highestScoreLabel.config(text="Highest Score: " + str(highest_score))

# Countdown timer function
def countdown():
    global timeleft

    # If a game is in play
    if timeleft > 0:
        # Decrement the timer.
        timeleft -= 1

        # Update the time left label
        timeLabel.config(text="Time left: " + str(timeleft))

        # Run the function again after 1 second.
        timeLabel.after(1000, countdown)
    else:
        # Game over, show the play again button
        playAgainButton.pack()
        accuracy = (correct_entries / total_entries) * 100 if total_entries > 0 else 0
        end_time = time.time()
        elapsed_time = end_time - start_time
        typing_speed = total_entries / (elapsed_time / 60) if elapsed_time > 0 else 0
        accuracyLabel.config(text="Accuracy: {:.2f}%".format(accuracy))
        typingSpeedLabel.config(text="Typing Speed: {:.2f} entries/min".format(typing_speed))

# Function to reset the game and play again
def playAgain():
    global score
    global timeleft
    global total_entries
    global correct_entries
    global start_time

    # Reset all variables
    score = 0
    timeleft = 60
    total_entries = 0
    correct_entries = 0
    start_time = None

    # Reset labels
    scoreLabel.config(text="Press enter to start")
    timeLabel.config(text="Time left: " + str(timeleft))
    highestScoreLabel.config(text="Highest Score: " + str(highest_score))
    accuracyLabel.config(text="Accuracy: ")
    typingSpeedLabel.config(text="Typing Speed: ")

    # Hide the play again button
    playAgainButton.pack_forget()

    # Start the game
    startGame()


# Create a GUI window
root = tkinter.Tk()

# Set the title
root.title("COLORGAME")

# Set the size
root.geometry("800x400")

# Add an instructions label
instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!",
                             font=('Helvetica', 12))
instructions.pack()

# Add a score label
scoreLabel = tkinter.Label(root, text="Press enter to start",
                           font=('Helvetica', 12))
scoreLabel.pack()

# Add a highest score label
highestScoreLabel = tkinter.Label(root, text="Highest Score: " + str(highest_score),
                                  font=('Helvetica', 12))
highestScoreLabel.pack()

# Add a time left label
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

# Add a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# Add a text entry box for typing in colours
e = tkinter.Entry(root)

# Run the 'startGame' function when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# Set focus on the entry box
e.focus_set()

# Add a play again button
playAgainButton = tkinter.Button(root, text="Play Again", command=playAgain)

# Add labels for accuracy and typing speed
accuracyLabel = tkinter.Label(root, text="Accuracy: ", font=('Helvetica', 12))
accuracyLabel.pack()

typingSpeedLabel = tkinter.Label(root, text="Typing Speed: ", font=('Helvetica', 12))
typingSpeedLabel.pack()

# Start the GUI
root.mainloop()
