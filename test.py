from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/form_example',methods=['POST', 'GET'])
def form_example():
   if request.method == 'POST':
     language=request.form.get('language')
     if(language == "telugu"):
        p="తెలుగు"
     elif(language == "hindi"):
        p="हिंदी"
     elif(language == "english"):
        p="English"
     else:
        p="other"
     return '<h1>The language is {}. </h1>'.format(p)
   return '''<form method="POST">
            
            <input type="radio" name="language" value="telugu" checked> telugu<br>
            <input type="radio" name="language" value="hindi"> hindi<br>
            <input type="radio" name="language" value="english"> english<br>

            <input type="submit">
            </form>'''
            #return "hello world"   
		
if __name__ == '__main__':
   app.run(debug = True)
