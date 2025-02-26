from sqlalchemy import Index, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, intpk, str_not_null, str_null, created_at


class Users(Base):
    __tablename__ = 'users'

    id = intpk
    email: Mapped[str_not_null] = mapped_column(unique=True)
    hashed_password: Mapped[str_not_null]
    created_at: Mapped[created_at]
    first_name: Mapped[str_null]
    last_name: Mapped[str_null]
    about: Mapped[str_null]
    profile_photo_url: Mapped[str_null] = mapped_column(default='/images/default.jpg')
    id_city: Mapped[int] = mapped_column(ForeignKey('city.id'), nullable=True)

    city: Mapped[list['City']] = relationship(back_populates='users')

    __table_args__ = (
        Index('id_city_index', 'id_city'),
    )

    def __str__(self):
        return f'{self.email}'


class City(Base):
    __tablename__ = 'city'

    id = intpk
    name = Mapped[str_null]

    users: Mapped[list['Users']] = relationship(back_populates='city')

    def __str__(self):
        return f'{self.name}'