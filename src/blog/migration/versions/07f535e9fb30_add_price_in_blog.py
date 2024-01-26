"""add price in blog

Revision ID: 07f535e9fb30
Revises: 739bd67a3170
Create Date: 2024-01-26 12:51:31.007708

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "07f535e9fb30"
down_revision: Union[str, None] = "739bd67a3170"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        table_name="blogs", column=sa.Column("price", sa.FLOAT), schema="blog"
    )


def downgrade() -> None:
    op.drop_column(
        table_name="blogs", column=sa.Column("price", sa.FLOAT), schema="blog"
    )
