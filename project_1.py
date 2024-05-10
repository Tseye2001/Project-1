import tkinter as tk

class SimpleMathQuiz:
    def __init__(self, root: tk.Tk):
        """starts  the SimpleMathQuiz class."""
        self.root = root
        self.root.title("Tseye's Math Quiz")
        self.root.geometry("240x240")
        self.root.resizable(False, False)

        self.current_question = 0
        self.score = 0
        self.passing_grade = 3

        self.questions = [
            ("What is 2 + 3?", 5),
            ("What is 7 - 4?", 3),
            ("What is 5 + 6?", 11),
            ("What is 9 - 2?", 7),
            ("What is 4 + 8?", 12)
        ]

        self.label_question = tk.Label(root, text="", font=("Arial", 12))
        self.label_question.grid(row=0, column=0, padx=10, pady=10)

        self.entry_answer = tk.Entry(root, font=("Arial", 12))
        self.entry_answer.grid(row=1, column=0, padx=10, pady=10)

        self.button_next = tk.Button(root, text="Next", font=("Arial", 12), command=self.next_question)
        self.button_next.grid(row=2, column=0, padx=10, pady=10)

        self.label_result = tk.Label(root, text="", font=("Arial", 12))
        self.label_result.grid(row=3, column=0, padx=10, pady=10)

        self.back_button = tk.Button(root, text="StartOver", font=("Arial", 12), command=self.restart_quiz)

        self.load_question()

    def load_question(self):
        """Loads the next question in the quiz."""
        if self.current_question < len(self.questions):
            question, _ = self.questions[self.current_question]
            self.label_question.config(text=question)
            self.entry_answer.delete(0, tk.END)
        else:
            self.show_results()

    def next_question(self):
        """Processes the user's answer and loads the next quiz question."""
        try:
            user_answer = int(self.entry_answer.get())
            _, correct_answer = self.questions[self.current_question]
            if user_answer == correct_answer:
                self.score += 1
            self.current_question += 1
            self.load_question()
        except ValueError:
            self.label_result.config(text="Error,insert an integer")
            self.entry_answer.delete(0,tk.END)


    def show_results(self):
        """Displays the quiz results and determining a pass or fail."""
        self.label_question.config(text="")
        self.entry_answer.grid_remove()
        self.button_next.grid_remove()
        if self.score >= self.passing_grade:
            self.label_result.config(text=f"You scored {self.score} out of {len(self.questions)}. You pass!")
        else:
            self.label_result.config(text=f"You scored {self.score} out of {len(self.questions)}.Try again.")
            self.back_button.grid(row=4, column=0, padx=10, pady=10)

    def restart_quiz(self):
        """Restarts the quiz from the beginning."""
        self.current_question = 0
        self.score = 0
        self.label_result.config(text="")
        self.entry_answer.grid()
        self.button_next.grid()
        self.back_button.grid_remove()
        self.load_question()
