# Main application run script that imports the msrwebhook app.

from msrwebhook import app

if __name__ == '__main__':
    app.run(debug=True)
