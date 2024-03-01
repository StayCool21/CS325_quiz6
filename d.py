# Imagine you're developing a web application and need a robust logging system.
# Currently, your code directly utilizes a specific logging library like logging, loguru,
# Google_auth, throughout your application.
# Question:
# WAP to adhere to the Dependency Inversion Principle (DIP) in regards to logging.
# Focus on the following aspects and Name your program d.py.:
# ● Tight coupling with a specific logging library: Can you decouple your
# application logic from the chosen library, making it easier to switch or extend
# logging capabilities later?
# ● Testing concerns: How can DIP improve the testability of your application's
# logging functionality?
# ● Enhancing flexibility: Can you introduce mechanisms to dynamically configure
# logging behavior based on different environments or user preferences?

from abc import ABC, abstractmethod

class AbstractLogger(ABC):
    @abstractmethod
    def log(self, message: str, env: str) -> None:
        print("Logging message: ", message)
        print("Environment: ", env)

    # error handling, log levels, etc. can be added here
    @abstractmethod
    def error(self, message: str) -> None:
        print("Error message: ", message)

    # ... we could also add warnings too
    @abstractmethod
    def warning(self, message: str) -> None:
        print("Warning message: ", message)

    @abstractmethod
    def debug(self, message: str) -> None:
        print("Debug message: ", message)


# now we add the application class that could be extended to use any logging library
# we would most likely need to include different logging libraries in the future
class Application:
    def __init__(self, logger: AbstractLogger) -> None:
        self.logger = logger

    def do_something_cool(self) -> None:
        # debug/trace messages
        self.logger.log("Doing something cool...")
        self.logger.debug("This is a debug message")

    def flag(self) -> None:
        # warning messages
        self.logger.warning("Warning message on line 100")

    def choose_env(self, env: str) -> None:
        supported_envs = ["logging", "loguru", "google_auth"]
        # error messages
        if env not in supported_envs:
            self.logger.error("Invalid environment specified")
        else:
            self.logger.log(f"Switching to {env} environment")
       

    
    