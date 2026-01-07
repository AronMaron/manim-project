from manim import*

class TestScene(Scene):
    def construct(self):
        text = Text("Manim Works!!!")
        self.play(Write(text))
        self.wait(2)
