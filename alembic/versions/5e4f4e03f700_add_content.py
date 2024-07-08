"""add content

Revision ID: 5e4f4e03f700
Revises: d38124920313
Create Date: 2024-07-06 11:23:40.361662

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e4f4e03f700'
down_revision: Union[str, None] = 'd38124920313'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(45),nullable=False))


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
