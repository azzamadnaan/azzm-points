from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.properties import ListProperty, NumericProperty
import random

# حجم نافذة اللعبة والوحدة
GRID_SIZE = 20
CELL_SIZE = 20
WINDOW_WIDTH = GRID_SIZE * CELL_SIZE
WINDOW_HEIGHT = GRID_SIZE * CELL_SIZE

class SnakeGame(Widget):
    snake = ListProperty([])
    food = ListProperty([0, 0])
    direction = ListProperty([1, 0])
    score = NumericProperty(0)
    game_over = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        self.reset_game()
        Clock.schedule_interval(self.update, 0.18)  # سرعة اللعبة
        Window.bind(on_key_down=self.on_key_press)

    def reset_game(self):
        self.snake = [[5, 10], [5, 9], [5, 8]]
        self.direction = [1, 0]
        self.place_food()
        self.score = 0
        self.game_over = False
        self.redraw()

    def place_food(self):
        while True:
            self.food = [
                random.randint(0, GRID_SIZE - 1),
                random.randint(0, GRID_SIZE - 1)
            ]
            if self.food not in self.snake:
                break

    def update(self, dt):
        if self.game_over:
            return

        head = self.snake[0][:]
        new_head = [head[0] + self.direction[0], head[1] + self.direction[1]]

        # التحقق من الاصطدام بالحواف أو بالجسم
        if (new_head in self.snake or
                not (0 <= new_head[0] < GRID_SIZE) or
                not (0 <= new_head[1] < GRID_SIZE)):
            self.game_over = True
            self.redraw()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()

        self.redraw()

    def on_key_press(self, window, key, *args):
        # مفاتيح الأسهم: 273=أعلى، 274=أسفل، 275=يمين، 276=يسار
        if key == 273 and self.direction != [0, 1]:
            self.direction = [0, -1]
        elif key == 274 and self.direction != [0, -1]:
            self.direction = [0, 1]
        elif key == 275 and self.direction != [-1, 0]:
            self.direction = [1, 0]
        elif key == 276 and self.direction != [1, 0]:
            self.direction = [-1, 0]

    def redraw(self):
        self.canvas.clear()
        with self.canvas:
            # خلفية
            Color(0.1, 0.1, 0.1, 1)
            Rectangle(pos=self.pos, size=self.size)

            # الثعبان
            Color(0, 1, 0, 1)
            for segment in self.snake:
                Rectangle(
                    pos=(self.x + segment[0] * CELL_SIZE,
                         self.y + segment[1] * CELL_SIZE),
                    size=(CELL_SIZE - 2, CELL_SIZE - 2)
                )

            # الطعام
            Color(1, 0, 0, 1)
            Rectangle(
                pos=(self.x + self.food[0] * CELL_SIZE,
                     self.y + self.food[1] * CELL_SIZE),
                size=(CELL_SIZE - 2, CELL_SIZE - 2)
            )


class SnakeApp(App):
    def build(self):
        Window.size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        game = SnakeGame()
        Window.bind(on_key_down=game.on_key_press)
        return game


if __name__ == "__main__":
    SnakeApp().run()
