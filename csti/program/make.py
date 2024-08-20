from __future__ import annotations

import os
from enum import Enum
from pathlib import Path

from csti.consts import Language
from csti.program.exceptions import UnexpectedLanguage

CUR_DIR = Path(__file__).parent.resolve()
MAKE_DIR = CUR_DIR / "make"
FORMAT_CONFIGS_DIR = CUR_DIR / "format_configs"


class MakeTarget(Enum):
	compile = "compile"
	run = "run"
	clear = "clear"
	format = "format"


class LangInfo:
	def __init__(
			self, canBeCompiled: bool, canBeFormatted: bool, 
			makefile: str|None, formatConfig: str|None
		):
		self._canBeCompiled = canBeCompiled
		self._canBeFormatted = canBeFormatted
		self._makefile = makefile
		self._formatConfig = formatConfig

	@staticmethod
	def fromLang(lang: Language) -> LangInfo:
		match lang:
			case Language.c:
				return LangInfo(True, True, "c/makefile", "cformat.yaml")
			case Language.cpp:
				return LangInfo(True, True, "cpp/makefile", "cformat.yaml")
			case Language.asm:
				return LangInfo(True, False, "asm/makefile", None)
			case _:
				raise UnexpectedLanguage(lang)
	
	@property
	def canBeCompiled(self) -> bool:
		return self._canBeCompiled
	
	@property
	def canBeFormatted(self) -> bool:
		return self._canBeFormatted
	
	@property
	def makefile(self) -> str|None:
		return os.path.join(MAKE_DIR, self._makefile)
	
	@property
	def formatConfig(self) -> str|None:
		return os.path.join(FORMAT_CONFIGS_DIR, self._formatConfig)