# ==========================================================
# IMPORTS
# ==========================================================

import tkinter as tk
from tkinter import ttk


# ==========================================================
# COLORS
# ==========================================================

PINK_LIGHT  = "#ffe6f0"
PINK_MEDIUM = "#ffb3c6"
PINK_DARK   = "#ff80a1"
PINK_ACCENT = "#ff4d75"


# ==========================================================
# MAIN WINDOW
# ==========================================================

class LibraryApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Li-berry")

        self.root.geometry("1350x800")
        self.root.configure(bg=PINK_LIGHT)

        self.setup_style()

        self.build_top_panel()
        self.build_main_area()

    # ======================================================
    # STYLE
    # ======================================================

    def setup_style(self):

        style = ttk.Style()

        style.theme_use("default")

        style.configure(
            "Pink.TButton",
            background=PINK_MEDIUM,
            foreground="black"
        )

        style.configure(
            "Pink.TLabel",
            background=PINK_LIGHT,
            foreground="black"
        )

        style.configure(
            "Pink.TFrame",
            background=PINK_LIGHT
        )

    # ======================================================
    # TOP PANEL
    # ======================================================

    def build_top_panel(self):

        top = tk.Frame(
            self.root,
            bg=PINK_MEDIUM,
            height=40
        )

        top.pack(fill="x")

        btn_add = tk.Button(
            top,
            text="Загрузить новую книгу",
            bg=PINK_ACCENT,
            fg="white",
            relief="flat",
            width=30
        )

        btn_add.pack(
            side="left"
        )

        search_entry = tk.Entry(
            top,
            bd=0,
            width=40
        )

        search_entry.insert(
            0,
            "Поиск..."
        )

        search_entry.pack(
            side="right",
            padx=15,
            pady=8
        )

    # ======================================================
    # BODY
    # ======================================================

    def build_main_area(self):

        body = tk.Frame(
            self.root,
            bg=PINK_LIGHT
        )

        body.pack(
            fill="both",
            expand=True
        )

        self.build_filter_panel(body)
        self.build_books_panel(body)

    # ======================================================
    # FILTER PANEL
    # ======================================================

    def build_filter_panel(self, parent):

        left = tk.LabelFrame(
            parent,
            text="Фильтры",
            bg=PINK_LIGHT,
            fg=PINK_ACCENT,
            width=300
        )

        left.pack(
            side="left",
            fill="y",
            padx=10,
            pady=10
        )

        left.pack_propagate(False)

        # Автор

        tk.Label(
            left,
            text="Автор:",
            bg=PINK_LIGHT
        ).pack(
            anchor="w",
            padx=10,
            pady=(20, 0)
        )

        tk.Entry(left).pack(
            fill="x",
            padx=10
        )

        # Название

        tk.Label(
            left,
            text="Название:",
            bg=PINK_LIGHT
        ).pack(
            anchor="w",
            padx=10,
            pady=(10, 0)
        )

        tk.Entry(left).pack(
            fill="x",
            padx=10
        )

        # Теги

        tk.Label(
            left,
            text="Теги:",
            bg=PINK_LIGHT
        ).pack(
            anchor="w",
            padx=10,
            pady=(10, 0)
        )

        tk.Entry(left).pack(
            fill="x",
            padx=10
        )

        # Рейтинг

        tk.Label(
            left,
            text="Рейтинг:",
            bg=PINK_LIGHT
        ).pack(
            anchor="w",
            padx=10,
            pady=(10, 0)
        )

        scale = tk.Scale(
            left,
            from_=0,
            to=10,
            orient="horizontal",
            bg=PINK_LIGHT,
            troughcolor=PINK_MEDIUM,
            highlightthickness=0
        )

        scale.pack(
            fill="x",
            padx=10
        )

        ttk.Button(
            left,
            text="Применить"
        ).pack(
            pady=20
        )

        # Статистика

        stat = tk.LabelFrame(
            left,
            text="Статистика",
            bg=PINK_LIGHT,
            fg=PINK_ACCENT
        )

        stat.pack(
            fill="x",
            side="bottom",
            padx=5,
            pady=10
        )

        tk.Label(
            stat,
            text="Всего книг: 0",
            bg=PINK_LIGHT
        ).pack(
            anchor="w",
            padx=10,
            pady=3
        )

        tk.Label(
            stat,
            text="Средний рейтинг: 0",
            bg=PINK_LIGHT
        ).pack(
            anchor="w",
            padx=10,
            pady=3
        )

        tk.Label(
            stat,
            text="Любимый автор:",
            bg=PINK_LIGHT
        ).pack(
            anchor="w",
            padx=10,
            pady=3
        )

    # ======================================================
    # BOOKS PANEL
    # ======================================================

    def build_books_panel(self, parent):

        right = tk.Frame(
            parent,
            bg=PINK_LIGHT
        )

        right.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        canvas = tk.Canvas(
            right,
            bg=PINK_LIGHT,
            highlightthickness=0
        )

        scrollbar = ttk.Scrollbar(
            right,
            orient="vertical",
            command=canvas.yview
        )

        cards_frame = tk.Frame(
            canvas,
            bg=PINK_LIGHT
        )

        cards_frame.bind(
            "<Configure>",
            lambda e:
            canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0),
            window=cards_frame,
            anchor="nw"
        )

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # Тестовые карточки

        for i in range(24):

            self.create_book_card(
                cards_frame,
                f"Книга {i+1}",
                i
            )

    # ======================================================
    # CARD
    # ======================================================

    def create_book_card(
            self,
            parent,
            title,
            index
    ):

        card = tk.Frame(
            parent,
            bg="white",
            width=130,
            height=220,
            bd=1,
            relief="solid"
        )

        card.grid(
            row=index // 6,
            column=index % 6,
            padx=15,
            pady=15
        )

        card.grid_propagate(False)

        cover = tk.Label(
            card,
            bg="#efefef",
            width=14,
            height=8
        )

        cover.pack(
            pady=10
        )

        name = tk.Label(
            card,
            text=title,
            bg="white"
        )

        name.pack()

        cover.bind(
            "<Button-1>",
            lambda e:
            self.open_book_window(title)
        )

        card.bind(
            "<Button-1>",
            lambda e:
            self.open_book_window(title)
        )

    # ======================================================
    # BOOK WINDOW
    # ======================================================

    def open_book_window(self, title):

        window = tk.Toplevel(self.root)

        window.title(title)

        window.geometry("1350x800")

        window.configure(
            bg=PINK_LIGHT
        )

        left = tk.Frame(
            window,
            bg=PINK_LIGHT
        )

        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        right = tk.Frame(
            window,
            bg=PINK_LIGHT,
            width=300
        )

        right.pack(
            side="right",
            fill="y",
            padx=20,
            pady=20
        )

        right.pack_propagate(False)

        # Теги

        tk.Label(
            left,
            text="Теги:",
            bg=PINK_LIGHT,
            font=("Segoe UI", 12)
        ).pack(
            anchor="w"
        )

        tk.Text(
            left,
            height=3
        ).pack(
            fill="x",
            pady=5
        )

        # Описание

        tk.Label(
            left,
            text="Описание:",
            bg=PINK_LIGHT,
            font=("Segoe UI", 12)
        ).pack(
            anchor="w",
            pady=(20, 0)
        )

        tk.Text(
            left,
            height=10
        ).pack(
            fill="x"
        )

        # Заметки

        tk.Label(
            left,
            text="Заметки:",
            bg=PINK_LIGHT,
            font=("Segoe UI", 12)
        ).pack(
            anchor="w",
            pady=(20, 0)
        )

        tk.Text(
            left,
            height=12
        ).pack(
            fill="both",
            expand=True
        )

        # Обложка

        cover = tk.Label(
            right,
            bg="#f0f0f0",
            width=25,
            height=15
        )

        cover.pack(
            pady=10
        )

        tk.Label(
            right,
            text=title,
            bg=PINK_LIGHT,
            font=("Segoe UI", 18)
        ).pack(
            pady=15
        )

        tk.Label(
            right,
            text="Автор:",
            bg=PINK_LIGHT
        ).pack(
            anchor="w"
        )

        tk.Entry(
            right
        ).pack(
            fill="x"
        )

        tk.Label(
            right,
            text="Рейтинг:",
            bg=PINK_LIGHT
        ).pack(
            anchor="w",
            pady=(15, 0)
        )

        tk.Scale(
            right,
            from_=0,
            to=10,
            orient="horizontal",
            bg=PINK_LIGHT,
            troughcolor=PINK_MEDIUM,
            highlightthickness=0
        ).pack(
            fill="x"
        )

        ttk.Button(
            right,
            text="Скачать книгу"
        ).pack(
            fill="x",
            pady=10
        )

        ttk.Button(
            right,
            text="Сохранить изменения"
        ).pack(
            fill="x"
        )


# ==========================================================
# START
# ==========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = LibraryApp(root)

    root.mainloop()