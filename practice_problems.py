"""
Problem 1: Duplicate Tracker
You are given a collection of product IDs. Some IDs may appear more than once.

Write a function that returns True if any duplicates are found, and False otherwise.
"""

def has_duplicates(product_ids):
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)

    return False


# I used a set because I only need to know if I have already seen a product ID before.
# Checking and adding values to a set are O(1) on average, so going through the full
# list is O(n).


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support
removing tasks from the front.
"""

from collections import deque


class TaskQueue:

    def __init__(self):
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if len(self.tasks) == 0:
            return None

        return self.tasks.popleft()


# I used a queue because the first task added should also be the first task removed.
# A deque lets me add to the end and remove from the front in O(1) time.


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to
return the number of unique values seen so far.
"""

class UniqueTracker:

    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)

print(has_duplicates([10, 20, 30, 20, 40]))
print(has_duplicates([1, 2, 3, 4, 5]))

task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
print(task_queue.remove_oldest_task())
print(task_queue.remove_oldest_task())
print(task_queue.remove_oldest_task())

tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
print(tracker.get_unique_count())

# I used a set because sets automatically keep only unique values even if the same
# value is added more than once. Adding a value is O(1) on average and getting the
# number of values with len() is O(1).