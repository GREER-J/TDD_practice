class Display:
    def __init__(self, render, model) -> None:
        self.display_call_count = 0
        self.render = render
        self.model = model
    
    def display(self, text: str) -> str:
        self.display_call_count += 1
        return self.render(text)
    
    def show_numbers(self, max_val: int) -> None:
        for i in range(max_val):
            self.display(self.model(i + 1))
