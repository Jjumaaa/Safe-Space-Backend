"""created all the tables

Revision ID: 5298fe908e93
Revises: 7d13558d708f
Create Date: 2025-06-24 15:28:26.734616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5298fe908e93'
down_revision: Union[str, None] = '7d13558d708f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
