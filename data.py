import math
from typing import Any

# Representation of time as hours, minutes, and seconds
class Time:
    # Initialize a new Time object.
    # input: hour as an int
    # input: minute as an int
    # input: second as an int
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    # Compare the Time object with another value to determine equality.
    # input: Another value to compare to the Time
    # output: boolean indicating equality
    def __eq__(self, other: Any) -> bool:
        # Check that `other` is a Time instance and that its attributes match
        return (
            isinstance(other, Time) and
            self.hour == other.hour and
            self.minute == other.minute and
            self.second == other.second
        )

    # Provide a developer-friendly string representation of the object.
    # output: string representation of the Time instance
    def __repr__(self) -> str:
        return f"Time({self.hour}, {self.minute}, {self.second})"


# Representation of a two-dimensional point.
class Point:
    # Initialize a new Point object.
    # input: x-coordinate as a float
    # input: y-coordinate as a float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Provide a developer-friendly string representation of the object.
    # output: string representation
    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)

    # Compare the Point object with another value to determine equality.
    # input: Another value to compare to the Point
    # output: boolean indicating equality
    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, Point) and
            math.isclose(self.x, other.x) and
            math.isclose(self.y, other.y)
        )
