"""empty message

Revision ID: 482a06fd5c4e
Revises: 4c26c232e657
Create Date: 2021-04-25 13:26:13.793062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '482a06fd5c4e'
down_revision = '4c26c232e657'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_username', table_name='user')
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.create_index('ix_user_username', 'user', ['username'], unique=True)
    # ### end Alembic commands ###
