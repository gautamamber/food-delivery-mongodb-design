### DB schema

```python
+------------+       +--------------+       +----------+
|   User     |       |  Restaurant  |       |  Review  |
+------------+       +--------------+       +----------+
| username   |       | name         |       | user_id  |
| email      |       | address      |       | restaurant_id |
| password   |       | phone        |       | rating   |
| address    |       | cuisine      |       | comment  |
| phone      |       | rating       |       | created_at |
| role       |       | created_at   |       +----------+
| created_at |       | menu         |
+------------+       +--------------+
     |                    |                  |
     |                    |                  |
     +---------+          +----------+       |
               |                     |       |
           +------------+       +--------------+ 
           |   Order    |       | DeliveryPerson|
           +------------+       +--------------+
           | user_id    |       | user_id      |
           | restaurant_id|     | vehicle_details |
           | delivery_person_id | | rating      |
           | order_items |       | created_at   |
           | total_price |       +--------------+
           | status      |
           | order_date  |
           | delivery_date|
           +------------+


```


### Schema Explanation

# Food Delivery Application Database Schema

This document outlines the MongoDB schema for a food delivery application using MongoEngine ODM. The database consists of multiple collections and embedded documents, each representing different entities and their relationships within the system.

## Collections and Embedded Documents

### 1. User Collection

Represents users in the system. Users can have roles such as `customer` or `delivery_person`.

**Fields:**
- `username` (String, required, unique)
- `email` (String, required, unique)
- `password` (String, required)
- `address` (Embedded Document: Address)
- `phone` (String, required)
- `role` (String, required, choices: `customer`, `delivery_person`)
- `created_at` (DateTime, default: current time)

**Roles:**
- `customer`
- `delivery_person`

### 2. Restaurant Collection

Represents a restaurant entity.

**Fields:**
- `name` (String, required)
- `address` (Embedded Document: Address, required)
- `phone` (String, required)
- `cuisine` (List of Strings)
- `rating` (Float)
- `created_at` (DateTime, default: current time)
- `menu` (Embedded Document List: MenuItem)

### 3. Order Collection

Represents a customer's order from a restaurant.

**Fields:**
- `user_id` (Reference: User, required)
- `restaurant_id` (Reference: Restaurant, required)
- `delivery_person_id` (Reference: User, required)
- `order_items` (Embedded Document List: OrderItem, required)
- `total_price` (Float, required)
- `status` (String, required, choices: `placed`, `in_transit`, `delivered`, `cancelled`)
- `order_date` (DateTime, default: current time)
- `delivery_date` (DateTime)

**Relationships:**
- References `User` (customer)
- References `Restaurant`
- References `User` (delivery person)

### 4. Review Collection

Represents a user's review of a restaurant.

**Fields:**
- `user_id` (Reference: User, required)
- `restaurant_id` (Reference: Restaurant, required)
- `rating` (Float, required)
- `comment` (String)
- `created_at` (DateTime, default: current time)

**Relationships:**
- References `User`
- References `Restaurant`

### 5. DeliveryPerson Collection

Represents a delivery person's details, including their user ID, vehicle details, rating, and creation date.

**Fields:**
- `user_id` (Reference: User, required)
- `vehicle_details` (String)
- `rating` (Float)
- `created_at` (DateTime, default: current time)

**Relationships:**
- References `User`

### 6. Address Embedded Document

Represents a physical address.

**Fields:**
- `street` (String, required)
- `city` (String, required)
- `state` (String, required)
- `zip` (String, required)

**Embedded in:**
- `User`
- `Restaurant`

### 7. MenuItem Embedded Document

Represents an item on a restaurant's menu.

**Fields:**
- `item_id` (ObjectId)
- `name` (String, required)
- `description` (String)
- `price` (Float, required)
- `category` (String, required, choices: `starter`, `main course`, `dessert`)

**Embedded in:**
- `Restaurant` (menu)

### 8. OrderItem Embedded Document

Represents an item within an order.

**Fields:**
- `item_id` (ObjectId)
- `name` (String, required)
- `price` (Float, required)
- `quantity` (Integer, required)

**Embedded in:**
- `Order` (order_items)
