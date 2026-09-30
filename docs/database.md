# Database Design

## Database

The Inventory Management System uses MySQL for storing and managing application data.

The database used by the project is:

`himalaya`

## Tables

The system uses three main tables:

### 1. Product

The `product` table stores information about products.

| Field | Description |
|---|---|
| prod_name | Name of the product |
| prod_no | Product number |
| prod_instock | Available stock |
| prod_to_be_produced | Quantity to be produced |
| mrp | Maximum Retail Price |
| rate | Product rate |
| mfg | Manufacturing date |
| expiry | Expiry date |

### 2. Purchase

The `purchase` table stores information about product purchases.

| Field | Description |
|---|---|
| p_name | Product name |
| no_of_unit | Number of units |
| _mrp_ | Product MRP |
| _rate_ | Product rate |
| customer_name | Customer name |

### 3. Invoice

The `invoice` table stores invoice-related information.

| Field | Description |
|---|---|
| p_name | Product name |
| no_of_unit | Number of units |
| _mrp_ | Product MRP |
| _rate_ | Product rate |
| customer_name | Customer name |
| amount | Invoice amount |

## Database Flow

```text
Python Application
        |
        v
    MySQL Database
        |
   +----+----+
   |    |    |
   v    v    v
Product Purchase Invoice
 Table    Table    Table
