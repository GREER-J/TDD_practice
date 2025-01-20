class Display:
    def __init__(self, render, model) -> None:
        self.display_call_count = 0
        self.render = render
        self.model = model

    def display(self, text: str) -> str:
        """Calls a given render function

        Args:
            text (str): Text to display

        Returns:
            str: rendered text
        """
        #TODO remove this line, it doesn't need to be here
        self.display_call_count += 1
        return self.render(text)

    def show_numbers(self, max_val: int) -> None:
        """Generate the number sequence for FizzBuzz

        Args:
            max_val (int): length of the sequence
        """
        for i in range(max_val):
            self.display(self.model(i + 1))
