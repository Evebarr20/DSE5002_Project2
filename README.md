# DSE5002_Project2

Our bank wants a set of functions and classes to clean up access to the database for our data teams and managers.

This project uses the **`bank` database** from *Learning SQL* by Beaulieu.

---

## Project Requirements

---

## 1. Connection Tool (No Hardcoded Passwords)

Create a Python function that connects to the `bank` database using credentials stored in a separate file.

### Vault File Format

The vault file must contain exactly two lines:

Line 1: username  
Line 2: password  

Example:

Pat  
PatPassword  

You must create a PostgreSQL user named **Pat** with access to your PostgreSQL server and the `bank` database.

---

### Function Requirements

Write a function in a single `.py` file that:

- Takes a filename as input
- Opens the file
- Reads the username (first line)
- Reads the password (second line)
- Connects to the `bank` database using those credentials
- Returns the database connection

### Additional Requirements

- Must be written in a single `.py` file
- Must include proper documentation (docstrings)
- Must be run through `pylint` and be as clean as possible

---

## 2. Jupyter Notebook Testing (Connection Function)

Create a Jupyter Notebook to test your connection function.

### Notebook Setup

- Place the `.py` file from Step 1 in the same working directory as the notebook
- Import the function
- Create the vault file in the working directory

### Testing Requirements

- Show that the connection function works by:
  - Creating a connection
  - Loading a table from the `bank` database
- Show what happens if an invalid vault filename is provided

Make sure this section is clearly labeled and documented in your notebook.

---

## 3. Monthly Transaction Function

Create a function that retrieves all transactions for a given month and year.

### Inputs

- Database connection (from Step 1)
- Month
- Year

### Output

- Return a Pandas DataFrame
- Include all transactions for the specified month and year
- Do NOT include the `account_id` column

### Invalid Input Handling

If the month or year is invalid:

- Print a warning message
- Return a DataFrame:
  - With correct column names
  - Containing exactly one row
  - All values in that row should be `-1`

### Additional Requirements

- Must be written in a single `.py` file
- Must include proper documentation
- Must pass `pylint` as cleanly as possible

---

## 4. Test the Transaction Function

In your Jupyter Notebook:

- Import the function from Step 3
- Create a clearly labeled section
- Show that the function works for:
  - Valid month/year
  - Invalid month/year

Your notebook should now contain clearly labeled sections for:

- Connection Function Testing
- Transaction Function Testing

---

## 5. Create a Class

Create a class that stores:

- The vault filename
- The database connection
- The data retrieval functionality

The class must be in a `.py` file in the same working directory as:

- Your Step 1 `.py` file
- Your Step 3 `.py` file
- Your Jupyter Notebook

You will need to import your functions from Steps 1 and 3.

---

### Class Requirements

#### `__init__` Method

The constructor must:

- Take the vault filename as input
- Store the filename in the class
- Use the Step 1 function to:
  - Read credentials
  - Create a database connection
- Store the connection in the class

---

### Method 1: Retrieve Transactions

Create a method that:

- Takes month and year as inputs
- Calls your Step 3 function
- Returns the transaction DataFrame

---

### Method 2: Plot Transactions

Create a method that:

- Takes month and year as inputs
- Retrieves transaction data using your Step 3 function
- Generates a bar plot of transactions by day within that month and year

Note: The dataset is small, so the plot may appear sparse.

---

### Additional Requirements

- Must be written in a single `.py` file
- Must include proper documentation
- Must pass `pylint` as cleanly as possible

---

## 6. Test the Class

In your Jupyter Notebook:

- Create a clearly labeled section for class testing
- Create an instance of the class
- Test:
  - The transaction retrieval method
  - The bar plot method

---

## Deliverables
- A .py file, well documented and clean
- A pdf of the Jupyter notebook showing all the tests
-  A .py file, well documented and clean
-    .py file, well documented and clean
