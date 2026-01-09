from manim import *
import numpy as np

# --- 1. ПАЛИТРА ---
PALETTE = {
    "background": "#111111", 
    "accent": "#00E5FF",      # Неон (Циан)
    "body_main": "#b2bec3",   # Светло-серый металл
    "body_shadow": "#636e72", # Темно-серый для объема
    "joint_color": "#2d3436", # Темные суставы
    "base_color": "#1e272e",
    "laser": "#FF0055",
    "grid": "#222222",
}

# --- 2. ГЕНЕРАТОР "МОНОЛИТНОГО" РОБОТА ---
def generate_solid_robot(points):
    # Этот метод создает робота как единую структуру с правильным порядком слоев
    robot_group = VGroup()
    
    # Слой 1: Рычаги (Limbs) - они находятся внизу
    limbs = VGroup()
    for i in range(len(points) - 1):
        start = points[i]
        end = points[i+1]
        # Используем Line с закругленными краями (cap_style=1) для монолитности
        # Толстая основа
        limb = Line(start, end, stroke_width=24, color=PALETTE["body_main"])
        limb.set_stroke(opacity=1) 
        # Тонкая линия для объема
        deco = Line(start, end, stroke_width=6, color=PALETTE["body_shadow"])
        
        # Группируем звено
        limbs.add(limb, deco)
    
    # Слой 2: Суставы (Joints) - они лежат ПОВЕРХ рычагов
    joints = VGroup()
    for i, point in enumerate(points):
        if i == 0: continue # Базу пропускаем
        
        if i == len(points) - 1: # Кончик (Лапа)
            foot = RoundedRectangle(corner_radius=0.1, height=0.3, width=0.6, color=PALETTE["joint_color"], fill_opacity=1).move_to(point)
            # Неоновое свечение внутри лапы
            core = Dot(point, color=PALETTE["accent"], radius=0.1)
            glow = Dot(point, color=PALETTE["accent"], radius=0.4, fill_opacity=0.3)
            joints.add(foot, glow, core)
        else: # Промежуточные шарниры
            # Внешний круг (темный)
            outer = Dot(point, radius=0.25, color=PALETTE["joint_color"])
            # Внутренний круг (металл)
            inner = Dot(point, radius=0.12, color=PALETTE["body_main"])
            # Центр (болт)
            bolt = Dot(point, radius=0.04, color=PALETTE["joint_color"])
            joints.add(outer, inner, bolt)

    # ВАЖНО: Добавляем в таком порядке, чтобы суставы перекрывали концы линий
    robot_group.add(limbs, joints)
    return robot_group

# --- 3. ГЕНЕРАТОР БАЗЫ ---
def create_heavy_base(position):
    # Рисуем тяжелую платформу
    base = RoundedRectangle(corner_radius=0.1, width=3, height=0.6, color=PALETTE["base_color"], fill_opacity=1)
    # Детали
    detail = Rectangle(width=2.6, height=0.1, color=PALETTE["accent"], fill_opacity=0.5, stroke_width=0)
    detail.move_to(base.get_bottom() + UP*0.15)
    
    group = VGroup(base, detail).move_to(position)
    return group

# --- 4. ОСНОВНАЯ СЦЕНА ---
class MorphScene(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["background"]
        grid = NumberPlane(background_line_style={"stroke_color": PALETTE["grid"], "stroke_opacity": 0.3})
        self.add(grid)

        # --- ГЕОМЕТРИЯ ---
        # Центрирование буквы А
        CENTER_X = 0
        CENTER_Y = 0
        
        # Координаты узлов буквы А (относительно центра)
        # База (Левая нога)
        P1_BASE = np.array([-1.2, -2.0, 0])
        # Вершина
        P3_APEX = np.array([0.4, 2.2, 0]) # Смещение вправо для курсива
        # Правая нога
        P4_FOOT = np.array([2.0, -2.0, 0])
        
        # P2 (Левое колено) - Точка на прямой между низом и верхом
        # P1 + 45% пути до P3
        P2_JOINT = P1_BASE + (P3_APEX - P1_BASE) * 0.45

        points_pose_a = [P1_BASE, P2_JOINT, P3_APEX, P4_FOOT]
        
        # Начальная поза "Змейка" (сложенный робот)
        # Он начинается там же, где база
        points_idle = [
            P1_BASE,
            P1_BASE + UP*1.5 + LEFT*0.5,
            P1_BASE + UP*2.5 + RIGHT*0.5,
            P1_BASE + UP*1.5 + RIGHT*0.5
        ]

        # --- СОЗДАНИЕ ОБЪЕКТОВ ---
        
        # 1. База
        base = create_heavy_base(P1_BASE)
        
        # 2. Роботы (Создаем два состояния)
        robot_idle = generate_solid_robot(points_idle)
        robot_pose_a = generate_solid_robot(points_pose_a)
        
        # 3. Лазер
        laser_start = P2_JOINT
        # Лазер идет горизонтально вправо до пересечения с правой ногой
        # Для простоты визуально находим точку на правой ноге
        laser_end = P3_APEX + (P4_FOOT - P3_APEX) * 0.55
        laser_beam = Line(laser_start, laser_end, color=PALETTE["laser"], stroke_width=0)

        # 4. Буква А (Итоговая)
        letter_A = Text("A", font="Arial", font_size=550, weight=BOLD, slant=ITALIC, color=PALETTE["accent"])
        # Тонкая подстройка позиции буквы под робота
        letter_A.move_to(ORIGIN).shift(DOWN*0.1 + LEFT*0.1)

        # --- АНИМАЦИЯ ---

        # 1. Появление Базы
        self.play(DrawBorderThenFill(base), run_time=1)
        
        # 2. Появление Робота (ЧЕРЧЕНИЕ)
        # Create рисует контуры, это предотвращает "разлет" деталей
        self.play(Create(robot_idle), run_time=2)
        self.wait(0.5)

        # 3. Трансформация в Позу А
        # ReplacementTransform здесь сработает идеально, так как структура объектов идентична
        self.play(
            ReplacementTransform(robot_idle, robot_pose_a),
            run_time=2.5,
            rate_func=rush_into
        )
        
        # 4. Лазер (Создание перекладины)
        self.play(
            laser_beam.animate.set_stroke_width(12).set_color(PALETTE["laser"]),
            Flash(laser_start, color=PALETTE["laser"], line_length=0.5, num_lines=10),
            Flash(laser_end, color=PALETTE["laser"], line_length=0.5, num_lines=10),
            run_time=1.0
        )
        self.wait(0.3)

        # Группировка для финала
        # Важно: robot_idle уже превратился в robot_pose_a, поэтому группируем robot_pose_a
        full_assembly = VGroup(base, robot_pose_a, laser_beam)

        # 5. Метаморфоза в Букву
        big_flash = Flash(ORIGIN, color=WHITE, line_length=6, num_lines=60, flash_radius=2.5, run_time=0.8)
        
        self.play(
            ReplacementTransform(full_assembly, letter_A),
            big_flash,
            run_time=0.8,
            rate_func=smooth
        )

        # 6. Финальные титры
        self.play(letter_A.animate.set_color(WHITE), run_time=0.2)
        self.play(letter_A.animate.set_color(PALETTE["accent"]), run_time=0.5)

        title = Text("VISUALIZATION", font="Arial", font_size=32, color=GRAY, weight=BOLD)
        title.next_to(letter_A, DOWN, buff=0.5)
        self.play(Write(title))
        
        self.wait(3)