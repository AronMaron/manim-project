from manim import *
import numpy as np

# --- 1. ПАЛИТРА ---
PALETTE = {
    "background": "#1A1A1A",
    "robot_accent": "#00E5FF",
    "robot_link": "#E0E0E0",
    "zen_sphere_off": "#4A4A4A",
    "zen_sphere_on": "#FF4081",
    "grid": "#333333",
    "connection_line": "#FFF59D"
}

# --- 2. ФУНКЦИЯ СОЗДАНИЯ РОБОТА ---
# Эта функция проста и надежна, мы ее оставляем.
def create_robot_arm(accent_color, link_color, scale=1.0):
    link1 = Line(ORIGIN, UP * 2.0, color=link_color, stroke_width=4)
    link2 = Line(link1.get_end(), link1.get_end() + UP * 1.5, color=link_color, stroke_width=4)
    dot = Dot(color=accent_color, radius=0.12)
    arm = VGroup(link1, link2, dot).scale(scale)
    return arm

# --- 3. ОСНОВНАЯ СЦЕНА ---
# Используется НАДЕЖНЫЙ метод "привязки к цели". Класс RobotDance ПОЛНОСТЬЮ УДАЛЕН.
class ZenGardenScene(Scene):
    def construct(self):
        # -- SCENE SETUP --
        self.camera.background_color = PALETTE["background"]
        grid = NumberPlane(background_line_style={"stroke_color": PALETTE["grid"], "stroke_opacity": 0.3})
        
        sphere1 = Dot(point=RIGHT * 4, radius=0.3, color=PALETTE["zen_sphere_off"])
        sphere2 = Dot(point=LEFT * 3 + UP * 2, radius=0.3, color=PALETTE["zen_sphere_off"])
        sphere3 = Dot(point=LEFT * 3 + DOWN * 2, radius=0.3, color=PALETTE["zen_sphere_off"])
        
        zen_objects = VGroup(sphere1, sphere2, sphere3)
        main_robot = create_robot_arm(PALETTE["robot_accent"], PALETTE["robot_link"])
        # Задаем начальную позицию "базы" робота
        main_robot_origin = LEFT * 8
        main_robot.move_to(main_robot_origin)
        
        world = VGroup(grid, zen_objects, main_robot)
        self.add(world)

        # -- СОЗДАЕМ НЕВИДИМУЮ ЦЕЛЬ И "ПРИВЯЗКУ" --
        target_dot = Dot(main_robot[2].get_center(), radius=0)

        def arm_updater(robot):
            target_pos = target_dot.get_center()
            link1, link2, end_effector_dot = robot
            
            # Важно: база робота теперь зафиксирована
            origin = main_robot_origin
            max_reach = 3.5
            
            vec = target_pos - origin
            dist = np.linalg.norm(vec)
            if dist == 0: # Защита от деления на ноль и нулевых векторов
                return 
            if dist > max_reach:
                vec *= max_reach / dist

            joint1_pos = origin + vec * (2.0 / max_reach)
            link1.put_start_and_end_on(origin, joint1_pos)
            link2.put_start_and_end_on(joint1_pos, target_pos)
            end_effector_dot.move_to(target_pos)

        main_robot.add_updater(arm_updater)
        
        # -- АНИМАЦИЯ: МЫ ДВИГАЕМ ТОЛЬКО ЦЕЛЬ `target_dot` --

        # АКТЫ 1-3
        self.play(world.animate.scale(1.2).move_to(zen_objects.get_center() * -0.5), run_time=2)
        self.wait(1)
        
        self.play(
            target_dot.animate.move_to(ORIGIN),
            world.animate.move_to(ORIGIN),
            run_time=4, rate_func=smooth
        )
        self.wait(1)

        self.play(target_dot.animate.move_to(sphere1.get_center()), run_time=2)
        self.play(Wiggle(sphere1), sphere1.animate.set_color(PALETTE["zen_sphere_on"]))
        self.wait(0.5)
        
        self.play(target_dot.animate.move_to(sphere2.get_center()), run_time=3)
        self.play(Wiggle(sphere2), sphere2.animate.set_color(PALETTE["zen_sphere_on"]))
        self.wait(0.5)
        
        self.play(target_dot.animate.move_to(sphere3.get_center()), run_time=2)
        self.play(Wiggle(sphere3), sphere3.animate.set_color(PALETTE["zen_sphere_on"]))
        self.wait(1)
        
        # АКТ 4: СОЕДИНЕНИЕ
        main_robot.clear_updaters() # Отключаем "привязку"
        self.play(Uncreate(main_robot))

        line12 = Line(sphere1.get_center(), sphere2.get_center(), color=PALETTE["connection_line"], stroke_width=4)
        line23 = Line(sphere2.get_center(), sphere3.get_center(), color=PALETTE["connection_line"], stroke_width=4)
        line31 = Line(sphere3.get_center(), sphere1.get_center(), color=PALETTE["connection_line"], stroke_width=4)
        connection_system = VGroup(line12, line23, line31)
        
        self.play(
            LaggedStart(
                ShowPassingFlash(line12.copy().set_color(WHITE), time_width=0.5), Create(line12),
                ShowPassingFlash(line23.copy().set_color(WHITE), time_width=0.5), Create(line23),
                ShowPassingFlash(line31.copy().set_color(WHITE), time_width=0.5), Create(line31),
                lag_ratio=0.7
            ), run_time=4
        )
        
        final_system = VGroup(zen_objects, connection_system)
        self.play(Flash(final_system, color=WHITE, time_width=0.5))
        self.wait(1)
        
        self.play(world.animate.scale(1/1.2).move_to(ORIGIN), run_time=2)
        self.wait(3)

# VER: 3.0 FINAL STABLE