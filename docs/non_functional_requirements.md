# Non-Functional Requirements

## 1. Usability
- The system provides a simple menu-driven interface.
- Users can select operations using numbered menu options.
- Input prompts make the operations easy to understand.

## 2. Reliability
- The system validates important user inputs.
- Database operations are performed through MySQL.
- The system maintains separate records for products, purchases, and invoices.

## 3. Maintainability
- The system is organized into separate functions for different operations.
- Functions are used for product management, purchasing, searching, sorting, and updating.
- The documentation explains the system structure and workflow.

## 4. Performance
- Product records can be searched and sorted using database queries.
- MySQL is used to store and retrieve inventory data efficiently.
- The system is designed for quick execution of common inventory operations.

## 5. Error Handling
- Input validation is used for important fields such as product numbers and quantities.
- The system provides messages when required records are not found.
- Invalid selections are handled through menu validation.
