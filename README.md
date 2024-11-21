## Expense Manager API

### Setup
1. Clone the repository
2. Create a .env file in the expense_manager directory:
```bash
touch .env
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Apply migrations:
```bash
python manage.py migrate
```
4. Run the development server:
```bash
python manage.py runserver
```

### Endpoints
- **Users**
- `GET /api/users/`: List all users.
- `POST /api/users/`: Create a new user.
- **Expenses**
- `GET /api/expenses/`: List all expenses.
- `POST /api/expenses/`: Create a new expense.
- `GET /api/expenses/list_by_date_range/?user_id=&start_date=&end_date=`: List expenses by date range.
- `GET /api/expenses/category_summary/?user_id=&month=`: Get total expenses per category for a month.
