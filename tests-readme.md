# Pizza Store Application - Test Cases and Results

## Overview
This document outlines the test cases and results for the Pizza Store Application. The tests cover all major functionality including inventory management, recipe management, menu management, side item management, and order processing.


## Test Categories

### 1. Inventory Management

#### Test Case 1.1: Add New Ingredient
**Description:** Add a new ingredient to the inventory  
**Steps:**
1. Navigate to Inventory Management
2. Select "Add Ingredient"
3. Enter ingredient details:
   - Name: "Mozzarella"
   - Quantity: 50
   - Unit: "kg"
   - Reorder Level: 10

**Expected Outcome:**
- Ingredient successfully added to inventory
- Success message displayed
- Ingredient visible in inventory list

**Actual Outcome:**
- Ingredient added successfully
- "Successfully added Mozzarella to inventory" message displayed
- Ingredient appears in inventory list with correct details

#### Test Case 1.2: Update Existing Ingredient Quantity
**Description:** Add quantity to an existing ingredient  
**Steps:**
1. Navigate to Inventory Management
2. Select "Add Ingredient"
3. Enter same ingredient name with additional quantity:
   - Name: "Mozzarella"
   - Quantity: 25
   - Unit: "kg"
   - Reorder Level: 10

**Expected Outcome:**
- Existing ingredient quantity updated (75 kg total)
- Update message displayed

**Actual Outcome:**
- Quantity updated successfully
- "Updated quantity of Mozzarella. New quantity: 75 kg" message displayed

#### Test Case 1.3: Check Reorder Levels
**Description:** Verify reorder level alerts  
**Steps:**
1. Navigate to Inventory Management
2. Remove ingredients until below reorder level
3. Select "Check Reorder Levels"

**Expected Outcome:**
- List of ingredients below reorder level displayed
- Each low ingredient shows current quantity and reorder level

**Actual Outcome:**
-  Low stock alerts displayed correctly
-  Shows correct quantities and reorder levels
-  Only displays items below reorder threshold

### 2. Recipe Management

#### Test Case 2.1: Create New Recipe
**Description:** Create a new pizza recipe  
**Steps:**
1. Navigate to Recipe Management
2. Select "Add Recipe"
3. Enter recipe details:
   - Name: "Margherita"
   - Add ingredients:
     * Dough: 0.5 kg
     * Tomato Sauce: 0.2 L
     * Mozzarella: 0.3 kg

**Expected Outcome:**
- Recipe created successfully
- All ingredients properly associated
- Recipe visible in recipe list

**Actual Outcome:**
-  Recipe created with all ingredients
-  Success message displayed
-  Recipe appears in recipe list with correct ingredients

#### Test Case 2.2: Search Recipe
**Description:** Search for existing recipe  
**Steps:**
1. Select "Search Recipes" from main menu
2. Enter search term: "Marghe"

**Expected Outcome:**
- Margherita recipe displayed in results
- All recipe details visible

**Actual Outcome:**
-  Recipe found successfully
-  All recipe details displayed correctly
-  Partial name search working as expected

### 3. Menu Management

#### Test Case 3.1: Add Menu Item
**Description:** Add a new pizza to the menu  
**Steps:**
1. Navigate to Menu Management
2. Select "Add Menu Item"
3. Enter menu item details:
   - Name: "Classic Margherita"
   - Description: "Traditional Italian pizza"
   - Size: MEDIUM
   - Price: 12.99
   - Category: VEGETARIAN
   - Recipe: "Margherita"

**Expected Outcome:**
- Menu item created successfully
- All details saved correctly
- Item visible in menu list

**Actual Outcome:**
-  Menu item created with all details
-  Success message displayed
-  Item appears in menu with correct information

#### Test Case 3.2: View Menu Items by Category
**Description:** Filter menu items by category  
**Steps:**
1. Navigate to Menu Management
2. Select "View Menu Items by Category"
3. Choose category: VEGETARIAN

**Expected Outcome:**
- Only vegetarian pizzas displayed
- All details for each pizza visible

**Actual Outcome:**
-  Correct filtering by category
-  All vegetarian pizzas listed
-  Complete details shown for each item

### 4. Side Item Management

#### Test Case 4.1: Add Side Item
**Description:** Add a new side dish to the menu  
**Steps:**
1. Navigate to Side Item Management
2. Select "Add Side Item"
3. Enter side item details:
   - Name: "Caesar Salad"
   - Description: "Fresh romaine lettuce with caesar dressing"
   - Price: 6.99
   - Category: SALAD

**Expected Outcome:**
- Side item created successfully
- All details saved correctly
- Item visible in sides list

**Actual Outcome:**
-  Side item created with all details
-  Success message displayed
-  Item appears in sides menu

### 5. Order Processing

#### Test Case 5.1: Create Standard Pizza Order
**Description:** Create an order with menu pizza  
**Steps:**
1. Navigate to Order Management
2. Select "Create New Order"
3. Enter order details:
   - Customer: "John Doe"
   - Phone: "555-0123"
   - Delivery Time: (current time + 1 hour)
4. Add menu pizza:
   - Select "Classic Margherita"
   - Quantity: 1

**Expected Outcome:**
- Order created successfully
- Order ID generated (UUID)
- Kitchen slip generated
- Correct total price calculated

**Actual Outcome:**
-  Order created with unique UUID
-  Kitchen slip shows all order details
-  Total price calculated correctly
-  Order status set to NEW

#### Test Case 5.2: Create Custom Pizza Order
**Description:** Create an order with custom pizza  
**Steps:**
1. Navigate to Order Management
2. Select "Create New Order"
3. Enter customer details
4. Choose "Add Custom Pizza"
5. Select toppings:
   - Pepperoni (x2)
   - Extra Cheese
   - Mushrooms

**Expected Outcome:**
- Custom pizza created with selected toppings
- Correct price calculation (base price + toppings)
- Order created successfully

**Actual Outcome:**
-  Custom pizza created correctly
-  Toppings added with quantities
-  Price calculated correctly ($14.00 + $1.75 per topping quantity)
-  Order details saved properly

#### Test Case 5.3: Update Order Status
**Description:** Change order status  
**Steps:**
1. Navigate to Order Management
2. Select "Update Order Status"
3. Enter order ID
4. Change status to PREPARING

**Expected Outcome:**
- Order status updated successfully
- New status reflected in order details

**Actual Outcome:**
-  Status updated correctly
-  Change reflected immediately
-  Success message displayed