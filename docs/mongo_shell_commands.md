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

