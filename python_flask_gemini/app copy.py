from flask import Flask,request,jsonify
import google.generativeai as genai
app = Flask(__name__)

@app.route('/api',methods = ['GET'])
def returnascii():
    d={}
    inputstr = str(request.args['query'])
    # answer = str(ord(intputchr))
    lst=inputstr.split(',',1)
    del lst[0]
    d["output1"]=lst
    def model(s):
        genai.configure(api_key="AIzaSyB1OICYjUzxVZIrkO7texsBGw-ZeK-4K_s")
        generation_config = {
        "temperature": 0,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
        }
        
        safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        ]

        model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                    generation_config=generation_config,
                                    safety_settings=safety_settings)


        prompt_parts = [
        "Make a tour plan for these places in Chennai, the plan must be optimized based on the minimum distance and time to travel, the best time to visit, and the entry fee with an exact time slot. give results in table formate each day separately.Within no of days"+s
        ]

        response = model.generate_content(prompt_parts)

        d['output'] = response.text
    model(inputstr)
    return jsonify(d)
if __name__ == '__main__':
    app.run()