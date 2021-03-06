"""empty message

Revision ID: 90fa1cabafcb
Revises: f7d6596b6ebd
Create Date: 2020-07-01 16:31:57.858195

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '90fa1cabafcb'
down_revision = 'f7d6596b6ebd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genres', postgresql.ARRAY(sa.INTEGER()), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
