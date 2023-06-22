from flask import Flask, request, render_template
from supabase import create_client, Client
from key import Key
import os
from random import randint

app = Flask(__name__)

supabse_url: str = "https://zfxsfzyrdtxdzoaqgkxp.supabase.co"
supabase_key: str = Key

supabase: Client = create_client(supabse_url, supabase_key)

bucket_name : str = "IVP4"


@app.route('/')
def render():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
    
        file = request.files['image']

        
        image_name = f"{file.filename}_temporary_image{randint(1, 100)}.jpg"
        image_path = f"./temporary_image/{image_name}"
        print("image name: ", image_name)
        print("image path: ", image_path)
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        
        f = open(f"{image_path}", "wb")        
        print("File: ", f)
        f.write(file.read())
        print("File: ", f)
        
        image_data = open(image_path, 'rb').read()
        
        response = supabase.storage.from_(bucket_name).upload(image_name, image_data)

        print("response: ", response)
        
        os.remove(f"{image_path}")
        os.rmdir("./temporary_image/")
            
        print({'success': 'Image uploaded successfully'})
        return render_template('index.html', erro='Image uploaded successfully')
    
    except Exception as e:
        print({'error': str(e)})
        return render_template('index.html', erro=str(e))

if __name__ == '__main__':
    app.run(debug=True)