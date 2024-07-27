### Aggregation queries

##### Collections

- Customers
- Orders

##### Insert data

```shell
# Switch to or create the database
use customer_order_db

# Create the Customers collection and insert sample data
db.customers.insertMany([
    {
        _id: ObjectId("64c8e9e5f8f5a15f85d5c9b1"),
        name: "Alice Johnson",
        email: "alice.johnson@example.com",
        phone: "555-1234"
    },
    {
        _id: ObjectId("64c8e9e5f8f5a15f85d5c9b2"),
        name: "Bob Smith",
        email: "bob.smith@example.com",
        phone: "555-5678"
    }
])

# Create the Orders collection and insert sample data
db.orders.insertMany([
    {
        _id: ObjectId("64c8e9e5f8f5a15f85d5c9c1"),
        customer_id: ObjectId("64c8e9e5f8f5a15f85d5c9b1"),
        order_date: ISODate("2024-07-25T10:00:00Z"),
        total: 150.00,
        status: "completed"
    },
    {
        _id: ObjectId("64c8e9e5f8f5a15f85d5c9c2"),
        customer_id: ObjectId("64c8e9e5f8f5a15f85d5c9b1"),
        order_date: ISODate("2024-07-26T14:30:00Z"),
        total: 200.00,
        status: "pending"
    },
    {
        _id: ObjectId("64c8e9e5f8f5a15f85d5c9c3"),
        customer_id: ObjectId("64c8e9e5f8f5a15f85d5c9b2"),
        order_date: ISODate("2024-07-27T09:15:00Z"),
        total: 100.00,
        status: "completed"
    }
])

```

### Queries

##### Find customer by name
```shell
db.customers.aggregate([
    {
        "$match": {
            "name": "Alice Johnson"
        }
    },
    {
        "$project": {
            "_id": 0,
            "name": 1,
            "email": 1,
            "phone": 1
        }
    }
])

```
##### Find order by status

```shell
db.customers.aggregate([
    {
        $match: {
            name: "Alice Johnson"
        }
    },
    {
        $project: {
            _id: 0,
            name: 1,
            email: 1,
            phone: 1
        }
    }
])

```

#####  Find Orders Exceeding a Certain Total
```shell
db.orders.aggregate([
    {
        $match: {
            total: { $gt: 100 }
        }
    },
    {
        $project: {
            _id: 0,
            customer_id: 1,
            total: 1
        }
    }
])

```