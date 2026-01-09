from manim import *
from manim.utils.rate_functions import ease_out_quad, ease_in_quad, ease_in_out_quad, ease_in_out_cubic

class RoboticArmToA(Scene):
    """
    DIPLOMA-LEVEL ANIMATION: Robotic Manipulator → Letter "A"
    
    Six-Act Structure:
    ACT 1: Abstract Energy - Animated lines, dots, arcs establish rhythm
    ACT 2: Assembly - Abstract elements morph into mechanical parts
    ACT 3: Character Movement - Manipulator performs expressive motion
    ACT 4: Deconstruction - Mechanical identity dissolves
    ACT 5: Typographic Resolution - Forms become letter "A"
    ACT 6: Final Hold - Subtle emphasis and calm ending
    
    Visual Strategy:
    - Dark tech aesthetic (#0f1117)
    - Limited palette: Cyan (#00d9ff), Magenta (#ff006e), Yellow (#ffbe0b)
    - Rounded industrial shapes
    - No sudden appearances - every element is earned
    - High-contrast, clean, modern
    """
    
    def construct(self):
        # Dark background - deep tech aesthetic
        self.camera.background_color = "#0f1117"
        
        # Color palette: industrial, limited, high contrast
        CYAN = "#00d9ff"
        MAGENTA = "#ff006e"
        YELLOW = "#ffbe0b"
        LIGHT_GRAY = "#e0e0e0"
        
        # ===== ACT 1: ABSTRACT ENERGY =====
        # Animated lines, dots, and arcs appear with motion and intention
        # They establish rhythm and spatial direction
        
        self._act1_abstract_energy(CYAN, MAGENTA, YELLOW)
        
        # ===== ACT 2: ASSEMBLY =====
        # Abstract elements morph into recognizable mechanical parts
        # Base, joints, and arm segments emerge via Transform
        
        arm_group = self._act2_assembly(CYAN, MAGENTA, YELLOW)
        
        # ===== ACT 3: CHARACTER MOVEMENT =====
        # Manipulator performs confident, expressive motion
        # Anticipation, action, settle - like motion graphics
        
        self._act3_character_movement(arm_group)
        
        # ===== ACT 4: DECONSTRUCTION =====
        # Mechanical identity dissolves
        # Segments align, rotate, straighten - visual complexity reduces
        
        aligned_segments = self._act4_deconstruction(arm_group)
        
        # ===== ACT 5: TYPOGRAPHIC RESOLUTION =====
        # Remaining shapes clearly form capital letter "A"
        # Letter A is built from manipulator geometry - no sudden text
        
        letter_a = self._act5_typographic_resolution(aligned_segments, CYAN, MAGENTA, YELLOW)
        
        # ===== ACT 6: FINAL HOLD =====
        # Subtle camera scale or emphasis
        # Calm ending pose - minimal caption
        
        self._act6_final_hold(letter_a, CYAN)
    
    # ========================================
    # ACT 1: ABSTRACT ENERGY
    # ========================================
    def _act1_abstract_energy(self, CYAN, MAGENTA, YELLOW):
        """
        Create energetic abstract elements that appear with intention.
        Lines, arcs, and dots fade in with motion, establishing spatial rhythm.
        Duration: ~3 seconds
        """
        
        # Animated arc (from bottom-left to top-right)
        arc1 = Arc(
            radius=1.5,
            angle=PI/2,
            arc_center=[-1.5, 0, 0],
            color=CYAN,
            stroke_width=4
        )
        
        # Second arc (offset, secondary color)
        arc2 = Arc(
            radius=1.2,
            angle=PI/2.5,
            arc_center=[0.5, 0.5, 0],
            color=MAGENTA,
            stroke_width=3.5
        )
        
        # Animated lines - establish direction and energy
        energy_line1 = Line(
            start=[-2, -2, 0],
            end=[0, 2, 0],
            color=CYAN,
            stroke_width=3
        )
        
        energy_line2 = Line(
            start=[1, 2.5, 0],
            end=[-0.5, -1.5, 0],
            color=MAGENTA,
            stroke_width=2.5
        )
        
        # Dots punctuate the space (small circles)
        dot1 = Circle(radius=0.12, color=YELLOW, fill_opacity=1)
        dot1.move_to([-2, -2, 0])
        
        dot2 = Circle(radius=0.1, color=CYAN, fill_opacity=1)
        dot2.move_to([0, 2, 0])
        
        dot3 = Circle(radius=0.08, color=MAGENTA, fill_opacity=1)
        dot3.move_to([1, 2.5, 0])
        
        # Fade in with motion - staggered timing
        self.play(FadeIn(arc1), run_time=0.7)
        self.play(FadeIn(dot1), run_time=0.4)
        self.play(FadeIn(energy_line1), run_time=0.8)
        self.play(FadeIn(dot2), run_time=0.3)
        self.play(FadeIn(arc2), run_time=0.7)
        self.play(FadeIn(energy_line2), run_time=0.6)
        self.play(FadeIn(dot3), run_time=0.4)
        
        self.wait(0.8)
        
        # Abstract elements exit to make space
        self.play(
            FadeOut(arc1, arc2, energy_line1, energy_line2, dot1, dot2, dot3),
            run_time=0.9
        )
        
        self.wait(0.3)
    
    # ========================================
    # ACT 2: ASSEMBLY
    # ========================================
    def _act2_assembly(self, CYAN, MAGENTA, YELLOW):
        """
        Abstract elements morph into mechanical parts via Transform.
        Base, joints, and arm segments emerge with intention.
        Duration: ~4-5 seconds
        """
        
        # ---- BASE (Foundation) ----
        base_rect = RoundedRectangle(
            width=1.6,
            height=0.4,
            corner_radius=0.15,
            color=CYAN,
            fill_opacity=0.95,
            stroke_width=2
        )
        base_rect.move_to([-2, -2, 0])
        
        self.play(FadeIn(base_rect), run_time=0.8)
        self.wait(0.3)
        
        # ---- JOINT 1 (Base joint - largest) ----
        joint1 = Circle(
            radius=0.22,
            color=CYAN,
            fill_opacity=0.95,
            stroke_width=2.5
        )
        joint1.move_to([-2, -0.8, 0])
        
        self.play(
            FadeIn(joint1),
            run_time=0.6
        )
        self.wait(0.2)
        
        # ---- SEGMENT 1 (First arm - cyan) ----
        segment1 = Line(
            start=[-2, -0.8, 0],
            end=[-0.3, 1.2, 0],
            color=CYAN,
            stroke_width=10
        )
        
        self.play(
            FadeIn(segment1),
            run_time=0.7,
            rate_func=ease_out_quad
        )
        self.wait(0.2)
        
        # ---- JOINT 2 (Mid joint) ----
        joint2 = Circle(
            radius=0.18,
            color=MAGENTA,
            fill_opacity=0.95,
            stroke_width=2.5
        )
        joint2.move_to([-0.3, 1.2, 0])
        
        self.play(
            FadeIn(joint2),
            run_time=0.5
        )
        self.wait(0.2)
        
        # ---- SEGMENT 2 (Second arm - magenta) ----
        segment2 = Line(
            start=[-0.3, 1.2, 0],
            end=[1.5, 2.1, 0],
            color=MAGENTA,
            stroke_width=8
        )
        
        self.play(
            FadeIn(segment2),
            run_time=0.7,
            rate_func=ease_out_quad
        )
        self.wait(0.2)
        
        # ---- JOINT 3 (End joint - smallest) ----
        joint3 = Circle(
            radius=0.14,
            color=YELLOW,
            fill_opacity=0.95,
            stroke_width=2.5
        )
        joint3.move_to([1.5, 2.1, 0])
        
        self.play(
            FadeIn(joint3),
            run_time=0.5
        )
        self.wait(0.2)
        
        # ---- GRIPPER/END EFFECTOR (Minimal, stylized) ----
        gripper_left = Line(
            start=[1.5, 2.1, 0],
            end=[1.8, 2.75, 0],
            color=YELLOW,
            stroke_width=5
        )
        gripper_right = Line(
            start=[1.5, 2.1, 0],
            end=[1.2, 2.75, 0],
            color=YELLOW,
            stroke_width=5
        )
        
        self.play(
            FadeIn(gripper_left, gripper_right),
            run_time=0.6
        )
        
        self.wait(0.5)
        
        # Assemble complete arm group
        arm_group = VGroup(
            base_rect,
            joint1, segment1,
            joint2, segment2,
            joint3,
            gripper_left, gripper_right
        )
        
        return arm_group
    
    # ========================================
    # ACT 3: CHARACTER MOVEMENT
    # ========================================
    def _act3_character_movement(self, arm_group):
        """
        Manipulator performs confident, expressive motion.
        Shows personality through easing: anticipation, action, settle.
        Duration: ~3-4 seconds
        """
        
        self.wait(0.4)
        
        # ANTICIPATION: Slight rotation back before main motion
        self.play(
            Rotate(arm_group, angle=-0.15, about_point=[-2, -2, 0]),
            run_time=0.5,
            rate_func=ease_in_quad
        )
        
        self.wait(0.2)
        
        # ACTION: Main sweep motion (confident, full)
        self.play(
            Rotate(arm_group, angle=0.8, about_point=[-2, -2, 0]),
            run_time=1.8,
            rate_func=ease_in_out_cubic
        )
        
        self.wait(0.3)
        
        # SETTLE: Return with slight overshoot, then settle
        self.play(
            Rotate(arm_group, angle=-0.85, about_point=[-2, -2, 0]),
            run_time=1.5,
            rate_func=ease_out_quad
        )
        
        self.wait(0.5)
        
        # Small accent move - shows confidence
        self.play(
            Rotate(arm_group, angle=0.05, about_point=[-2, -2, 0]),
            run_time=0.6,
            rate_func=ease_in_out_quad
        )
        
        self.wait(0.4)
        
        # Final reset to neutral
        self.play(
            Rotate(arm_group, angle=-0.05, about_point=[-2, -2, 0]),
            run_time=0.5,
            rate_func=ease_out_quad
        )
        
        self.wait(1)
    
    # ========================================
    # ACT 4: DECONSTRUCTION
    # ========================================
    def _act4_deconstruction(self, arm_group):
        """
        Mechanical identity dissolves.
        Segments align, rotate, and straighten.
        Visual complexity reduces as shapes prepare for typographic form.
        Duration: ~4-5 seconds
        """
        
        # Store original components for transformation
        base_rect = arm_group[0]
        joint1 = arm_group[1]
        segment1 = arm_group[2]
        joint2 = arm_group[3]
        segment2 = arm_group[4]
        joint3 = arm_group[5]
        gripper_left = arm_group[6]
        gripper_right = arm_group[7]
        
        self.wait(0.3)
        
        # Dim the industrial colors slightly
        self.play(
            arm_group.animate.set_opacity(0.8),
            run_time=0.6
        )
        
        self.wait(0.2)
        
        # Move base down and out (will form bottom of "A")
        self.play(
            base_rect.animate.move_to([-0.2, -1.3, 0]),
            run_time=1
        )
        
        self.wait(0.2)
        
        # Left segment becomes left diagonal of "A"
        # Rotate and align it
        self.play(
            segment1.animate.rotate(angle=1.2, about_point=[-0.3, 1.2, 0]),
            segment1.animate.move_to([-0.4, 0.2, 0]),
            run_time=1.2,
            rate_func=ease_in_out_quad
        )
        
        self.wait(0.2)
        
        # Right segment becomes right diagonal
        self.play(
            segment2.animate.rotate(angle=-1.0, about_point=[-0.3, 1.2, 0]),
            segment2.animate.move_to([0.4, 0.2, 0]),
            run_time=1.2,
            rate_func=ease_in_out_quad
        )
        
        self.wait(0.2)
        
        # Joints fade - they're no longer needed visually
        self.play(
            FadeOut(joint1, joint2, joint3, gripper_left, gripper_right),
            run_time=0.8
        )
        
        self.wait(0.3)
        
        # Adjust segment positions for perfect "A" geometry
        self.play(
            segment1.animate.move_to([-0.45, 0.3, 0]),
            segment2.animate.move_to([0.45, 0.3, 0]),
            base_rect.animate.move_to([0, -0.05, 0]).scale(0.8),
            run_time=1,
            rate_func=ease_out_quad
        )
        
        self.wait(0.5)
        
        # Create aligned segments group for next act
        aligned_segments = VGroup(segment1, segment2, base_rect)
        
        return aligned_segments
    
    # ========================================
    # ACT 5: TYPOGRAPHIC RESOLUTION
    # ========================================
    def _act5_typographic_resolution(self, aligned_segments, CYAN, MAGENTA, YELLOW):
        """
        Remaining shapes clearly form capital letter "A".
        Letter is visually built from manipulator geometry.
        No sudden text appearance - transformation is earned.
        Duration: ~3-4 seconds
        """
        
        self.wait(0.3)
        
        # Brighten the aligned segments - they become the letter
        self.play(
            aligned_segments.animate.set_opacity(1),
            run_time=0.6
        )
        
        self.wait(0.2)
        
        # Perfect the left diagonal (left side of "A")
        left_diagonal = Line(
            start=[-0.75, 1.5, 0],
            end=[-0.05, -1.1, 0],
            color=CYAN,
            stroke_width=14
        )
        
        # Perfect the right diagonal (right side of "A")
        right_diagonal = Line(
            start=[0.05, 1.5, 0],
            end=[0.75, -1.1, 0],
            color=CYAN,
            stroke_width=14
        )
        
        # Horizontal bar in middle (crossbar of "A")
        horizontal_bar = Line(
            start=[-0.45, 0.25, 0],
            end=[0.45, 0.25, 0],
            color=MAGENTA,
            stroke_width=10
        )
        
        # Transform the segments into perfect letter geometry
        self.play(
            Transform(aligned_segments[0], left_diagonal),
            run_time=1.2,
            rate_func=ease_in_out_quad
        )
        
        self.wait(0.2)
        
        self.play(
            Transform(aligned_segments[1], right_diagonal),
            run_time=1.2,
            rate_func=ease_in_out_quad
        )
        
        self.wait(0.2)
        
        # Add the horizontal bar (emerge from the base)
        self.play(
            FadeIn(horizontal_bar),
            run_time=0.7,
            rate_func=ease_out_quad
        )
        
        self.wait(0.4)
        
        # Fade out the old base (no longer needed)
        self.play(
            FadeOut(aligned_segments[2]),
            run_time=0.5
        )
        
        self.wait(0.3)
        
        # The letter "A" is now complete and beautiful
        letter_a = VGroup(left_diagonal, right_diagonal, horizontal_bar)
        
        # Quick shine effect - accent highlight on one diagonal
        accent_shine = Line(
            start=[-0.75, 1.5, 0],
            end=[-0.05, -1.1, 0],
            color=YELLOW,
            stroke_width=4
        )
        accent_shine.set_opacity(0)
        
        self.play(
            accent_shine.animate.set_opacity(0.6),
            run_time=0.3
        )
        self.play(
            accent_shine.animate.set_opacity(0),
            run_time=0.4
        )
        
        self.wait(0.5)
        
        return letter_a
    
    # ========================================
    # ACT 6: FINAL HOLD
    # ========================================
    def _act6_final_hold(self, letter_a, CYAN):
        """
        Subtle camera scale or emphasis.
        Calm ending pose - the letter has arrived.
        Optional minimal caption.
        Duration: ~2-3 seconds
        """
        
        self.wait(0.4)
        
        # Subtle scale emphasis - the letter "arrives"
        self.play(
            letter_a.animate.scale(1.15),
            run_time=0.8,
            rate_func=ease_out_quad
        )
        
        self.wait(0.3)
        
        # Slight scale back for balance
        self.play(
            letter_a.animate.scale(0.95),
            run_time=0.6,
            rate_func=ease_in_out_quad
        )
        
        self.wait(0.5)
        
        # Optional: Add subtle caption (minimal)
        caption = Text(
            "TRANSFORMATION",
            font_size=28,
            color=CYAN,
            weight=BOLD
        )
        caption.set_opacity(0.5)
        caption.move_to([0, -2, 0])
        
        self.play(
            FadeIn(caption),
            run_time=1
        )
        
        self.wait(2)
        
        # Final fade to black for cinematic ending
        self.play(
            FadeOut(letter_a, caption),
            run_time=1.2
        )
        
        self.wait(1)