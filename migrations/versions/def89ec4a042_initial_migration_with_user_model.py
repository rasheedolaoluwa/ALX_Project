"""Initial migration with user model

Revision ID: def89ec4a042
Revises: 
Create Date: 2024-06-26 18:18:17.136733

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'def89ec4a042'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portfolio_investment')
    op.drop_table('portfolio')
    op.drop_table('notification')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=64),
               existing_nullable=False)
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
        batch_op.alter_column('username',
               existing_type=sa.String(length=64),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)

    op.create_table('notification',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('message', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('read', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='notification_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='notification_pkey')
    )
    op.create_table('portfolio',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('portfolio_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('total_value', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='portfolio_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='portfolio_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('portfolio_investment',
    sa.Column('portfolio_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('investment_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('quantity', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('current_value', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['portfolio_id'], ['portfolio.id'], name='portfolio_investment_portfolio_id_fkey'),
    sa.PrimaryKeyConstraint('portfolio_id', 'investment_id', name='portfolio_investment_pkey')
    )
    # ### end Alembic commands ###