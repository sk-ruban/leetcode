from sortedcontainers import SortedList

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.list = SortedList()
        self.tasks = {}

        for u, t, p in tasks:
            self.add(u, t, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.list.add((priority, taskId, userId))
        self.tasks[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        oldPriority, userId = self.tasks[taskId]
        self.list.remove((oldPriority, taskId, userId))
        self.list.add((newPriority, taskId, userId))
        self.tasks[taskId] = (newPriority, userId)

    def rmv(self, taskId: int) -> None:
        priority, userId = self.tasks[taskId]
        self.list.remove((priority, taskId, userId))
        del self.tasks[taskId]

    def execTop(self) -> int:
        if len(self.list) == 0: return -1
        priority, taskId, userId = self.list.pop()
        del self.tasks[taskId]

        return userId
        
# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()