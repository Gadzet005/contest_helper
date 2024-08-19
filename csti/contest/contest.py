from contest.contest_interface import ContestInterface
from contest.task.task import Task


class Contest:
	def __init__(self, id: str, tasksId: list[str]):
		self._tasks: list[Task] = list()
		self._curentTaskLocalId: int = 0
		for taskId in tasksId:
			task = Task(taskId)
			self._tasks.append(task)

		self._id: str = id

		ContestInterface().selectContest(self._id)

	@property
	def tasks(self) -> list[Task]:
		return self._tasks

	def selectTask(self, taskLocalId: int):
		taskLocalId -= 1
		if taskLocalId not in range(0, len(self._tasks)):
			raise 
		self._curentTaskLocalId = taskLocalId

	@property
	def currentTask(self) -> Task:
		return self._tasks[self._curentTaskLocalId]

	@property
	def id(self) -> str:
		return self._id
