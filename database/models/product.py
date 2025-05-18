# database/models/product.py

from sqlalchemy import Column, BigInteger, String, Text, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from database.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True)  # Shopify product ID
    title = Column(String, nullable=False)
    body_html = Column(Text)
    vendor = Column(String)
    product_type = Column(String)
    handle = Column(String, unique=True)
    status = Column(String)
    published_scope = Column(String)
    admin_graphql_api_id = Column(String)

    tags = Column(JSONB)               # e.g., ["Festival", "Limited Edition"]
    option_definitions = Column(JSONB) # e.g., [{"name": "Nail shape", "position": 1, "values": [...]}, ...]

    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    published_at = Column(DateTime)

    variants = relationship("Variant", back_populates="product", cascade="all, delete")