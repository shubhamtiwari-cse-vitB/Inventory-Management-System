# System Architecture

The Inventory Management System follows a simple menu-driven architecture where the user interacts with the Python application, which performs operations on the MySQL database.

```mermaid
flowchart TD
    A[User] --> B[Python Inventory Management System]
    
    B --> C[Product Management]
    B --> D[Purchase Management]
    B --> E[Invoice Management]
    
    C --> F[(MySQL Database)]
    D --> F
    E --> F
    
    F --> G[Product Table]
    F --> H[Purchase Table]
    F --> I[Invoice Table]
