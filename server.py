from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # HTML template with a full-width div
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Full-Width Div</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
            }
            .full-width-div {
                width: 100%; /* Full width of the viewport */
                background-color: #007bff; /* Blue background */
                color: white; /* White text */
                text-align: center; /* Center-align text */
                padding: 20px; /* Add some space inside */
                box-sizing: border-box; /* Include padding in width calculation */
            }
        </style>
    </head>
    <body>
        <div class="full-width-div">
            <h1>This is a Full-Width Div</h1>
            <p>The div spans the entire width of the viewport.</p>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
