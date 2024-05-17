"""subindo base em prod

Revision ID: 7ef741be71c9
Revises: 
Create Date: 2024-05-15 21:18:21.073198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ef741be71c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('approved_card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo_de_pessoa', sa.String(length=50), nullable=False),
    sa.Column('nome_raz_o_social', sa.String(length=255), nullable=False),
    sa.Column('cpf', sa.String(length=14), nullable=True),
    sa.Column('estado_civil', sa.String(length=50), nullable=False),
    sa.Column('telefone', sa.String(length=20), nullable=False),
    sa.Column('e_mail', sa.String(length=100), nullable=False),
    sa.Column('valor_total_da_compra', sa.String(length=100), nullable=False),
    sa.Column('qual_tipo_de_im_vel', sa.String(length=50), nullable=False),
    sa.Column('cep', sa.String(length=10), nullable=False),
    sa.Column('endere_o', sa.String(length=255), nullable=False),
    sa.Column('n_mero', sa.String(length=10), nullable=False),
    sa.Column('bairro', sa.String(length=100), nullable=False),
    sa.Column('cidade', sa.String(length=100), nullable=False),
    sa.Column('estado', sa.String(length=50), nullable=False),
    sa.Column('qual_valor_do_im_vel', sa.String(length=100), nullable=False),
    sa.Column('qual_o_valor_do_empr_stimo', sa.String(length=100), nullable=False),
    sa.Column('prazo_pagamento', sa.String(length=50), nullable=False),
    sa.Column('indica_o', sa.String(length=100), nullable=True),
    sa.Column('assessor_respons_vel', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo_de_pessoa', sa.String(length=50), nullable=False),
    sa.Column('nome_raz_o_social', sa.String(length=255), nullable=False),
    sa.Column('cpf', sa.String(length=14), nullable=True),
    sa.Column('estado_civil', sa.String(length=50), nullable=False),
    sa.Column('telefone', sa.String(length=20), nullable=False),
    sa.Column('e_mail', sa.String(length=100), nullable=False),
    sa.Column('valor_total_da_compra', sa.String(length=100), nullable=False),
    sa.Column('qual_tipo_de_im_vel', sa.String(length=50), nullable=False),
    sa.Column('cep', sa.String(length=10), nullable=False),
    sa.Column('endere_o', sa.String(length=255), nullable=False),
    sa.Column('n_mero', sa.String(length=10), nullable=False),
    sa.Column('bairro', sa.String(length=100), nullable=False),
    sa.Column('cidade', sa.String(length=100), nullable=False),
    sa.Column('estado', sa.String(length=50), nullable=False),
    sa.Column('qual_valor_do_im_vel', sa.String(length=100), nullable=False),
    sa.Column('qual_o_valor_do_empr_stimo', sa.String(length=100), nullable=False),
    sa.Column('prazo_pagamento', sa.String(length=50), nullable=False),
    sa.Column('indica_o', sa.String(length=100), nullable=True),
    sa.Column('assessor_respons_vel', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=True),
    sa.Column('cnpj', sa.String(length=14), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cnpj'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('cards')
    op.drop_table('approved_card')
    # ### end Alembic commands ###