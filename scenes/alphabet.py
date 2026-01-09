from manim import *
import numpy as np

# --- 1. ПАЛИТРА ---
PALETTE = {
    "background": "#0F0F0F",
    "accent": "#00E5FF",      # Цвет робота
    "link": "#CFD8DC",        # Цвет звеньев
    "text_burn": "#FFEB3B",   # Горящий текст
    "text_cool": "#FFFFFF",   # Остывший текст
    "laser_beam": "#FF0055",  # Луч
    "grid": "#222222",
}

# --- 2. ГЕНЕРАТОРЫ ---
def create_robot_arm(accent_color, link_color):
    link1 = Line(ORIGIN, UP * 2.2, color=link_color, stroke_width=8)
    joint1 = Circle(radius=0.15, color=GREY, fill_opacity=1, fill_color=BLACK).move_to(ORIGIN)
    link2 = Line(link1.get_end(), link1.get_end() + UP * 1.8, color=link_color, stroke_width=8)
    joint2 = Circle(radius=0.12, color=GREY, fill_opacity=1, fill_color=BLACK).move_to(link1.get_end())
    
    head = VGroup()
    casing = RoundedRectangle(corner_radius=0.05, height=0.4, width=0.3, color=GREY_D, fill_opacity=1)
    lens = Dot(radius=0.08, color=accent_color)
    glow = Dot(radius=0.2, color=accent_color, fill_opacity=0.3)
    head.add(casing, glow, lens).move_to(link2.get_end())
    
    return VGroup(link1, link2, head, joint1, joint2)

def create_base(position):
    base = VGroup()
    plat = RoundedRectangle(corner_radius=0.1, width=3, height=0.5, color="#263238", fill_opacity=1)
    line = Line(LEFT*1.2, RIGHT*1.2, color=PALETTE["accent"], stroke_width=3).shift(DOWN*0.1)
    base.add(plat, line).move_to(position)
    return base

# --- 3. ОСНОВНАЯ СЦЕНА ---
class LaserWritingScene(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["background"]
        grid = NumberPlane(background_line_style={"stroke_color": PALETTE["grid"], "stroke_opacity": 0.4})
        self.add(grid)

        # --- НАСТРОЙКА ТЕКСТА ---
        text_group = Text("Misha", font="Arial", font_size=144, weight=BOLD)
        text_group.move_to(UP * 1.5)
        text_group.set_fill(opacity=0).set_stroke(color=PALETTE["text_burn"], width=0)

        # --- НАСТРОЙКА РОБОТА ---
        base_pos = DOWN * 2.5
        base = create_base(base_pos)
        robot = create_robot_arm(PALETTE["accent"], PALETTE["link"])
        robot.move_to(base_pos + UP*0.2)
        
        target_dot = Dot(radius=0).move_to(robot[2].get_center())

        # --- ЛОГИКА IK (Inverse Kinematics) ---
        def robot_updater(mob):
            target = target_dot.get_center()
            l1, l2, head, j1, j2 = mob
            origin = j1.get_center()
            
            len1 = 2.2
            len2 = 1.8
            
            vec = target - origin
            dist = np.linalg.norm(vec)
            
            max_len = len1 + len2 - 0.01
            if dist > max_len:
                vec = vec * (max_len / dist)
                dist = max_len
            elif dist < 0.1:
                dist = 0.1
                
            angle_base = np.arctan2(vec[1], vec[0])
            
            cos_angle_mid = (dist**2 - len1**2 - len2**2) / (2 * len1 * len2)
            cos_angle_mid = np.clip(cos_angle_mid, -1.0, 1.0)
            angle_mid = np.arccos(cos_angle_mid)
            
            cos_angle_a = (len1**2 + dist**2 - len2**2) / (2 * len1 * dist)
            cos_angle_a = np.clip(cos_angle_a, -1.0, 1.0)
            angle_a = np.arccos(cos_angle_a)
            
            final_angle1 = angle_base + angle_a
            
            new_elbow_pos = origin + np.array([np.cos(final_angle1), np.sin(final_angle1), 0]) * len1
            l1.put_start_and_end_on(origin, new_elbow_pos)
            j2.move_to(new_elbow_pos)
            
            l2.put_start_and_end_on(new_elbow_pos, target)
            head.move_to(target)
            head.rotate(0) 

        robot.add_updater(robot_updater)
        
        # --- ЛАЗЕР (С ЗАЩИТОЙ ОТ ОШИБОК) ---
        laser_beam = Line(stroke_width=0, color=PALETTE["laser_beam"])
        
        def laser_updater(beam):
            start = robot[2].get_center()
            end = target_dot.get_center()
            
            # ЗАЩИТА: Если точки слишком близко, чуть сдвигаем конец
            if np.linalg.norm(end - start) < 0.01:
                end = start + RIGHT * 0.01 # Микроскопический сдвиг, чтобы не было деления на 0
            
            if beam.stroke_opacity > 0:
                beam.put_start_and_end_on(start, end)
            else:
                # Даже когда лазер выключен, держим его длину не нулевой
                beam.put_start_and_end_on(start, start + RIGHT * 0.01)

        laser_beam.add_updater(laser_updater)

        spark = Dot(radius=0.08, color=YELLOW).set_opacity(0)
        spark.add_updater(lambda s: s.move_to(target_dot.get_center()))

        self.add(base, robot, laser_beam, spark)

        # --- АНИМАЦИЯ ---
        self.play(FadeIn(base, shift=UP), run_time=1)
        self.play(FadeIn(robot), run_time=1)
        self.wait(0.5)

        # --- ЦИКЛ РИСОВАНИЯ ---
        for i, letter in enumerate(text_group):
            
            # Manim хранит части буквы в submobjects. Если их нет, значит буква цельная.
            parts = letter.submobjects if len(letter.submobjects) > 0 else [letter]
            
            for part in parts:
                # 1. Подготовка: летим к началу части
                # ИСПРАВЛЕНИЕ: Используем универсальный способ получить начало кривой
                if hasattr(part, "get_start"):
                    start_point = part.get_start()
                else:
                    # Если вдруг метод не сработает, берем центр (как запасной вариант)
                    start_point = part.get_center()

                self.play(
                    target_dot.animate.move_to(start_point),
                    run_time=0.5,
                    rate_func=smooth
                )

                # 2. Включаем лазер
                self.play(
                    laser_beam.animate.set_stroke_width(4).set_stroke_opacity(1),
                    spark.animate.set_opacity(1),
                    run_time=0.05
                )

                # 3. Рисуем
                part.set_stroke(color=PALETTE["text_burn"], width=4)
                
                self.play(
                    MoveAlongPath(target_dot, part),
                    Create(part),
                    run_time=0.8,
                    rate_func=linear
                )

                # 4. Выключаем лазер
                self.play(
                    laser_beam.animate.set_stroke_width(0).set_stroke_opacity(0),
                    spark.animate.set_opacity(0),
                    run_time=0.05
                )
            
            # Остывание
            self.play(
                letter.animate.set_stroke(color=PALETTE["text_cool"], width=0).set_fill(color=WHITE, opacity=1),
                run_time=0.2
            )

        # --- ФИНАЛ ---
        park_pos = base_pos + UP * 1.5 + RIGHT * 3
        self.play(target_dot.animate.move_to(park_pos), run_time=1.5, rate_func=smooth)
        
        self.play(
            text_group.animate.scale(1.2).set_color(PALETTE["accent"]),
            Flash(text_group, color=WHITE, line_length=1),
            run_time=0.5
        )
        self.play(text_group.animate.scale(1/1.2), run_time=0.5)

        self.wait(3)