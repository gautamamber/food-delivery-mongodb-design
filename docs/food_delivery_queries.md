## Food Delivery Application

### Basic Queries

#### Import the models

```python
import datetime
from bson import ObjectId
from delivery.models import User, Restaurant, Order, OrderItem, Review, DeliveryPerson, Address, MenuItem
```

#### 1. Create a new user (Customer)
```python
address = Address(street="123 Main St", city="Springfield", state="IL", zip="62701")
new_user = User(username="john_doe", email="john@example.com", password="password123", address=address, phone="555-1234", role="customer")
new_user.save()
```

#### 2. Retrieve all users
```python
all_users = User.objects.all()
print(all_users)
for user in all_users:
    print(user.to_json())
```

#### 3. Filter users by role
```python
customers = User.objects.filter(role="customer")
print(customers)
for customer in customers:
    print(customer.to_json())
```

#### 4. Create a new delivery person
```python
# Define the address for the new user
delivery_user_address = Address(street="456 Elm St", city="Springfield", state="IL", zip="62702")

# Create the new user with the delivery_person role
delivery_new_user = User(
    username="jane_doe",
    email="jane@example.com",
    password="securepassword456",
    address=delivery_user_address,
    phone="555-6789",
    role="delivery_person"
)

# Save the new user to the database
delivery_new_user.save()

new_delivery_person = DeliveryPerson(
    user_id=delivery_new_user,
    vehicle_details="Bike",
    rating=4.8
)

# Save the delivery person to the database
new_delivery_person.save()

```

#### 5. Retrieve all delivery persons
```python
all_delivery_persons = DeliveryPerson.objects.all()
print(all_delivery_persons)
```

#### 6. Filter delivery persons by rating
```python
top_rated_delivery_persons = DeliveryPerson.objects.filter(rating__gte=4.5)
print(top_rated_delivery_persons)
```

#### 7. Create a new restaurant
```python
menu_item = MenuItem(item_id=None, name="Burger", description="Tasty burger", price=5.99, category="main course")
restaurant_address = Address(street="456 Market St", city="Springfield", state="IL", zip="62701")
new_restaurant = Restaurant(name="Burger House", address=restaurant_address, phone="555-5678", cuisine=["American"], rating=4.5, menu=[menu_item])
new_restaurant.save()
```

#### 8. Retrieve all restaurants
```python
all_restaurants = Restaurant.objects.all()
print(all_restaurants)
for restaurants in all_restaurants:
    print(restaurants.to_json())
```

#### 9. Filter restaurants by rating
```python
top_rated_restaurants = Restaurant.objects.filter(rating__gte=4.0)
print(top_rated_restaurants)
```

#### 10. Create a new order
```python
order_item = OrderItem(item_id=menu_item.item_id, name="Burger", price=5.99, quantity=2)
new_order = Order(user_id=new_user, restaurant_id=new_restaurant, delivery_person_id=delivery_new_user, order_items=[order_item], total_price=11.98, status="placed")
new_order.save()
```

#### 11. Retrieve all orders
```python
all_orders = Order.objects.all()
print(all_orders)
```

#### 12. Filter orders by status
```python
placed_orders = Order.objects.filter(status="placed")
print(placed_orders)
```

#### 13. Create a new review
```python
new_review = Review(user_id=new_user, restaurant_id=new_restaurant, rating=5, comment="Great food!", created_at=datetime.datetime.utcnow())
new_review.save()
```

#### 14. Retrieve all reviews
```python
all_reviews = Review.objects.all()
print(all_reviews)
```

#### 15. Filter reviews by rating
```python
high_rated_reviews = Review.objects.filter(rating__gte=4.0)
print(high_rated_reviews)
```


### Aggregation Queries

##### Get average rating of all restaurant
```python
pipeline = [
    {
        "$group": {
            "_id": None,
            "average_rating": {"$avg": "$rating"}
        }
    }
]

average_rating = Restaurant.objects.aggregate(pipeline)
for result in average_rating:
    print(result)

```

##### Count order by status

```python
pipeline = [
    {
        "$group": {
            "_id": "$status",
            "count": {"$sum": 1}
        }
    }
]

order_counts = Order.objects.aggregate(pipeline)
for result in order_counts:
    print(result)

```

##### Total revenue by Restaurant
```python
pipeline = [
    {
        "$group": {
            "_id": "$restaurant_id",
            "total_revenue": {"$sum": "$total_price"}
        }
    }
]

total_revenue = Order.objects.aggregate(pipeline)
for result in total_revenue:
    print(result)

```

##### Top most ordered items
```python
pipeline = [
    {
        "$unwind": "$order_items"
    },
    {
        "$group": {
            "_id": "$order_items.name",
            "total_quantity": {"$sum": "$order_items.quantity"}
        }
    },
    {
        "$sort": {"total_quantity": -1}
    },
    {
        "$limit": 5
    }
]

top_items = Order.objects.aggregate(pipeline)
for result in top_items:
    print(result)

```

##### Average delivery person  rating
```python
pipeline = [
    {
        "$group": {
            "_id": None,
            "average_rating": {"$avg": "$rating"}
        }
    }
]

average_rating = DeliveryPerson.objects.aggregate(pipeline)
for result in average_rating:
    print(result)

```

##### Average order value by customer
```python
pipeline = [
    {
        "$group": {
            "_id": "$user_id",
            "average_order_value": {"$avg": "$total_price"}
        }
    }
]

average_order_value = Order.objects.aggregate(pipeline)
for result in average_order_value:
    print(result)

```

##### Top 5 customer by total spending

```pipeline = [
    {
        "$match": {
            "status": "delivered"
        }
    },
    {
        "$group": {
            "_id": "$user_id",
            "total_spent": {"$sum": "$total_price"}
        }
    },
    {
        "$sort": {"total_spent": -1}
    },
    {
        "$limit": 5
    },
    {
        "$project": {
            "_id": 0,
            "user_id": "$_id",
            "total_spent": 1
        }
    }
]

top_customers = Order.objects.aggregate(pipeline)
for result in top_customers:
    print(result)
```