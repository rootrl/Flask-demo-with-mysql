"""empty message

Revision ID: 57c0db215a45
Revises: e28f15c8bc0f
Create Date: 2019-12-21 16:07:53.976025

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '57c0db215a45'
down_revision = 'e28f15c8bc0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('article', 'ext_field_1',
               existing_type=mysql.VARCHAR(length=1024),
               nullable=False)
    op.alter_column('article', 'ext_field_2',
               existing_type=mysql.VARCHAR(length=1024),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('article', 'ext_field_2',
               existing_type=mysql.VARCHAR(length=1024),
               nullable=True)
    op.alter_column('article', 'ext_field_1',
               existing_type=mysql.VARCHAR(length=1024),
               nullable=True)
    # ### end Alembic commands ###
