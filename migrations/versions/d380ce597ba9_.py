"""empty message

Revision ID: d380ce597ba9
Revises: f9ddc0f6d02d
Create Date: 2021-07-18 19:16:23.788566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd380ce597ba9'
down_revision = 'f9ddc0f6d02d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dishes', 'description',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=5000),
               existing_nullable=True)
    op.alter_column('dishes', 'description_uz',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=5000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dishes', 'description_uz',
               existing_type=sa.String(length=5000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
    op.alter_column('dishes', 'description',
               existing_type=sa.String(length=5000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
    # ### end Alembic commands ###
