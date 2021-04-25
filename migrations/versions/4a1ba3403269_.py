"""empty message

Revision ID: 4a1ba3403269
Revises: aa91817de394
Create Date: 2021-04-25 12:48:04.063511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a1ba3403269'
down_revision = 'aa91817de394'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('source', sa.String(length=128), nullable=True),
    sa.Column('discord_id', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('discord_id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('eggs', sa.Integer(), nullable=True),
    sa.Column('coins', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inventory_coins'), 'inventory', ['coins'], unique=False)
    op.create_index(op.f('ix_inventory_eggs'), 'inventory', ['eggs'], unique=False)
    op.create_table('pet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('species', sa.String(length=128), nullable=True),
    sa.Column('color', sa.String(length=128), nullable=True),
    sa.Column('closeness', sa.Integer(), nullable=True),
    sa.Column('size', sa.String(length=64), nullable=True),
    sa.Column('ability_type', sa.String(length=128), nullable=True),
    sa.Column('rarity', sa.String(length=128), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pet')
    op.drop_index(op.f('ix_inventory_eggs'), table_name='inventory')
    op.drop_index(op.f('ix_inventory_coins'), table_name='inventory')
    op.drop_table('inventory')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###