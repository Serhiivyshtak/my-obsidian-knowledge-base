# SQL Data Types

Always when creating tables in SQL, developer must decide which data type to use for each column. The data type is a guideline for SQL to understand what type of data is expected inside of each column, and it also identifies how SQL will interact with the stored data.

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
| *INT(size)* | A normal-sized integer. *size* specifies the display length. Default for *size* is 11 | Signed: -2147483648 to 2147483647 (2 billion) <br> Unsigned: 0 to 4294967295 (4 billion) | Identifiers, counts, population |
| *TINYINT(size)* | Small integer. *size* specifies the display length. Default for *size* is 4 | Signed: -128 to 127 <br> Unsigned: 0 to 255 | Small counts, age, day of the week |
| *BIGINT(size)* | Large integer. *size* specifies the display length. Default for *size* is 20 | Signed: -9223372036854775808 to 9223372036854775807 (9 quintillion) <br> Unsigned: 0 to 18446744073709551615 (18 quintillion) | Very big counts, distance in meters, time in milliseconds |
| *DOUBLE* | A normal-sized floating-point number. Approximate precision, not exact. | 8 bytes <br> Range: ±1.8 × 10³⁰⁸ <br> Precision: ~15 digits | Scientific calculations, statistics, averages |
| *FLOAT* | A small floating-point number. Approximate precision, not exact. | 4 bytes <br> Range: ±3.4 × 10³⁸ <br> Precision: ~7 digits | Game coordinates, sensor data, graphics |
| *DECIMAL(p,d)* | Exact fixed-point number. *p* = total digits (max 65), *d* = decimal places (max 30) | Varies based on precision <br> Range: up to 10⁶⁵ - 1 <br> Precision: Exact | Money, prices, tax rates, GPS coordinates |

### Other data types

| Data type | Description | Size | Use Cases |
| - | - | - | - |
| *BOOLEAN* | Boolean value. 0 represents False and all other numbers represent True. *BOOLEAN* is an alias for *TINYINT(1)* | -128 to 127 | Account statuses |
| *JSON* | Structured JSON documents. Throws an error if invalid JSON passed | Default: up to 64 MB <br> Configurable max value: 1 GB | API responses, dynamic properties |
| *DATE* | Date in format of 'YYYY-MM-DD' | '1000-01-01' to '9999-12-31' | Dates of birth, Last updated dates |
| *YEAR* | Year in format of 'YYYY' | 1901 to 2155, and 0000 | Movie release years, years of birth |
| *TIME* | Time in format of 'HH:MM:SS' | '-838:59:59' to '838:59:59' | Store opening hours, duration, elapsed time |
| *DATETIME* | Date and time in format of 'YYYY-MM-DD HH:MM:SS' | '1000-01-01 00:00:00' to '9999-12-31 23:59:59' | Event schedules, appointment dates, historical records |
| *TIMESTAMP* | Date and time, stored as UTC and converted to current timezone on retrieval | '1970-01-01 00:00:01' to '2038-01-19 03:14:07' | Created at, updated at, audit logs |
| *BLOB* | Binary Large Object for storing binary data | Up to 65 KB <br> MEDIUMBLOB: 16 MB <br> LONGBLOB: 4 GB | Images, files, encrypted data (prefer filesystem storage) |

