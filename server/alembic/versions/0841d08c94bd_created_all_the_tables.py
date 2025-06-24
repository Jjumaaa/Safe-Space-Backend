"""created all the tables

Revision ID: 0841d08c94bd
Revises: 96487d7c0eda
Create Date: 2025-06-24 13:03:19.652903

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0841d08c94bd'
down_revision: Union[str, None] = '96487d7c0eda'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
