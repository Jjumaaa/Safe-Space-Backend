"""created all the tables

Revision ID: 7d669facb9da
Revises: 0841d08c94bd
Create Date: 2025-06-24 13:13:28.868116

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d669facb9da'
down_revision: Union[str, None] = '0841d08c94bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
