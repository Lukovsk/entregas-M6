from flask import Flask, request, render_template
from supabase import create_client, Client
from key import Key
import os
from random import randint

app = Flask(__name__)

supabse_url: str = "https://zfxsfzyrdtxdzoaqgkxp.supabase.co"
supabase_key: str = Key

supabase: Client = create_client(supabse_url, supabase_key)

bucket_name : str = "IPV4"


@app.route('/')
def render():
    return render_template('index.html')

@app.post('/upload')
def upload():
    try:
    
        file = request.files['image']

        
        image_name = f"temporary_image{randint(1, 100)}.jpg"
        image_path = f"./temporary_image/{image_name}"
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        
        f = open(f"{image_path}", "wb")
        f.write(file.read())
        
        response = supabase.storage.bucket(bucket_name).upload(image_path, image_name)

        print(response)
        
        os.rmdir("./temporary_image")
            
        return {'success': 'Image uploaded successfully'}
    
    except Exception as e:
        print({'error': str(e)})
        return render_template('index.html', erro=str(e))

if __name__ == '__main__':
    app.run(debug=True, reload=True)