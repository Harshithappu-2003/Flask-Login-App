# database.py

# Dummy database (You can replace this with an actual database connection)
users_db = {}

def find_user(email, password=None):
    """Check if the user exists. If password is provided, check credentials."""
    if email in users_db:
        if password:  # If password is provided, check if it matches
            return users_db[email]['password'] == password
        return True  # User exists
    return False

def add_user(name, email, password):
    """Add a new user to the database."""
    users_db[email] = {'name': name, 'password': password}
    print(f"User {name} added successfully!")
