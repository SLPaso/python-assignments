def make_get_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"  # Example API
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Response Data:", response.json())
        else:
            print("Failed to fetch data. Status code:", response.status_code)
    except requests.RequestException as e:
        print("An error occurred while making the GET request:", e)

make_get_request()
def make_get_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"  # Example API
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Response Data:", response.json())
        else:
            print("Failed to fetch data. Status code:", response.status_code)
    except requests.RequestException as e:
        print("An error occurred while making the GET request:", e)

make_get_request()
def connect_to_database():
    try:
        # Connect to SQLite database (creates file if it doesn't exist)
        conn = sqlite3.connect("example.db")
        cursor = conn.cursor()

        # Create a table
        cursor.execute("""
def connect_to_database():
    try:
        # Connect to SQLite database (creates file if it doesn't exist)
        conn = sqlite3.connect("example.db")
        cursor = conn.cursor()

        # Create a table
        cursor.execute("""
        conn.commit()
        cursor.execute("SELECT * FROM users")
        print("Users:", cursor.fetchall())

    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        # Close connection
        conn.close()

connect_to_database()
