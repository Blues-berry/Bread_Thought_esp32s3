#!/usr/bin/env python3
import os
from flask import Flask, request

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
UPLOAD_FOLDER = '/Users/shorpen/编程/landingpage-doromon/backend/voice'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/voice', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        print('Failed to receive audio file: No audio file provided')
        return 'No audio file provided', 400
    audio_file = request.files['audio']
    if audio_file.filename == '':
        print('Failed to receive audio file: No selected file')
        return 'No selected file', 400
    if audio_file:
        import itertools
        assfilename = itertools.count(0)
        exfilename = 'recoder'
        while True:
            filename = f'{exfilename}{next(assfilename)}.wav'
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            if not os.path.exists(file_path):
                audio_file.save(file_path)
                print(f'Successfully received and saved audio file: {filename}')
                return 'File uploaded successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)