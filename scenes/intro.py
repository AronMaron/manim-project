from manim import *

class DiplomaIntro(Scene):
    def construct(self):

        self.camera.background_color = "#9d1834"

        # --- Base ---
        base = RoundedRectangle(
            width=4,
            height=0.6,
            corner_radius=0.15,
            fill_color=BLUE_D,
            fill_opacity=1,
            stroke_width=0
        )

        # --- First arm ---
        arm1 = RoundedRectangle(
            width=3,
            height=0.4,
            corner_radius=0.12,
            fill_color=TEAL_A,
            fill_opacity=1,
            stroke_width=0
        )
        arm1.next_to(base, UP, buff=0)

        # --- Second arm ---
        arm2 = RoundedRectangle(
            width=2.5,
            height=0.35,
            corner_radius=0.1,
            fill_color=TEAL_C,
            fill_opacity=1,
            stroke_width=0
        )
        arm2.next_to(arm1, RIGHT, buff=0)

        # --- Joints ---
        joint1 = Dot(base.get_top(), radius=0.08, color=GREY_B)
        joint2 = Dot(arm1.get_right(), radius=0.07, color=GREY_B)

        # --- Group ---
        manipulator = VGroup(base, arm1, arm2, joint1, joint2)
        manipulator.move_to(ORIGIN)

        # --- Intro text ---
        title = Text("Robotic Manipulator", font_size=42, color=WHITE)
        subtitle = Text("Visual Animation Concept", font_size=26, color=GREY_A)
        subtitle.next_to(title, DOWN)

        # --- Animation sequence ---
        self.play(FadeIn(title, shift=UP), run_time=1.2)
        self.play(Write(subtitle), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(subtitle))
        self.wait(0.5)

        self.play(Create(base), run_time=1)
        self.wait(0.2)

        self.play(Create(arm1), FadeIn(joint1), run_time=1)
        self.wait(0.2)

        self.play(Create(arm2), FadeIn(joint2), run_time=1)
        self.wait(0.5)

        self.play(
            Rotate(
                arm1,
                angle=PI / 8,
                about_point=joint1.get_center()
            ),
            Rotate(
                arm2,
                angle=-PI / 6,
                about_point=joint2.get_center()
            ),
            run_time=2,
            rate_func=smooth
        )

        self.wait(1)
