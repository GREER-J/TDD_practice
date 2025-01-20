class MockRender:
    def __init__(self, str_addition: str = '') -> None:
        self.display_render_count = 0
        self.render_history = []
        self.str_addition = str_addition

    def render(self, txt: str) -> str:
        render_str = f"{self.str_addition}{txt}"
        self.render_history.append(render_str)
        self.display_render_count += 1
        return render_str
