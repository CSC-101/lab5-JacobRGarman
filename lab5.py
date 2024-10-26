import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3: time_add function
def time_add(time1: data.Time, time2: data.Time) -> data.Time:
    total_seconds = time1.second + time2.second
    extra_minute, second = divmod(total_seconds, 60)

    total_minutes = time1.minute + time2.minute + extra_minute
    extra_hour, minute = divmod(total_minutes, 60)

    hour = time1.hour + time2.hour + extra_hour

    return data.Time(hour, minute, second)


# Part 4: is_descending function
def is_descending(numbers: list[float]) -> bool:
    for i in range(len(numbers) - 1):
        if numbers[i] <= numbers[i + 1]:  # If not strictly descending
            return False
    return True


# Part 5: largest_between function
def largest_between(nums: list[int], lower: int, upper: int) -> int | None:
    # Adjust bounds to be within valid indexes
    lower = max(0, lower)
    upper = min(len(nums) - 1, upper)

    if lower > upper:
        return None

    max_index = lower
    for i in range(lower, upper + 1):
        if nums[i] > nums[max_index]:
            max_index = i
    return max_index


# Part 6: furthest_from_origin function
def furthest_from_origin(points: list[data.Point]) -> int | None:
    if not points:
        return None

    max_distance = 0
    furthest_index = 0
    for i, point in enumerate(points):
        distance = (point.x ** 2 + point.y ** 2) ** 0.5  # Calculate Euclidean distance
        if distance > max_distance:
            max_distance = distance
            furthest_index = i
    return furthest_index