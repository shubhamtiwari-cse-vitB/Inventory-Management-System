# Testing

The Inventory Management System was tested by performing different operations through the menu-driven interface.

## Test Cases

| Test Case | Operation | Expected Result |
|---|---|---|
| TC01 | Display Products | Existing product records are displayed |
| TC02 | Add Product | New product information is stored in the database |
| TC03 | Search Product | Product information is displayed when the product number is entered |
| TC04 | Delete Product | Selected product is removed from the database |
| TC05 | Update Product | Selected product information is updated |
| TC06 | Sort Products | Product records are displayed according to the selected sorting option |
| TC07 | Purchase / Order | Purchase information is stored and invoice information is generated |
| TC08 | Purchase History | Stored purchase records are displayed |
| TC09 | Invoice Management | Stored invoice records are displayed |
| TC10 | Exit | The application terminates |

## Testing Approach

The system was tested manually by entering different inputs through the command-line menu.

The main areas tested were:

- Product management
- Product searching
- Product updating
- Product deletion
- Product sorting
- Purchase and order processing
- Purchase history
- Invoice management

## Expected Outcome

The system should perform the selected operation and display an appropriate result or message to the user.

Database operations are performed using MySQL, allowing product, purchase and invoice information to be stored persistently.
