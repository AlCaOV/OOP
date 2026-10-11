class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]
    ANGLES = {"квадрат": 4, "прямокутник": 4, "трикутник": 3}

    def __init__(self, figure_type: str, length: int) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert figure_type in self.FIGURES, "Невідомий тип фігури"
        self.type = figure_type
        self.length = length

    @property
    def get_figure_type(self) -> str:
        return self.type

    @property
    def get_figure_length(self) -> int:
        return self.length

    @property
    def get_angles(self) -> int:
        return self.ANGLES[self.type]


if __name__ == "__main__":
    a = Figure("квадрат", 5)
    b = Figure("трикутник", 3)
    print(a.get_figure_type, a.get_figure_length, a.get_angles)
    print(b.get_figure_type, b.get_figure_length, b.get_angles)
