from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
import report, getassist, Qprocess, Camera
import time, os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
Cam = 0
svr = 0
class_name = ''
confidence_score = 0
issue = ''
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/userdetails', methods=['GET', 'POST'])
def user_details():
    if request.method == 'POST':
        full_name = request.form['full_name']
        age = request.form['age']
        sex = request.form['sex']
        pregnant = request.form.get('pregnant', False)
        if sex == 'female' and pregnant:
            #getassist.pinghelp()
            return "As you're, assistance is on your way"
        elif int(age) < 13 or int(age) > 69:
            #getassist.pinghelp()
            return 'due to your age, assistance is on your way'
        report.new(full_name, age)
        print("Report Generated")
        return redirect(url_for('Q1'))

    return render_template('userdetails.html')
@app.route('/Q1')
def Q1():
 
    return render_template('Q1.html')
@app.route('/Camera')
def CamPage():
    return render_template('Camera.html')
@app.route('/prating')
def pain_ratings():
    return render_template('prating.html')
        
@app.route('/Meds')
def MedQuestion():
    return render_template('QMed.html')

@app.route('/AliG')
def AliGQuestions():
    return render_template('QAliG.html')

@app.route('/Vitals')
def WebVitals():
    return render_template('Vitals.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('Meds')
def MedAnswer(data):
    print("Allergies - ", data)

@socketio.on('AliG')
def MedAnswer(data):
    print("Allergies - ", data)
    
@socketio.on('Rating')
def recived(data):
    print("Recieved Pain rating of " , data)
    
   
@socketio.on('Q1d')
def handle_q1_data(data):
    print("Received data:", data)  # Replace this with your desired handling of the data
    global issue
    global Cam
    global svr
    issue, Cam, svr = Qprocess.Match(data)
    print("Issue - ", issue)
    print("CamStatus - ", Cam)
    print("Severity - ", svr)
    emit(Cam)
    
@socketio.on('request_assistance')
def handle_assistance_request():
    print('Request of assistance received')
    getassist.pinghelp()
    
@socketio.on('take_photo')

def handle_take_photo():
    Camera.take_photo(camera_index=0, file_name='photo.jpg')
    print("Pching")
    # Code to take the photo
    # This could involve calling a function to capture the photo using a camera
    # Once the photo is captured, emit an event to inform the client
    emit('photo_taken')

@socketio.on('process_image')
def handle_process_image():
    directory = ".\\users\\Current_User"
    image_name = "photo.jpg"  # Replace "your_image.jpg" with the name of your saved image file
    image_path = os.path.join(directory, image_name)
    #print("Beep Beep Boop Boop")
    global confidence_score
    global class_name
    class_name, confidence_score = Camera.process_saved_image(image_path)
    print("Determined Class: ", class_name)
    print("Confidence: ", confidence_score)
    # Code to process the saved image
    # This could involve calling a function to analyze the image and extract information
    # Once the image is processed, emit an event to inform the client
    emit('image_processed')
    
@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)
