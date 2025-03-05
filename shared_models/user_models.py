import uuid
import uuid_utils
from sqlalchemy import Index, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from database import Base, str_not_null, str_null, created_at


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid_utils.uuid7)
    email: Mapped[str_not_null] = mapped_column(unique=True)
    hashed_password: Mapped[str_not_null]
    name: Mapped[str_null]
    created_at: Mapped[created_at]
    profile_photo_url: Mapped[str_null] = mapped_column(default='/images/default.jpg')

    def __str__(self):
        return f'{self.email}'
