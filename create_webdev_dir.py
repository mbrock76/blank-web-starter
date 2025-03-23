import os

# Define the directory structure
directories = [
    "css",
    "img",
    "scripts"
]

# Create the base directory
def create_directory_structure():
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

# Create the index.html file
def create_index_html():
    index_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Web Project</title>
    <link rel="stylesheet" href="css/hrz.css">
    <script src="scripts/rename.js"></script>
</head>
<body onload="init()">

</body>
</html>
'''
    with open("index.html", "w") as f:
        f.write(index_content)

# Create CSS files
def create_css_files():
    with open("css/hrz.css", "w") as f:
        f.write("/* Horizontal styles go here */\n")

    with open("css/vrt.css", "w") as f:
        f.write("/* Vertical styles go here */\n")

# Create rename.js file
def create_rename_js():
    js_content = '''function init(){

    // --VARIABLES--

    //  --LISTENERS--

    //  --FUNCTIONS--

}
'''
    with open("scripts/rename.js", "w") as f:
        f.write(js_content)

# Create db_conn.php file
def create_db_conn_php():
    php_content = '''<?php

// Database connection parameters
$servername = "";
$username = "";
$password = "";
$dbname = "";

// Create a database connection
$conn = new mysqli($servername, $username, $password, $dbname);
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

?>
'''
    with open("scripts/db_conn.php", "w") as f:
        f.write(php_content)

# Run the functions
if __name__ == "__main__":
    create_directory_structure()
    create_index_html()
    create_css_files()
    create_rename_js()
    create_db_conn_php()

    print("Project structure and files created successfully!")
