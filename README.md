1. set venv
2. activate venv
3. pip install requirements.txt
4. python.exe .\sobes\manage.py makemigrations
5. python.exe .\sobes\manage.py migrate

6. python.exe .sobes\manage.py runserver


http://127.0.0.1:8000/all_accounts - get all payments accounts and post new payment account
http://127.0.0.1:8000/account/<int:id> - get payment account by id and post new payment account
http://127.0.0.1:8000/all_transactions - get transactions and post new transaction
