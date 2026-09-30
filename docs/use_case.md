# Use Case Diagram

## Actors

The main actor of the system is the **User**.

## Use Cases

The user can perform the following operations:

- Display Products
- Add Products
- Search Products
- Delete Products
- Update Products
- Sort Products
- Place Order / Record Purchase
- View Purchase History
- View Invoices
- Delete Purchase Records
- Delete Invoice Records

## Use Case Representation

```mermaid
flowchart LR
    U[User]

    U --> A[Display Products]
    U --> B[Add Products]
    U --> C[Search Products]
    U --> D[Delete Products]
    U --> E[Update Products]
    U --> F[Sort Products]
    U --> G[Order / Purchase]
    U --> H[Purchase History]
    U --> I[Invoice Management]
    U --> J[Delete Purchase Records]
    U --> K[Delete Invoice Records]
