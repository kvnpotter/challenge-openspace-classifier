class Seat:
    def __init__(self) -> None:
        self.free = True
        self.occupant = "None"
    
    def set_occupant(self, name: str) -> None:
        self.occupant = name
        self.free = False
    
    def remove_occupant(self) -> None:
        self.occupant = "None"
        self.free = True

    def __str__(self) -> str:
        if self.free:
            status = "empty"
        else:
            status = "occupied"
        return f"This is a chair.\nIt is currently {status}.\nIt's occupant is {self.occupant}."

class Table:
    def __init__(self, capacity: int = 4) -> None:
        self.capacity = capacity
        self.seats = [Seat() for _ in range(self.capacity)]

    def has_free_spot(self) -> bool:
        result = 0
        for seat in self.seats:
            result += seat.free
        return bool(result)
    
    def assign_seat(self, name: str) -> None:
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
