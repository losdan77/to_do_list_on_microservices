import uuid
import uuid_utils
from sqlalchemy import Index, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from database import Base, intpk, str_not_null, str_null, created_at


class Tasks(Base):
    __tablename__ = 'tasks'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid_utils.uuid7)
    task: Mapped[str_null]
    task_importance: Mapped[int] = mapped_column(nullable=True) 
    created_at: Mapped[created_at]
    id_user: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True),
                                               ForeignKey('users.id'), 
                                               nullable=False,)

    def __str__(self):
        return f'{self.task}'
