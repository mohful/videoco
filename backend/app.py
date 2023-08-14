from flask import Flask
import os
import sys
import traceback

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    try:
        return "This is the VideoCo backend"
    except:
        print(str(traceback.format_exc()), file=sys.stderr)
        return "Failed", 500
    
if __name__ == "__main__":
    app.run(debug=True)