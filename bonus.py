# In this code, the Single Responsibility Principle is satisfied because each class has a single responsibility. 
# Open-Closed Principle is satisfied because the Activity class is open for extension but closed for modification.
# Liskov Substitution Principle is satisfied because the Activity subclasses can be used interchangeably.
# Interface Segregation Principle is satisfied because the Activity subclasses implement only the methods they need.
# Dependency Inversion Principle is satisfied because the ActivityMonitor class depends on abstractions, not on concrete classes.



from abc import ABC, abstractmethod

# Single Responsibility Principle: The User class is responsible for managing user information.
class User:
    def __init(self, name, age):
        self.name = name
        self.age = age

# Open-Closed Principle: The Activity class is open for extension (you can create new subclasses) but closed for modification.
# Liskov Substitution Principle: The Activity subclasses can be used interchangeably because they all adhere to the same interface.
class DistanceActivity(ABC):
    @abstractmethod
    def update_distance(self, data):
        print(f"Updating distance with {data}...")

class TimeActivity(ABC):
    @abstractmethod
    def update_time(self, data):
        print(f"Updating time with {data}...")

class Walking(DistanceActivity):
    def update_distance(self, data):
        print(f"Walking {data} steps...")

class Running(DistanceActivity):
    def update_distance(self, data):
        print(f"Running {data} steps...")

class Swimming(TimeActivity):
    def update_time(self, data):
        print(f"Swimming for {data} minutes...")

# Single Responsibility Principle: The ActivityMonitor class is responsible for managing activities.
# Dependency Inversion Principle: The ActivityMonitor class depends on abstractions (the Activity and Display classes), not on concrete classes.
class ActivityMonitor: 
    def __init__(self, user, activities, display):
        self.user = user
        self.activities = []
        self.display = display
    
    def add_activity(self, activity):
        self.activity = activity
        self.notify_display()
        print(f"{activity} added to list of activities")

    def notify_display(self):
        self.display.update(self.activity)

# Single Responsibility Principle: The DataStorage class is responsible for managing data storage.
class DataStorage: 
    def __init__(self, user):
        self.user = user
        self.data = []

    def add_data(self, data):
        self.data.append(data)
        print(f"{data} added to list of data")

# Single Responsibility Principle: The Display class is responsible for managing the display.
class Display: 
    def __init__(self, user):
        self.user = user

    def update(self, activity):
        print(f"Updating display with {activity}...")

def main():
    user = User("John", 25)
    data_storage = DataStorage(user)

    display = Display(user)

    activity_monitor = ActivityMonitor(user, [], display)

    walking = Walking()
    activity_monitor.add_activity(walking)

if __name__ == "__main__":
    main()