"""empty message

Revision ID: e48825cc8fc8
Revises: 
Create Date: 2019-06-03 15:15:15.245574

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e48825cc8fc8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employee_email'), 'employee', ['email'], unique=True)
    op.create_index(op.f('ix_employee_first_name'), 'employee', ['first_name'], unique=False)
    op.create_index(op.f('ix_employee_last_name'), 'employee', ['last_name'], unique=False)
    op.create_index(op.f('ix_employee_username'), 'employee', ['username'], unique=True)
    op.drop_table('myusers')
    op.drop_table('tbl_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_user',
    sa.Column('user_id', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False),
    sa.Column('user_name', mysql.VARCHAR(charset='utf8', collation='utf8_unicode_ci', length=45), nullable=True),
    sa.Column('user_email', mysql.VARCHAR(charset='utf8', collation='utf8_unicode_ci', length=45), nullable=True),
    sa.Column('user_password', mysql.VARCHAR(charset='utf8', collation='utf8_unicode_ci', length=255), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('myusers',
    sa.Column('firstname', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('lastname', mysql.VARCHAR(length=30), nullable=False),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_index(op.f('ix_employee_username'), table_name='employee')
    op.drop_index(op.f('ix_employee_last_name'), table_name='employee')
    op.drop_index(op.f('ix_employee_first_name'), table_name='employee')
    op.drop_index(op.f('ix_employee_email'), table_name='employee')
    op.drop_table('employee')
    op.drop_table('roles')
    op.drop_table('departments')
    # ### end Alembic commands ###
