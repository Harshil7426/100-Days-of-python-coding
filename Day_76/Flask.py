from flask import Flask

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def portfolio():
  page = f"""<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>My Portfolio</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>

  <h1>Harshils's Portfolio</h1>
  <h2>Day 56 Solution</h2>
  <p>So, day 56 was all about using csv reading and file and folder manipulation to make 100 files in dozens of folders.
    This was tricky because the names of the folders and files were based on the top 100 streaming songs and so weren't
    simple to encode.</p>
  <a href="https://replit.com/@DavidAtReplit/Day-056-Solution#main.py"><img src="images/56.png" width="500px"></a>
  <br>
<a href="/linktree">Linktree</a>
  <script src="script.js"></script>

</body>

</html>"""

  return page



@app.route('/linktree')  # Creates the path to the home page
def linktree():
    a = 20  # Subroutine to create the home page
    # Three quotes followed by the html for the baldies site. Three more quotes to close. All the HTML is assigned to the 'page' variable
    page = f"""<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <img src="" alt="My pic">
  <h1 align="center"> Harshil Amin</h1>
  <h3 align="center">Student at NMIMS</h3>
  <p>
    I am a student at NMIMS. <br>
    <a href="https://replit.com/@HarshilAmin1">My Journey</a>
  </p>
  
  <script src="script.js"></script>

</body>

</html>
  """

    return page  # returns the contents of the page variable


app.run(host='0.0.0.0', port=81)
