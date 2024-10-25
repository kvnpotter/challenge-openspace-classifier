class Seat:
    """
    Class representing a seat.
    """
    def __init__(self) -> None:
        """
        Create a seat with it's attributes, occupancy status and occupant, both empty.
        """
        self.free = True
        self.occupant = "None"
    
    def set_occupant(self, name: str) -> None:
        """
        Set seat occupancy status and occupant.

        :param name: str: A string containing occupant name.
        """
        self.occupant = name
        self.free = False
    
    def remove_occupant(self) -> None:
        """
        Remove seat occupant, reset occupancy status attributes.
        """
        self.occupant = "None"
        self.free = True

    def __str__(self) -> str:
        if self.free:
            status = "empty"
        else:
            status = "occupied"
        return f"This is a chair.\nIt is currently {status}.\nIt's occupant is {self.occupant}."

class Table:
    """
    Class representing a table.
    """
    def __init__(self, capacity: int = 4) -> None:
        """
        Create a table with a number of chairs.

        :param capacity: (int, optional): Number of seats at the table. Defaults to 4.
        """
        self.capacity = capacity
        self.seats = [Seat() for _ in range(self.capacity)]

    def has_free_spot(self) -> bool:
        """
        Verify if table has free seats.

        :return: bool: A boolean, true if there are free seats at the table.
        """
        result = 0
        for seat in self.seats:
            result += seat.free
        return bool(result)
    
    def assign_seat(self, name: str) -> None:
        """
        Assign a person to a seat

        :param name: str: Name of the person to assign.

        """
        if self.has_free_spot():
            for seat in self.seats:
                if seat.free:
                    seat.set_occupant(name)
                    break
                else:
                    continue
        else:
            print("table full")
    
    def left_capacity(self) -> int:
        """
        Verify number of remaining free seats at the table.

        :return: int: Number of free seats.
        """
        taken = 0
        for seat in self.seats:
            taken += not(seat.free)
        return self.capacity - taken 
    
    def __str__(self) -> str:
        occupants = ""
        for seat in self.seats:
            if seat.occupant != "None":
                occupants += f"{seat.occupant}\n"
        return f"This is a table.\nThere are {self.left_capacity()} free seats.\nThe occupants are:\n{occupants}"
