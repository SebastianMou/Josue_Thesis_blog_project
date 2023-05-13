# Josue_Thesis_blog_project

<!DOCTYPE html>
<html>
<head>
    <title>MyDjangoProject</title>
</head>
<body>
<h1>MyDjangoProject</h1>

<h2>Introduction</h2>

<p>MyDjangoProject is a web application built with Django, a high-level Python Web framework that encourages rapid development and clean, pragmatic design. This README will guide you through setting up your development environment and running the project.</p>

<h2>Prerequisites</h2>

<p>Before you begin, ensure you have met the following requirements:</p>
<ul>
    <li>You have installed Python 3.8 or newer. You can download it from the <a href="https://www.python.org/downloads/">official website</a>.</li>
    <li>You have installed pip. If you installed Python from source, with an installer from python.org, you should already have pip.</li>
    <li>You have a Windows/Linux machine. This guide will provide instructions for both systems.</li>
</ul>

<h2>Setting up MyDjangoProject</h2>

<p>To set up MyDjangoProject, follow these steps:</p>

<h3>Windows/Linux</h3>

<ol>
    <li>Clone the repository:</li>
    <pre><code>git clone https://github.com/yourusername/MyDjangoProject.git</code></pre>
    
    <li>Navigate to the project directory:</li>
    <pre><code>cd MyDjangoProject</code></pre>
    
    <li>If you have an old virtual environment (env) in the project directory, delete it:</li>
    <pre><code>rm -rf env</code></pre>
    
    <li>Create a new virtual environment:</li>
    <p>For Windows:</p>
    <pre><code>python -m venv env</code></pre>
    
    <p>For Linux:</p>
    <pre><code>python3 -m venv env</code></pre>
    
    <li>Activate the virtual environment:</li>
    <p>For Windows:</p>
    <pre><code>.\env\Scripts\activate</code></pre>
    
    <p>For Linux:</p>
    <pre><code>source env/bin/activate</code></pre>
    
    <li>Install the project dependencies:</li>
    <pre><code>pip install -r requirements.txt</code></pre>
</ol>

<h2>Running MyDjangoProject</h2>

<p>To run MyDjangoProject, follow these steps:</p>

<ol>
    <li>Apply the migrations:</li>
    <pre><code>python manage.py migrate</code></pre>
    
    <li>Run the development server:</li>
    <pre><code>python manage.py runserver</code></pre>
    
    <li>Open your web browser and visit <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a></li>
</ol>

<h2>Contact</h2>

<p>If you want to contact me, you can reach me at your_email@your_domain.com.</p>

<h2>License</h2>

<p>This project uses the following license: <a href="link_to_license">license_name</a>.</p>
</body>
</html>
