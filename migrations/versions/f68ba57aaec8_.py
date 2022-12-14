"""empty message

Revision ID: f68ba57aaec8
Revises: da713194d5f7
Create Date: 2022-10-04 06:10:40.383025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f68ba57aaec8'
down_revision = 'da713194d5f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('complaint', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('complaint', schema=None) as batch_op:
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
