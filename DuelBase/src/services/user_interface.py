from tkinter import Tk, ttk, PhotoImage, StringVar, LEFT


class UserInterface:
    def __init__(self):
        self.hero_health = StringVar(value="Hero HP: 100")
        self.enemy_health = StringVar(value="Enemy HP: 100")
        self.combat_log = StringVar(value="Combat log...")
        self.hero_image: PhotoImage | None = None
        self.enemy_image: PhotoImage | None = None

    def _create_placeholder_image(
        self, color_map: list[list[str]], pixel_size: int = 10
    ) -> PhotoImage:
        """
        color_map: 2D-Liste von Farbnamen als Strings, z.B. "blue", "red"
        pixel_size: Größe eines Pixels im PhotoImage
        """
        height = len(color_map)
        width = len(color_map[0])
        img = PhotoImage(width=width * pixel_size, height=height * pixel_size)

        for y, row in enumerate(color_map):
            for x, color in enumerate(row):
                # Zeichne jeden "Pixel" als ein kleines Rechteck
                for dy in range(pixel_size):
                    for dx in range(pixel_size):
                        img.put(color, (x * pixel_size + dx, y * pixel_size + dy))
        return img

    def _setup_main_frame(self, ui: Tk) -> ttk.Frame:
        frm = ttk.Frame(ui, padding=10)
        frm.grid()
        ttk.Label(frm, text="DuelBase").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=ui.destroy).grid(column=1, row=0)
        return frm

    def _setup_top_frame(self, frm: ttk.Frame) -> ttk.Frame:
        top_frame = ttk.Frame(frm)
        top_frame.grid(row=0, column=0, sticky="ew", pady=10)
        top_frame.columnconfigure(0, weight=1)
        top_frame.columnconfigure(1, weight=1)
        return top_frame

    def _setup_hero_panel(self, top_frame: ttk.Frame) -> ttk.Frame:
        hero_panel = ttk.Frame(top_frame, borderwidth=2, relief="solid", padding=5)
        hero_panel.grid(row=0, column=0, sticky="nsew", padx=5)
        ttk.Label(hero_panel, text="Hero").pack()
        # Platzhalter-Held (10x6 Pixel)
        hero_colors = [
            [
                "blue",
                "blue",
                "blue",
                "blue",
                "blue",
                "blue",
                "blue",
                "blue",
                "blue",
                "blue",
            ],
            [
                "blue",
                "gold",
                "gold",
                "blue",
                "blue",
                "gold",
                "gold",
                "blue",
                "blue",
                "blue",
            ],
            [
                "blue",
                "gold",
                "red",
                "red",
                "gold",
                "red",
                "red",
                "gold",
                "blue",
                "blue",
            ],
            [
                "blue",
                "gold",
                "red",
                "gold",
                "gold",
                "gold",
                "red",
                "gold",
                "blue",
                "blue",
            ],
            [
                "blue",
                "blue",
                "gold",
                "gold",
                "gold",
                "gold",
                "gold",
                "blue",
                "blue",
                "blue",
            ],
            [
                "blue",
                "blue",
                "blue",
                "blue",
                "gold",
                "blue",
                "blue",
                "blue",
                "blue",
                "blue",
            ],
        ]
        self.hero_image = self._create_placeholder_image(hero_colors, pixel_size=8)
        ttk.Label(hero_panel, image=self.hero_image).pack()
        ttk.Label(hero_panel, textvariable=self.hero_health).pack()
        return hero_panel

    def _setup_enemy_panel(self, top_frame: ttk.Frame) -> ttk.Frame:
        enemy_panel = ttk.Frame(top_frame, borderwidth=2, relief="solid", padding=5)
        enemy_panel.grid(row=0, column=1, sticky="nsew", padx=5)
        ttk.Label(enemy_panel, text="Enemy").pack()
        # Platzhalter-Enemy (10x6 Pixel)
        enemy_colors = [
            [
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
            ],
            [
                "black",
                "white",
                "white",
                "black",
                "black",
                "white",
                "white",
                "black",
                "black",
                "black",
            ],
            [
                "black",
                "red",
                "red",
                "black",
                "red",
                "red",
                "red",
                "black",
                "black",
                "black",
            ],
            [
                "black",
                "red",
                "gray",
                "black",
                "black",
                "black",
                "red",
                "black",
                "black",
                "black",
            ],
            [
                "black",
                "black",
                "white",
                "white",
                "black",
                "black",
                "white",
                "white",
                "black",
                "black",
            ],
            [
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
                "black",
            ],
        ]
        self.enemy_image = self._create_placeholder_image(enemy_colors, pixel_size=8)
        ttk.Label(enemy_panel, image=self.enemy_image).pack()
        ttk.Label(enemy_panel, textvariable=self.enemy_health).pack()
        return enemy_panel

    def _setup_buttons(self, frm: ttk.Frame) -> ttk.Frame:
        action_frame = ttk.Frame(frm)
        action_frame.grid(row=1, column=0, pady=10)
        ttk.Button(action_frame, text="Attack", command=self.attack_action).pack(
            side=LEFT, padx=5
        )
        ttk.Button(action_frame, text="Heal", command=self.heal_action).pack(
            side=LEFT, padx=5
        )
        return action_frame

    def _setup_log_frame(self, frm: ttk.Frame) -> ttk.Frame:
        log_frame = ttk.Frame(frm)
        log_frame.grid(row=2, column=0, sticky="ew")
        ttk.Label(log_frame, textvariable=self.combat_log).pack()
        return log_frame

    def setup_screen(self, ui: Tk):
        self._main_frame = self._setup_main_frame(ui)
        self._top_frame = self._setup_top_frame(self._main_frame)
        self._hero_panel = self._setup_hero_panel(self._top_frame)
        self._enemy_panel = self._setup_enemy_panel(self._top_frame)
        self._buttons = self._setup_buttons(self._main_frame)
        self._log_frame = self._setup_log_frame(self._main_frame)

    def attack_action(self):
        self.enemy_health.set("Enemy HP: 80")
        self.combat_log.set("Hero attacks Enemy for 20 damage!")

    def heal_action(self):
        self.hero_health.set("Hero HP: 120")
        self.combat_log.set("Hero heals for 20 HP!")
