from mongoengine import Document, EmbeddedDocument, fields
import datetime


class Address(EmbeddedDocument):
    """Represents a physical address with street, city, state, and zip code."""
    street = fields.StringField(required=True)
    city = fields.StringField(required=True)
    state = fields.StringField(required=True)
    zip = fields.StringField(required=True)


class MenuItem(EmbeddedDocument):
    """Represents an item on a restaurant's menu with details like name, description, price, and category."""
    item_id = fields.ObjectIdField()
    name = fields.StringField(required=True)
    description = fields.StringField()
    price = fields.FloatField(required=True)
    category = fields.StringField(choices=["starter", "main course", "dessert"], required=True)


class User(Document):
    """Represents a user in the system"""
    username = fields.StringField(required=True, unique=True)
    email = fields.EmailField(required=True, unique=True)
    password = fields.StringField(required=True)
    address = fields.EmbeddedDocumentField(Address)
    phone = fields.StringField(required=True)
    role = fields.StringField(choices=["customer", "delivery_person"], required=True)
    created_at = fields.DateTimeField(default=datetime.datetime.utcnow)


class Restaurant(Document):
    """Represents a restaurant entity"""
    name = fields.StringField(required=True)
    address = fields.EmbeddedDocumentField(Address, required=True)
    phone = fields.StringField(required=True)
    cuisine = fields.ListField(fields.StringField())
    rating = fields.FloatField()
    created_at = fields.DateTimeField(default=datetime.datetime.utcnow)
    menu = fields.EmbeddedDocumentListField(MenuItem)


class OrderItem(EmbeddedDocument):
    """Represents an item within an order, including the item ID, name, price, and quantity."""
    item_id = fields.ObjectIdField()
    name = fields.StringField(required=True)
    price = fields.FloatField(required=True)
    quantity = fields.IntField(required=True)


class Order(Document):
    """Represents a customer's order from a restaurant"""
    user_id = fields.ReferenceField(User, required=True)
    restaurant_id = fields.ReferenceField(Restaurant, required=True)
    delivery_person_id = fields.ReferenceField(User, required=True)
    order_items = fields.EmbeddedDocumentListField(OrderItem, required=True)
    total_price = fields.FloatField(required=True)
    status = fields.StringField(choices=["placed", "in_transit", "delivered", "cancelled"], required=True)
    order_date = fields.DateTimeField(default=datetime.datetime.utcnow)
    delivery_date = fields.DateTimeField()


class Review(Document):
    """Represents a user's review of a restaurant"""
    user_id = fields.ReferenceField(User, required=True)
    restaurant_id = fields.ReferenceField(Restaurant, required=True)
    rating = fields.FloatField(required=True)
    comment = fields.StringField()
    created_at = fields.DateTimeField(default=datetime.datetime.utcnow)


class DeliveryPerson(Document):
    """Represents a delivery person's details, including their user ID, vehicle details, rating, and creation date."""
    user_id = fields.ReferenceField(User, required=True)
    vehicle_details = fields.StringField()
    rating = fields.FloatField()
    created_at = fields.DateTimeField(default=datetime.datetime.utcnow)
