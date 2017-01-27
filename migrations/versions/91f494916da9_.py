"""empty message

Revision ID: 91f494916da9
Revises: 
Create Date: 2017-01-27 15:47:43.863374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91f494916da9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('home_listings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('zid', sa.Integer(), nullable=True),
    sa.Column('entry_date', sa.Integer(), nullable=True),
    sa.Column('street_address', sa.String(length=255), nullable=False),
    sa.Column('city', sa.String(length=255), nullable=False),
    sa.Column('state', sa.String(length=255), nullable=False),
    sa.Column('zip_code', sa.String(length=10), nullable=False),
    sa.Column('latitude', sa.Integer(), nullable=True),
    sa.Column('longitude', sa.Integer(), nullable=True),
    sa.Column('pgapt', sa.String(length=25), nullable=True),
    sa.Column('sgapt', sa.String(length=25), nullable=True),
    sa.Column('link', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('home_listings')
    # ### end Alembic commands ###
