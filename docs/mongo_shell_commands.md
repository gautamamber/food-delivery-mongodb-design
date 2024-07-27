# MongoDB Shell Commands

This document provides a list of common MongoDB shell commands used for database management and operations. 

### 1. Connecting to MongoDB

To connect to a MongoDB server using the MongoDB shell, use the `mongo` command. 

**Command:**
```sh

mongo
mongo --host <hostname> --port <port>
mongo --host <hostname> --port <port> -u <username> -p <password> --authenticationDatabase <database>
```
### 2. Database operations

##### Listing Databases
```shell
show databases
```

##### Selecting Databases
```shell
use <database_name>
```
##### Creating a Database
 ```shell
use <database_name>
db.createCollection("testCollection")
```
##### Dropping a database
```shell
db.dropDatabase()
```
### 3. Collection operations

##### Creating a Collection
```shell
db.createCollection("<collection_name>")
```
##### Listing Collections
```shell
show collections

```
##### Dropping a Collection
```shell
db.<collection_name>.drop()
```

### 4. Document Operations

##### Inserting Documents
```shell
db.<collection_name>.insertOne({
    field1: "value1",
    field2: "value2"
})

```
##### Insert Multiple Documents
```shell
db.<collection_name>.insertMany([
    { field1: "value1", field2: "value2" },
    { field1: "value3", field2: "value4" }
])

```
##### Find single document
```shell
db.<collection_name>.find({ query })
```

##### Find with specific query
```shell
db.<collection_name>.find({ field: "value" })
```

##### Updating a Document
```shell
db.<collection_name>.updateOne(
    { query },
    { $set: { field1: "new_value" } }
)
```


##### Deleting Document 
```shell
db.<collection_name>.deleteOne({ query })
db.<collection_name>.deleteMany({ query })

```