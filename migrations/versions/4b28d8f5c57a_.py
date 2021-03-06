"""empty message

Revision ID: 4b28d8f5c57a
Revises: 42b8ae6ef541
Create Date: 2020-07-03 17:14:13.603408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b28d8f5c57a'
down_revision = '42b8ae6ef541'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('artist_id', sa.Integer(), nullable=True))
    op.add_column('show', sa.Column('start_time', sa.String(length=120), nullable=True))
    op.add_column('show', sa.Column('venue_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'show', 'Venue', ['venue_id'], ['id'])
    op.create_foreign_key(None, 'show', 'Artist', ['artist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'show', type_='foreignkey')
    op.drop_constraint(None, 'show', type_='foreignkey')
    op.drop_column('show', 'venue_id')
    op.drop_column('show', 'start_time')
    op.drop_column('show', 'artist_id')
    # ### end Alembic commands ###
