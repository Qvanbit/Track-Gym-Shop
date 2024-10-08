"""Added relationships

Revision ID: a97ee03f69e3
Revises: cc1b3c31a5a6
Create Date: 2024-08-26 22:11:34.743094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a97ee03f69e3'
down_revision: Union[str, None] = 'cc1b3c31a5a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category_product',
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], )
    )
    op.add_column('category', sa.Column('is_visible', sa.Boolean(), nullable=True, comment='Отображение категории'))
    op.add_column('product', sa.Column('full_description', sa.Text(), nullable=False, comment='Полное описание товара, включая состав и прочую информацию'))
    op.add_column('product', sa.Column('is_visible', sa.Boolean(), nullable=True, comment='Отображение товара'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'is_visible')
    op.drop_column('product', 'full_description')
    op.drop_column('category', 'is_visible')
    op.drop_table('category_product')
    # ### end Alembic commands ###
