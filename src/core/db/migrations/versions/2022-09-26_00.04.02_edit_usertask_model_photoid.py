"""edit_usertask_model_photoid

Revision ID: 2c2d12934211
Revises: d37fa6413c00
Create Date: 2022-09-26 00:04:02.709015

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2c2d12934211'
down_revision = 'd37fa6413c00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_tasks', 'photo_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_tasks', 'photo_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    # ### end Alembic commands ###
