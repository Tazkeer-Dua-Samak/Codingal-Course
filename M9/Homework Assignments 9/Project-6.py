import tkinter as tk
import random

def game_window():
    game_window = tk.Toplevel(root)
    game_window.title("Rock, Paper, Scissors")
    game_window.geometry("450x300")
    game_window.configure(bg="#F0F0F0")

    def play_game(user_choice):
        computer_choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(computer_choices)

        result = ""
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
        else:
            result = "You lose!"             

        result_window = tk.Toplevel(game_window)
        result_window.title("Game Result")
        result_window.geometry("350x200")
        result_window.configure(bg="#E0E0E0")

        # we can change the font of text and even bolden it by using it in Label and Button widgets.
        choice_label = tk.Label(result_window, text=f"You chose: {user_choice}\nComputer chose: {computer_choice}", font=("Arial", 12), bg="#E0E0E0")
        choice_label.pack(pady=10)

        result_label = tk.Label(result_window, text=result, font=("Arial", 16, "bold"), bg="#E0E0E0")
        result_label.pack(pady=5)

        play_again_label = tk.Label(result_window, text="Do you want to play again?", font=("Arial", 12), bg="#E0E0E0")
        play_again_label.pack(pady=10)
        
        def play_again_yes():
            result_window.destroy()  # Using .destroy(), it will automatically close the window when I press the button
        
        def play_again_no():
            result_window.destroy()
            game_window.destroy()
            
        yes_button = tk.Button(result_window, text="Yes", command=play_again_yes, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        yes_button.pack(side="left", padx=20, expand=True)
        
        no_button = tk.Button(result_window, text="No", command=play_again_no, bg="#F44336", fg="white", font=("Arial", 10, "bold"))
        no_button.pack(side="right", padx=20, expand=True)
        
        result_window.mainloop()

    instruction_label = tk.Label(game_window, 
                                 text="Click an image to choose your weapon", 
                                 font=("Arial", 14), 
                                 bg="#F0F0F0")
    instruction_label.pack(pady=20)

    button_frame = tk.Frame(game_window, bg="#F0F0F0")
    button_frame.pack(pady=10)

    # Loading the images and creating buttons with images
    rock_image = tk.PhotoImage(file="rps_piece_1.png")
    paper_image = tk.PhotoImage(file='rps_piece_2.png')
    scissors_image = tk.PhotoImage(file='rps_piece_3.png') 

    rock_button = tk.Button(button_frame, 
                            image=rock_image, 
                            # lambda is used when we need to pass arguments
                            command=lambda: play_game("Rock"),
                            width=100,
                            height=100,
                            bg="#2196F3", 
                            relief=tk.RAISED)
    rock_button.image = rock_image 
    rock_button.pack(side="left", padx=10)

    paper_button = tk.Button(button_frame, 
                             image=paper_image, 
                             command=lambda: play_game("Paper"), 
                             width=100,
                             height=100,
                             bg="#8BC34A", 
                             relief=tk.RAISED)
    paper_button.image = paper_image  
    paper_button.pack(side="left", padx=10)

    scissors_button = tk.Button(button_frame, 
                                image=scissors_image, 
                                command=lambda: play_game("Scissors"), 
                                width=100,
                                height=100,
                                bg="#FF5722", 
                                relief=tk.RAISED)
    scissors_button.image = scissors_image  # I read that if you don't keep a reference to the image it may be deleted during execution
    scissors_button.pack(side="left", padx=10)

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x200")
root.configure(bg="#E6E6FA")

welcome_label = tk.Label(root, 
                         text="Welcome to Rock, Paper, Scissors Game", 
                         font=("Arial", 16, "bold"), 
                         bg="#E6E6FA")
welcome_label.pack(pady=30)

start_button = tk.Button(root, 
                         text="Click to play!", 
                         command=game_window,
                         font=("Arial", 12),
                         bg="#9370DB", 
                         fg="white", 
                         relief=tk.RAISED)
start_button.pack(pady=10)

root.mainloop()