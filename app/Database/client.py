from sqlalchemy.orm import mapped_column, Mapped

from . import Model


class Client(Model):
    __tablename__ = "clients"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    phone: Mapped[str]
    description: Mapped[str | None]
