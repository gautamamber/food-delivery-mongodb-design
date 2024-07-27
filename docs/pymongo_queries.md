## Pymongo Queries

#### Import Pymongo client

```python
from pymongo import MongoClient
```

#### Establish a connection to the MongoDB server
```python
client = MongoClient('localhost', 27017)
```


#### 1. List all databases
```python
database_names = client.list_database_names()
print(database_names)
```

#### 2. Create database
```python
db = client['TestDataBase']
```

#### 3. Create collections
```python
collection = db.create_collection('Student')
```

#### 4. List collections
```python
collection_names = db.list_collection_names()
print(collection_names)
```

#### 5. Add data in collections
```python
data = {'name': 'John', 'age': 12, 'is_active': True}
collection.insert_one(data)
```


#### 6. Remove data in collection
```python
collection.delete_one({'name': 'John'})
```


#### Find data in collection
```python
found_data = collection.find_one({'name': 'John'})
print(found_data)
```


#### Update data in collection
```python
collection.update_one({'name': 'John'}, {'$set': {'age': 13}})
```


#### 7. Add indexing
```python
collection.create_index([('name', 1)])
```
