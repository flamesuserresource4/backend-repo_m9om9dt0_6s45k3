"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
Each model name maps to a collection using its lowercase name.
"""
from typing import Optional, List, Literal
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

# Core site data
class MenuItem(BaseModel):
    category: Literal["Starters", "Mains", "Desserts", "Drinks"]
    name: str = Field(..., max_length=120)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., ge=0)
    image_url: Optional[str] = None
    is_signature: bool = False
    available: bool = True

class Reservation(BaseModel):
    date: str = Field(..., description="YYYY-MM-DD")
    time: str = Field(..., description="HH:MM")
    party_size: int = Field(..., ge=1, le=20)
    name: str
    email: EmailStr
    phone: str
    notes: Optional[str] = None
    status: Literal["pending", "confirmed", "waitlist", "cancelled"] = "pending"

class AvailabilityQuery(BaseModel):
    date: str
    time: str
    party_size: int

class EventRequest(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    event_type: Literal["Private Dining", "Catering", "Corporate", "Wedding", "Other"]
    preferred_date: Optional[str] = None
    guests: int = Field(..., ge=1, le=200)
    message: Optional[str] = None

class Testimonial(BaseModel):
    name: str
    rating: int = Field(..., ge=1, le=5)
    quote: str
    source: Optional[str] = None

# Optional contact submissions
class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    subject: Optional[str] = None
    message: str
