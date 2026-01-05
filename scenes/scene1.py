from manim import* 

class HelloManim(scene):
    def construct(self):
        text = Text("Hello,Manim")
        self.play(Write(text))
        self.wait(2) 
