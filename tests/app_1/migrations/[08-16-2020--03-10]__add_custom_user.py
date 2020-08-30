"""add custom user

Revision ID: 4839408a6f78
Revises: 51dfa20071b0
Create Date: 2020-08-16 03:10:00.842107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4839408a6f78"
down_revision = "51dfa20071b0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "app_1_custom_user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("username", sa.String(), nullable=True),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column("date_joined", sa.DateTime(), nullable=True),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("is_staff", sa.Boolean(), nullable=False),
        sa.Column("permission_group", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["permission_group"],
            ["auth_group.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("app_1_custom_user")
    # ### end Alembic commands ###
