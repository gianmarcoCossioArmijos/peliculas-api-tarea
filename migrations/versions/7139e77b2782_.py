"""empty message

Revision ID: 7139e77b2782
Revises: 
Create Date: 2023-10-29 02:26:04.672813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7139e77b2782'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('peliculas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('precio', sa.Double(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('foto', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('peliculas')
    # ### end Alembic commands ###
