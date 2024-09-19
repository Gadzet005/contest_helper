import os
import typing as t
from enum import Enum

from csti.data_storage import Group, StorageTemplate
from csti.data_storage.file import FileStorage
from csti.data_storage.file.field import *


class IntStorage(FileStorage):
    template = StorageTemplate(
        [
            IntField("number"),
            IntField("default_number", default=1000),
            IntField("invalid_number"),
        ]
    )


class StringStorage(FileStorage):
    template = StorageTemplate(
        [
            StringField("name"),
            StringField("default_name", default="Bob"),
        ]
    )


class BoolStorage(FileStorage):
    template = StorageTemplate(
        [
            BoolField("is_active"),
            BoolField("default_active", default=True),
            BoolField("invalid_flag"),
        ]
    )


class Color(Enum):
    red = 1
    green = 2
    blue = 3


class EnumStorage(FileStorage):
    template = StorageTemplate(
        [
            EnumField("color", enumType=Color),
            EnumField("default_color", enumType=Color, default=Color.red),
            EnumField("invalid_color", enumType=Color),
        ]
    )


class ListStorage(FileStorage):
    template = StorageTemplate(
        [
            ListField("numbers", IntField(), separator=" "),
            ListField("default_numbers", IntField(), default=[1, 2, 3]),
            ListField("invalid_numbers", IntField()),
            ListField("strings", StringField()),
            ListField("enums", EnumField(enumType=Color)),
            ListField(
                "default_enums",
                EnumField(enumType=Color),
                default=[Color.red, Color.blue],
            ),
            ListField(
                "matrix", ListField(item=IntField(), separator=" "), separator="\n"
            ),
            ListField(
                "default_matrix",
                ListField(item=IntField()),
                default=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                separator="\n",
            ),
            ListField("invalid_matrix", ListField(item=IntField(), separator="\n")),
        ]
    )


class GroupStorage(FileStorage):
    template = StorageTemplate(
        [
            IntField("num"),
            Group(
                "group1",
                [IntField("invalid_num"), IntField("num"), StringField("name")],
            ),
            Group(
                "group2",
                [
                    Group("group1", [IntField("num"), BoolField("flag")]),
                    Group("group2", [IntField("num"), StringField("name")]),
                ],
            ),
        ]
    )
