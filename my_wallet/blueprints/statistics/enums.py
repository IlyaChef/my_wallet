from enum import Enum


class ChoicebleEnumMixin:
    @classmethod
    def choices(cls) -> list[tuple[str, str]]:
        return [(i.value, i.value.lower().replace("_", " ").capitalize()) for i in cls]


class StatReportType(ChoicebleEnumMixin, Enum):
    BIGGEST_EXPENSES = "BIGGEST_EXPENSES"
    EXPENSES_BY_WEEKDAY = "EXPENSES_BY_WEEKDAY"
    EXPENSES_BY_WEEK = "EXPENSES_BY_WEEK"
    EXPENSES_BY_TYPE = "EXPENSES_BY_TYPE"
    WEEKLY_BALANCE = "WEEKLY_BALANCE"


class ReportDisplayFormat(ChoicebleEnumMixin, Enum):
    HTML = "HTML"
    XLSX = "XLSX"
    PDF = "PDF"
