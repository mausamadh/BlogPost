"""add blog service

Revision ID: 739bd67a3170
Revises: 
Create Date: 2024-01-26 12:43:41.781531

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "739bd67a3170"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "blogs",
        sa.Column("id", sa.Integer),
        sa.Column("title", sa.VARCHAR(64), nullable=False),
        sa.Column("content", sa.TEXT, nullable=False),
        sa.Column("author", sa.VARCHAR(32), nullable=False),
        sa.Column("publication_date", sa.DATE, nullable=False),
        sa.Column("tags", sa.VARCHAR(64), nullable=False),
        sa.Column(
            "date_created", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()")
        ),
        sa.Column(
            "date_updated", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()")
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    pass


def downgrade() -> None:
    op.drop_table("blogs")
