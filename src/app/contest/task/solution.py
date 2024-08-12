from dataclasses import dataclass
from enum import Enum


class SolutionStatus(Enum):
	accepted_for_review = "Принято на проверку"
	wrang_answer = "Неправильный ответ"
	compilation_error = "Ошибка компиляции"
	execution_error = "Ошибка выполнения"
	bad_output_format = "Неправильный формат вывода"
	unclassified_error = "Не классифицированная ошибка"
	time_limit = "Превышено максимальное время работы"

	@classmethod
	def _missing_(cls, value):
		return cls.unclassified_error


@dataclass
class Solution:
	id_: int
	status: SolutionStatus
	testsPassed: int

