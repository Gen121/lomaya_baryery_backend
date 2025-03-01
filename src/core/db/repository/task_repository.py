from uuid import UUID

from fastapi import Depends
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import get_session
from src.core.db.DTO_models import TasksAnalyticReportDto
from src.core.db.models import Report, Task
from src.core.db.repository import AbstractRepository


class TaskRepository(AbstractRepository):
    """Репозиторий для работы с моделью Task."""

    def __init__(self, session: AsyncSession = Depends(get_session)) -> None:
        super().__init__(session, Task)

    async def get_task_ids_list(self) -> list[UUID]:
        """Список task_id неархивированных заданий."""
        task_ids = await self._session.execute(select(Task.id).where(Task.is_archived.is_(False)))
        return task_ids.scalars().all()

    async def get_tasks_statistics_report(self) -> tuple[TasksAnalyticReportDto]:
        """Отчёт по задачам со всех смен.

        Содержит:
        - список всех задач;
        - общее количество принятых/отклонённых/не предоставленных отчётов по каждому заданию.
        """
        stmt = (
            select(
                Task.sequence_number,
                Task.title,
                func.count().filter(Report.status == Report.Status.APPROVED).label(Report.Status.APPROVED),
                func.count().filter(Report.status == Report.Status.DECLINED).label(Report.Status.DECLINED),
                func.count().filter(Report.status == Report.Status.SKIPPED).label(Report.Status.SKIPPED),
            )
            .join(Task.reports)
            .group_by(Task.id, Task.sequence_number)
            .order_by(Task.sequence_number)
        )
        tasks = await self._session.execute(stmt)
        return tuple(TasksAnalyticReportDto(*task) for task in tasks.all())
