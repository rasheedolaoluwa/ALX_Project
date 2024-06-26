"""Add portfolio models

Revision ID: 70008d374c8c
Revises: ab8f74a258c5
Create Date: 2024-06-26 13:54:02.850053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70008d374c8c'
down_revision = 'ab8f74a258c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('portfolio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('total_value', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('portfolio_investment',
    sa.Column('portfolio_id', sa.Integer(), nullable=False),
    sa.Column('investment_id', sa.String(), nullable=False),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.Column('current_value', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['portfolio_id'], ['portfolio.id'], ),
    sa.PrimaryKeyConstraint('portfolio_id', 'investment_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portfolio_investment')
    op.drop_table('portfolio')
    # ### end Alembic commands ###
