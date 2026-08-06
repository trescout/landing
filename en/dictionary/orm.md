# What is ORM?

> Object-Relational Mapping

It is a bridge that converts database tables into objects in code.

## Overview
It allows you to use this data like objects in a programming language, instead of dealing with complex tables in the database when developing software. In this way, you can manage data without writing complex queries such as SQL. It makes your code more readable and manageable.

*Analogy: Think of the raw data in the database as boxes; ORM is like a helper that opens these boxes for you and turns the items inside into objects that you can use directly.*

## How it works
It works as a layer between the database and the application code. When you save data in your code, it translates this operation into the appropriate SQL query in the background. This way, even if the database structure changes, you only need to change your code slightly.

## Where it is used
It is frequently used in web applications, enterprise software and database-intensive projects.

## Commonly confused with
It may be confused with the database driver; The driver provides the raw connection, while the ORM facilitates this connection.

## Frequently asked questions
**Why should I use ORM?**
It speeds up database operations and reduces code errors.

**Does it reduce performance?**
For very complex queries, manual SQL can sometimes be faster, but in most cases the convenience is worth it.


## Related terms
- [Database](/en/dictionary/database/)
- [Tech Stack](/en/dictionary/tech-stack/)

## Related tools
- [Prisma](/en/discover/prisma/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/orm/
