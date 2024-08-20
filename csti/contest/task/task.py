from csti.contest.contest_interface import ContestInterface
from csti.contest.parser.task_parser import TaskParser
from csti.contest.task.solution import Solution


# TODO: Добавить кеширование и проверку возвращаемого значения в функциях.
class Task:
	def __init__(self, id_: str) -> None:
		self._id: str = id_

	@property
	def id(self) -> str:
		return self._id

	def getInfo(self) -> list:
		return TaskParser.getInfo(ContestInterface().requestTask(self._id))

	def getName(self) -> str:	
		return TaskParser.getName(ContestInterface().requestTask(self._id))

	def getCondition(self) -> str:
		return TaskParser.getCondition(ContestInterface().requestTask(self._id))

	def getTests(self) -> list[tuple[str, str]]:
		return TaskParser.getTests(ContestInterface().requestTask(self._id))

	def getSolution(self) -> Solution|None:
		return TaskParser.getLastSolution(ContestInterface().requestTask(self._id))

	def sendSolution(self, file: str):
		return ContestInterface().sendTask(self._id, file)
