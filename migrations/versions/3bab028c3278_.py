"""empty message

Revision ID: 3bab028c3278
Revises: 5f79f4a8c61b
Create Date: 2022-11-04 06:44:09.849890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bab028c3278'
down_revision = '5f79f4a8c61b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('complaint', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.drop_column('buyer_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('complaint', schema=None) as batch_op:
        batch_op.add_column(sa.Column('buyer_id', sa.INTEGER(), nullable=True))
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
