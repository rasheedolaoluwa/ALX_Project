"""Initial migration.

Revision ID: 6d2eedc23384
Revises: 
Create Date: 2024-07-09 15:25:32.374204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d2eedc23384'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=False),
    sa.Column('email_verified', sa.Boolean(), nullable=True),
    sa.Column('risk_category', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('life_stage_score', sa.Integer(), nullable=True),
    sa.Column('financial_resources_score', sa.Integer(), nullable=True),
    sa.Column('investment_experience_score', sa.Integer(), nullable=True),
    sa.Column('emotional_risk_tolerance_score', sa.Integer(), nullable=True),
    sa.Column('total_score', sa.Integer(), nullable=True),
    sa.Column('life_stage_message', sa.String(length=256), nullable=True),
    sa.Column('financial_resources_message', sa.String(length=256), nullable=True),
    sa.Column('investment_experience_message', sa.String(length=256), nullable=True),
    sa.Column('emotional_risk_tolerance_message', sa.String(length=256), nullable=True),
    sa.Column('risk_category', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    op.drop_table('user')
    # ### end Alembic commands ###
