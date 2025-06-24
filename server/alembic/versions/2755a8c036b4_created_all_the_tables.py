"""created all the tables

Revision ID: 2755a8c036b4
Revises: 5298fe908e93
Create Date: 2025-06-24 15:29:22.550852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2755a8c036b4'
down_revision: Union[str, None] = '5298fe908e93'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
