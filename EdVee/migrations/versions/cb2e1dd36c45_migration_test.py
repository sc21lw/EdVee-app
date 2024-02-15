"""Migration Test

Revision ID: cb2e1dd36c45
Revises: aa55f42bca49
Create Date: 2024-01-27 13:50:44.264840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb2e1dd36c45'
down_revision = 'aa55f42bca49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('collection_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_project_collection', 'collection', ['collection_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('collection_id')

    # ### end Alembic commands ###
