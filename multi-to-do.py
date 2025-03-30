##################
# Task - class
##################
class Task:
    def __init__(self, text: str):
        """ Constructor """
        self.__text: str = text
        self.completed: bool = False

    @property
    def task(self) -> str:
        """ Method to get the value of text """
        return self.__text

    @task.setter
    def task(self, text: str):
        """ Method to change the value of text """
        if len(text) > 0:
            self.__text = text
        else:
            raise ValueError("The task can't be empty")

    def __repr__(self) -> str:
        """ Method to represent object """
        return f'{self.__text} [Not done]' if not self.completed else f'{self.__text} [Done]'


##################
# To-do - class
##################
class ToDoList:
    def __init__(self, name: str):
        """ Constructor """
        self.__name = name if len(name) > 0 else 'Unknown'
        self.__tasks: list[Task] = []

    @property
    def name(self) -> str:
        return self.__name

    def addTask(self, task: Task) -> None:
        """ Method to add new task """
        self.__tasks.append(task)

    def removeTask(self, id: int) -> None:
        """ Method to remove task """
        self.__tasks.remove(self.__tasks[id])

    def toggleDone(self, id: int) -> None:
        """ Method to toggle a task as done
         If it's not done then mark it as done
         If it's already done then mark it as not done
         """
        self.__tasks[id].completed = not self.__tasks[id].completed

    def renameList(self, name: str) -> None:
        """ Method to rename the list """
        if len(name) > 0:
            self.__name = name
        else:
            raise ValueError(f"Can't accept empty name")

    def __repr__(self) -> str:
        """ Method to represent the list """
        s: str = f'{self.__name}\n\n'
        for index in range(len(self.__tasks)):
            s += f'{index + 1}. {self.__tasks[index].__repr__()}\n'
        return s


##################
# Manager - class
##################
class ToDoManager:
    def __init__(self):
        """ Constructor """
        self.__todo_lists: list[ToDoList] = []      # To-do Lists
        self.__index: int = -1                      # Indicate current active to-do list

    @property
    def index(self) -> int:
        """ Get index of active to-do list """
        return self.__index

    @index.setter
    def index(self, value: int) -> None:
        """ Set index for active to-do list """
        if 0 <= value < len(self.__todo_lists):
            self.__index = value

    def addList(self, todo: ToDoList) -> None:
        """ Method to add a new to-do list """
        self.__todo_lists.append(todo)


# Debug
if __name__ == '__main__':
    pass