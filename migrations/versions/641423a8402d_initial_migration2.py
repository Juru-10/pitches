"""Initial Migration2

Revision ID: 641423a8402d
Revises: 2a7fa3346b91
Create Date: 2019-03-02 20:19:17.914620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '641423a8402d'
down_revision = '2a7fa3346b91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'category')
    # ### end Alembic commands ###
