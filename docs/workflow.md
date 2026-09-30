# System Workflow

The Inventory Management System follows a menu-driven workflow.

```mermaid
flowchart TD
    A[Start] --> B[Connect to MySQL Database]
    B --> C[Display Main Menu]

    C --> D{Select Operation}

    D --> E[Display Products]
    D --> F[Add Product]
    D --> G[Delete Product]
    D --> H[Update Product]
    D --> I[Sort Products]
    D --> J[Order / Purchase]
    D --> K[Purchase History]
    D --> L[Invoice Management]
    D --> M[Exit]

    E --> C
    F --> C
    G --> C
    H --> C
    I --> C
    J --> C
    K --> C
    L --> C

    M --> N[End]
