"""update text_search_index

Revision ID: 1bf70b8d9122
Revises: d75dce0b483a
Create Date: 2017-04-05 11:29:32.113917

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '1bf70b8d9122'
down_revision = 'd75dce0b483a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('of_text_search_unique', 'observation_fact', ['text_search_index'], unique=False)
    op.drop_constraint('observation_fact_text_search_index_key', 'observation_fact', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('observation_fact_text_search_index_key', 'observation_fact', ['text_search_index'])
    op.drop_index('of_text_search_unique', table_name='observation_fact')
    # ### end Alembic commands ###
