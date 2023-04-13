from main import dash_app
from routes import render_page_content



if __name__ == '__main__':
    dash_app.run_server( host='localhost', port= '1111', debug=True ) 