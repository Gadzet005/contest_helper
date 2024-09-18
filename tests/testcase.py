import typing as t
import os
import unittest
import shutil


class TestCase(unittest.TestCase):
    @staticmethod
    def dir() -> str:
        """Путь до коневой папки с тестами."""
        return os.path.dirname(os.path.realpath(__file__))

    @classmethod
    def getAbsolutePath(cls, relativePath: str) -> str:
        return os.path.join(cls.dir(), relativePath)


class FileTestCase(TestCase):
    """Класс для безопасного тестирования работы с файлами."""

    # Может быть переопределено в наследниках.
    # Директория с файлами.
    DATA_DIR = "data"
    # Директория, в которую будут копироваться файлы из DATA_DIR.
    # После завершения тестов эта директория будет удалена вместе с создержимым.
    TEST_DIR = "test"

    @classmethod
    def setUpClass(cls):
        os.makedirs(cls.getTestDir(), exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.getTestDir()):
            shutil.rmtree(cls.getTestDir())

    @classmethod
    def getDataDir(cls, relPath: t.Optional[str] = None) -> str:
        path = cls.DATA_DIR
        if relPath:
            path = os.path.join(path, relPath)
        return cls.getAbsolutePath(path)

    @classmethod
    def getTestDir(cls, relPath: t.Optional[str] = None) -> str:
        path = cls.TEST_DIR
        if relPath:
            path = os.path.join(path, relPath)
        return cls.getAbsolutePath(path)

    @classmethod
    def useData(
        cls,
        srcRelPath: str,
        destRelPath: t.Optional[str] = None,
        isDir: bool = False
    ) -> str:
        """
        Копирование файла/директории из `DATA_DIR` в `TEST_DIR`.
        Возвращает путь до скопированного файла/директории.
        """

        if destRelPath is None:
            destRelPath = srcRelPath

        srcPath = os.path.join(cls.getDataDir(), srcRelPath)
        destPath = os.path.join(cls.getTestDir(), destRelPath)

        os.makedirs(os.path.dirname(destPath), exist_ok=True)
        if isDir:
            shutil.copytree(srcPath, destPath, dirs_exist_ok=True)
        else:
            shutil.copy(srcPath, destPath)

        return destPath

    @classmethod
    def copyAll(cls):
        """Копирование всех файлов из `DATA_DIR` в `TEST_DIR`."""
        shutil.copytree(cls.getDataDir(), cls.getTestDir(), dirs_exist_ok=True)
