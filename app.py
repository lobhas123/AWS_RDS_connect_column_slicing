from flask import Flask, request, render_template
import psycopg2
import pandas as pd

app = Flask(__name__)

# Function to fetch data from PostgreSQL
def fetch_data_from_postgres():
    conn = psycopg2.connect(
        host="database-2.ctaoq2syig0k.eu-north-1.rds.amazonaws.com",
        database="HDFC_db",
        user="postgres",
        password="lobhas12345"
    )
    query = "SELECT * FROM Task1"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Default route (GET): Show full table with all columns
@app.route("/", methods=["GET"])
def home():
    df = fetch_data_from_postgres()
    columns = df.columns.tolist()  # Get all column names
    data = df.to_dict(orient="records")  # Convert DataFrame to dictionary for rendering
    return render_template("index.html", data=data, columns=columns, selected_columns=columns)

# Filter route (POST): Show table with selected columns
@app.route("/filter", methods=["POST"])
def filter_columns():
    # Get selected columns from the form
    selected_columns = request.form.getlist("columns")

    # Fetch all data from the database
    df = fetch_data_from_postgres()

    # If no columns are selected, show all columns
    if not selected_columns:
        selected_columns = df.columns.tolist()

    # Filter the DataFrame to show only the selected columns
    filtered_df = df[selected_columns]

    # Convert filtered DataFrame to dictionary for rendering
    data = filtered_df.to_dict(orient="records")
    columns = df.columns.tolist()  # Keep all column names for the dropdown
    return render_template("index.html", data=data, columns=columns, selected_columns=selected_columns)

if __name__ == "__main__":
    app.run(debug=True)
