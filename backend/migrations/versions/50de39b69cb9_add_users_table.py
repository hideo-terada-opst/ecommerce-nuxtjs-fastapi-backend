"""add users table

Revision ID: 50de39b69cb9
Revises: 0508f9ca0879
Create Date: 2021-05-15 12:48:43.971448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50de39b69cb9'
down_revision = '0508f9ca0879'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('username', sa.Unicode(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('email_verified', sa.Boolean(), server_default='True', nullable=True),
    sa.Column('salt', sa.Unicode(), nullable=False),
    sa.Column('password', sa.Unicode(), nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='True', nullable=False),
    sa.Column('is_superuser', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
