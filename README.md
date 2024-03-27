# Electronic Component Management System
Electronic Component Management System implemented using Flask, SQLite for the database, and HTML for the front-end :

HTML Templates (index.html, edit_component.html):

index.html: This is the main page of your application where users can view all the electronic components in a table format. It has a form to add new components and displays existing components in a table.
edit_component.html: This page allows users to edit existing components. It contains a form with fields pre-filled with the component's current data, allowing users to make changes and save them.
CSS Styling:

Both HTML files have CSS styles embedded to provide a visually appealing and user-friendly interface. Styles are applied to headings, tables, form elements, buttons, and links to improve the overall look and feel of the application.
Flask Backend (app.py):

Flask: Flask is used as the web framework to handle HTTP requests, routing, and rendering HTML templates.
SQLite Database: SQLite is used to store and manage electronic component data.
create_table: This function creates the SQLite table components if it doesn't already exist, defining the schema for storing component information.
@app.route('/'): This route renders the main page (index.html) and fetches all components from the database to display in the table.
@app.route('/add_component', methods=['POST', 'GET']) and @app.route('/edit/<int:component_id>', methods=['POST', 'GET']): These routes handle both adding new components and editing existing components. They capture form data, validate it, and interact with the SQLite database to insert new records or update existing ones.
@app.route('/delete/<int:component_id>', methods=['GET']): This route handles component deletion by accepting a component ID and deleting the corresponding record from the database.
if _name_ == '_main_':: This block ensures that the create_table function is called when the script is run directly, and it starts the Flask application with debugging enabled.
Functionality:

Users can view all components, add new components, edit existing components, and delete components through the web interface.
Data entered in the forms is validated on the server-side (Flask) to ensure correctness before being saved or updated in the database.
Components are displayed in a tabular format on the main page, making it easy for users to view and manage them.
Overall, your project provides a basic but functional Electronic Component Management System with CRUD (Create, Read, Update, Delete) operations implemented using Flask and SQLite. Users can interact with the system through a web browser to manage electronic components effectively.
