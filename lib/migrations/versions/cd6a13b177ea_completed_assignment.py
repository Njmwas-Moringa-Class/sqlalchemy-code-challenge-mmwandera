"""Completed assignment

Revision ID: cd6a13b177ea
Revises: 54da28e85ce8
Create Date: 2024-02-13 22:44:22.619011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd6a13b177ea'
down_revision = '54da28e85ce8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant_users',
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('restaurant_id', 'customer_id')
    )
    op.add_column('reviews', sa.Column('score', sa.Integer(), nullable=True))
    op.add_column('reviews', sa.Column('comment', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reviews', 'comment')
    op.drop_column('reviews', 'score')
    op.drop_table('restaurant_users')
    # ### end Alembic commands ###
