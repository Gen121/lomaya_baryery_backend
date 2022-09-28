from sqlalchemy.ext.asyncio import AsyncSession

from src.api.request_models.photo import PhotoRequest
from src.core.db.models import Photo
from src.core.db.repository import AbstractRepository


class PhotoRepositopry(AbstractRepository):
    """Репозиторий для работы с моделью Photo."""

    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.model = Photo

    async def get(self, obj_id: PhotoRequest.id) -> Photo:
        return await super().get(obj_id)

    async def create(self, obj_data: PhotoRequest) -> Photo:
        return await super().create(obj_data)
