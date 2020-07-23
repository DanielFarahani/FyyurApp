"""empty message

Revision ID: 0813eefd03a2
Revises: 7d1f8cabd1a1
Create Date: 2020-07-03 20:54:51.781659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0813eefd03a2'
down_revision = '7d1f8cabd1a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('start_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Show', 'start_time')
    # ### end Alembic commands ###
