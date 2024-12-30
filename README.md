# AWS RDS Connect Column Slicing

This project demonstrates how to connect to an AWS RDS database, create and populate a table, and then use Flask to build a web application that integrates an HTML/CSS frontend for column slicing functionality. It allows users to view specific columns from the table based on their selection.

## Features

- **Database Setup**: Connects to an AWS RDS database, creates a table, and inserts values using Jupyter Notebook.
- **Backend**: Flask is used to handle backend operations and serve data from the database.
- **Frontend**: A user-friendly interface built with HTML and CSS, integrated with the Flask backend.
- **Column Slicing**: Allows users to slice specific columns from the table for better data analysis.

## Workflow

1. **Database Setup in Jupyter Notebook**:  
   - Connected to an AWS RDS database.  
   - Created a table and inserted values.  
   - Verified the table structure and data through SQL queries.  

2. **Backend Integration Using Flask**:  
   - Used Flask to retrieve and process data from the AWS RDS database.  
   - Exposed endpoints for the frontend to interact with the database.  

3. **Frontend Development with Flask Integration**:  
   - Developed a dynamic HTML/CSS interface.  
   - Integrated the frontend with Flask to enable column slicing functionality.  


