# database/models/variant.py

from sqlalchemy import Column, BigInteger, String, Integer, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from database.base import Base

class Variant(Base):
    __tablename__ = "variants"

    id = Column(BigInteger, primary_key=True)  # Shopify variant ID
    product_id = Column(BigInteger, ForeignKey("products.id"), nullable=False)

    title = Column(String)
    sku = Column(String)
    price = Column(String)
    compare_at_price = Column(String)

    options = Column(JSONB)  # e.g., {"Nail shape": "Coffin", "Size": "XS"}

    inventory_quantity = Column(Integer)
    inventory_policy = Column(String)
    inventory_management = Column(String)
    fulfillment_service = Column(String)
    barcode = Column(String)

    taxable = Column(Boolean)
    grams = Column(Integer)
    weight = Column(Float)
    weight_unit = Column(String)
    requires_shipping = Column(Boolean)

    position = Column(Integer)
    image_id = Column(BigInteger, nullable=True)
    inventory_item_id = Column(BigInteger)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    product = relationship("Product", back_populates="variants", lazy="joined")