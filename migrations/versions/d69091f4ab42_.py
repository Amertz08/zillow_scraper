"""empty message

Revision ID: d69091f4ab42
Revises: 4224bceeb26a
Create Date: 2017-02-03 14:00:27.370841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd69091f4ab42'
down_revision = '4224bceeb26a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('home_listings', sa.Column('baths', sa.Float(), nullable=True))
    op.add_column('home_listings', sa.Column('beds', sa.Integer(), nullable=True))
    op.add_column('home_listings', sa.Column('sq_feet', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('home_listings', 'sq_feet')
    op.drop_column('home_listings', 'beds')
    op.drop_column('home_listings', 'baths')
    # ### end Alembic commands ###