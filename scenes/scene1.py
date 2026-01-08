from manim import*

class BaseScene(Scene):
    def construct(self):
        square = Square()
        circle = Circle()

        self.play(Create(square))
        self.wait(0.5)
        self.play(Transform(square,circle))
        self.wait(0.5)

class Basics(Scene):
    def construct(self):
        axes = Axes()
        dot =Dot(ORIGIN)
        square = Square()

        self.play(Create(axes))
        self.play(FadeIn(dot))
        self.play(Create(square))
        self.wait(1)

class LinkTest(Scene):
    def construct(self):
        link = Rectangle(width=3,height=0.3)
        joint = Dot(link.get_left())

        self.add(joint)
        self.play(Create(link))
        self.wait(1)

class RotationTest(Scene):
    def construct(self):
        link = Rectangle(width=3, height=0.3)
        joint = Dot(link.get_left())

        self.add(joint)
        self.add(link)

        self.play(
            Rotate(
                link,
                angle=PI/4,
                about_point=joint.get_center()
            )
        )
        self.wait(1)

        

