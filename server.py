from flask import Flask, request

app = Flask(__name__)

@app.route('/uploads', methods=['POST'])
def upload_file():
    try:
        uploaded_file = request.files['file']
        if uploaded_file:
            # Save the file to a desired location
            uploaded_file.save("uploads/" + uploaded_file.filename)
            return {'message': 'File uploaded successfully'}, 200
        else:
            return {'error': 'No file uploaded'}, 400
    except Exception as e:
        print('Error processing request:', str(e))
        return {'error': 'An error occurred while processing the request'}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
