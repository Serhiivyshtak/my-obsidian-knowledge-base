# SQL Data Types

Always when creating tables in [[SQL (DE)|SQL]], developer must decide which data type to use for each column. The data type is a guideline for SQL to understand what type of data is expected inside of each column, and it also identifies how SQL will interact with the stored data.

> Data types might have different names in different databases. And even if the name is the same, the size and other details may be different!

## Most commonly used SQL data types

### String data types

| Data type | Description | Size | Use Cases |
| - | - | - | - |
| *CHAR(size)* | A fixed-length string. *size* variable specifies the length. If the string is shorter than *size* variable, then it will be padded with spaces to match the specified length | Up to 255 characters | Country codes, postal codes |
| *VARCHAR(size)* | A variable-length string. *size* specifies the maxium length | Up to 65535 characters | Usernames, email adresses, descriptions |
| *TEXT* | A normal-sized string. No need to specify the maximal length. Setting default value isn't possible | Up to 65535 characters | Comments, articles, descriptions |
| *MEDIUMTEXT* | A medium-sized string. No need to specify the maximal length. Setting default value isn't possible | Up to 16777215 characters | Big articles, HTML templates, book chapters |
| *ENUM(value1, value2, value3...)* | A string that can only have one value  from the predefined list of values. If a value is inserted that is not in the list, a blank value will be inserted | Up to 65535 values. Up to 255 characters fro each value | Account status, country codes |

### Numeric data types

| Data type | Description | Size | Use Cases |
| - | - | - | - |
| *BIT(size)* |
