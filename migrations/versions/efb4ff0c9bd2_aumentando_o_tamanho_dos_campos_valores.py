"""aumentando o tamanho dos campos valores

Revision ID: efb4ff0c9bd2
Revises: 7e544ee8cb4e
Create Date: 2024-03-12 05:00:42.524614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efb4ff0c9bd2'
down_revision = '7e544ee8cb4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('approved_card', schema=None) as batch_op:
        batch_op.alter_column('valor_total_da_compra',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('qual_valor_do_im_vel',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('qual_o_valor_do_empr_stimo',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=100),
               existing_nullable=False)

    with op.batch_alter_table('cards', schema=None) as batch_op:
        batch_op.alter_column('valor_total_da_compra',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('qual_valor_do_im_vel',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('qual_o_valor_do_empr_stimo',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cards', schema=None) as batch_op:
        batch_op.alter_column('qual_o_valor_do_empr_stimo',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.alter_column('qual_valor_do_im_vel',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.alter_column('valor_total_da_compra',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)

    with op.batch_alter_table('approved_card', schema=None) as batch_op:
        batch_op.alter_column('qual_o_valor_do_empr_stimo',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.alter_column('qual_valor_do_im_vel',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.alter_column('valor_total_da_compra',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###
