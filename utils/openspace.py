from table import Table

class Openspace:
    ...

    def __init__(self, number_of_tables: int = 6) -> None:
        ...
        self.number_of_tables: int = number_of_tables
        self.tables: list[Table] = [Table for _ in range(self.number_of_tables)]

    def organize(self, names: list) -> None:
        ...

    def display(self) -> None:
        ...

    def store(self, filename: str) -> None:
        ...