"""empty message

Revision ID: 4c26c232e657
Revises: 4a1ba3403269
Create Date: 2021-04-25 12:49:45.518927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c26c232e657'
down_revision = '4a1ba3403269'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventory', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.drop_constraint('inventory_user_id_fkey', 'inventory', type_='foreignkey')
    op.create_foreign_key(None, 'inventory', 'user', ['owner_id'], ['id'])
    op.drop_column('inventory', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventory', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'inventory', type_='foreignkey')
    op.create_foreign_key('inventory_user_id_fkey', 'inventory', 'user', ['user_id'], ['id'])
    op.drop_column('inventory', 'owner_id')
    # ### end Alembic commands ###
