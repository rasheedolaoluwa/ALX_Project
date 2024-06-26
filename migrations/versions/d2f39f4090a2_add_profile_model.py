"""Add profile model

Revision ID: d2f39f4090a2
Revises: def89ec4a042
Create Date: 2024-06-26 19:32:59.669017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2f39f4090a2'
down_revision = 'def89ec4a042'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('life_stage_score', sa.Integer(), nullable=True),
    sa.Column('financial_resources_score', sa.Integer(), nullable=True),
    sa.Column('investment_experience_score', sa.Integer(), nullable=True),
    sa.Column('emotional_risk_tolerance_score', sa.Integer(), nullable=True),
    sa.Column('total_score', sa.Integer(), nullable=True),
    sa.Column('risk_category', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    # ### end Alembic commands ###
