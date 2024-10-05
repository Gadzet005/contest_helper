from csti.contest import Contest, Task
from csti.contest.env.exceptions import EnvStorageError
from csti.contest.manager import ContestManager
from csti.contest.systems.supported import SupportedContestSystem
from csti.storage import Group, StorageTemplate
from csti.storage.exceptions import FieldIsEmpty
from csti.storage.file import FileStorage
from csti.storage.file.field import EnumField, IntField, ListField


class EnvDataStorage(FileStorage):
    template = StorageTemplate(
        [
            Group(
                "contest",
                [
                    IntField("id"),
                    IntField("currentTaskId"),
                    ListField("taskIds", item=IntField(), default=[]),
                ],
            ),
            EnumField("contest-system", enumType=SupportedContestSystem),
        ]
    )

    def loadContest(self, manager: ContestManager) -> Contest:
        try:
            id = self.get("contest", "id")
            return manager.getContest(id)
        except FieldIsEmpty:
            raise EnvStorageError("Контест не выбран.")

    def loadCurrentTask(self, manager: ContestManager) -> Task:
        try:
            contest = self.loadContest(manager)
            taskId = self.get("contest", "currentTaskId")
            return contest.getTask(taskId)
        except FieldIsEmpty:
            raise EnvStorageError("Задача не выбрана.")

    def loadTasks(self, manager: ContestManager) -> list[Task]:
        try:
            contest = self.loadContest(manager)
            ids = self.get("contest", "taskIds")
            return [contest.getTask(taskId) for taskId in ids]
        except EnvStorageError:
            return []