"""initial schema

Revision ID: e6c007a09a72
Revises: 
Create Date: 2025-05-29 19:10:25.950453

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6c007a09a72'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agents',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('nom', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('actif', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('articles',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('sku', sa.String(), nullable=False),
    sa.Column('designation', sa.String(), nullable=False),
    sa.Column('categorie', sa.Enum('PRODUIT', 'PIECE', 'CONSOMMABLE', name='categoriearticle'), nullable=False),
    sa.Column('poids_kg', sa.Float(), nullable=False),
    sa.Column('volume_m3', sa.Float(), nullable=False),
    sa.Column('date_peremption', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sku')
    )
    op.create_table('commandes',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('reference', sa.String(), nullable=False),
    sa.Column('etat', sa.Enum('BROUILLON', 'RESERVEE', 'PREPAREE', 'EXPEDIEE', 'ANNULEE', name='etatcommande'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('reference')
    )
    op.create_table('emplacements',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('type', sa.Enum('STOCKAGE', 'VENTE', 'RESERVATION', 'RECEPTION', 'EXPEDITION', name='typeemplacement'), nullable=False),
    sa.Column('capacite_poids_kg', sa.Float(), nullable=False),
    sa.Column('capacite_volume_m3', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('implantations',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('article_id', sa.String(), nullable=False),
    sa.Column('emplacement_id', sa.String(), nullable=False),
    sa.Column('quantite', sa.Integer(), nullable=False),
    sa.Column('seuil_minimum', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
    sa.ForeignKeyConstraint(['emplacement_id'], ['emplacements.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lignes_commandes',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('commande_id', sa.String(), nullable=True),
    sa.Column('article_id', sa.String(), nullable=True),
    sa.Column('quantite', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
    sa.ForeignKeyConstraint(['commande_id'], ['commandes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('missions',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('type', sa.Enum('DEPLACEMENT', 'REAPPRO', 'INVENTAIRE', 'RECEPTION', 'PREPARATION', name='typemission'), nullable=False),
    sa.Column('etat', sa.Enum('A_FAIRE', 'EN_COURS', 'TERMINE', 'ECHOUE', name='etatmission'), nullable=False),
    sa.Column('article_id', sa.String(), nullable=False),
    sa.Column('source_id', sa.String(), nullable=True),
    sa.Column('destination_id', sa.String(), nullable=True),
    sa.Column('quantite', sa.Integer(), nullable=False),
    sa.Column('agent_id', sa.String(), nullable=True),
    sa.Column('date_creation', sa.DateTime(), nullable=True),
    sa.Column('date_execution', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['agent_id'], ['agents.id'], ),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
    sa.ForeignKeyConstraint(['destination_id'], ['emplacements.id'], ),
    sa.ForeignKeyConstraint(['source_id'], ['emplacements.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('receptions',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('article_id', sa.String(), nullable=False),
    sa.Column('quantite', sa.Integer(), nullable=False),
    sa.Column('fournisseur', sa.String(), nullable=False),
    sa.Column('date_reception', sa.DateTime(), nullable=True),
    sa.Column('emplacement_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
    sa.ForeignKeyConstraint(['emplacement_id'], ['emplacements.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('receptions')
    op.drop_table('missions')
    op.drop_table('lignes_commandes')
    op.drop_table('implantations')
    op.drop_table('emplacements')
    op.drop_table('commandes')
    op.drop_table('articles')
    op.drop_table('agents')
    # ### end Alembic commands ###
