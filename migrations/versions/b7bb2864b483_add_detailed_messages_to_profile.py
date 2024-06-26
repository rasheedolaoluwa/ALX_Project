"""Add detailed messages to profile

Revision ID: b7bb2864b483
Revises: d2f39f4090a2
Create Date: 2024-06-26 21:33:15.005849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7bb2864b483'
down_revision = 'd2f39f4090a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profile', schema=None) as batch_op:
        batch_op.add_column(sa.Column('life_stage_message', sa.String(length=256), nullable=True))
        batch_op.add_column(sa.Column('financial_resources_message', sa.String(length=256), nullable=True))
        batch_op.add_column(sa.Column('investment_experience_message', sa.String(length=256), nullable=True))
        batch_op.add_column(sa.Column('emotional_risk_tolerance_message', sa.String(length=256), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profile', schema=None) as batch_op:
        batch_op.drop_column('emotional_risk_tolerance_message')
        batch_op.drop_column('investment_experience_message')
        batch_op.drop_column('financial_resources_message')
        batch_op.drop_column('life_stage_message')

    # ### end Alembic commands ###
