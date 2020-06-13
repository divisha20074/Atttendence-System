from flask import *
from flaskext.mysql import MySQL
import datetime as dd
import time as tt
# from wtforms import Form, StringField, TextAreaField, validators
app = Flask(__name__)
app.secret_key = 'developerbrains'

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'face_recog'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



@app.route('/attendance')
def attendance():
    if 'email' in session:
        return render_template('attendance.html')
        # return render_template('index.html')
    else:
        return "Not Allowed <a href='/'>Home</a>"


@app.route('/loginstatus')
def loginstatus():
    return render_template('login-status.html')


@app.route('/signupstatus')
def signupstatus():
    return render_template('signupstatus.html')


@app.route('/notification')
def notify():
    return render_template('notification.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-face')
def face():
    return render_template('add-face.html')


@app.route('/myface', methods=['POST'])
def myface():
    if request.method == "POST":
        # importing modules
        import os
        import cv2
        face1 = request.form
        student_id = face1['id']
        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * from account where id_number=%s", (student_id))
        results = cursor.fetchone()
        if str(results[7]) == '1':
            return 'Already Registered...'

        else:
            # Directory
            directory = student_id

            # Parent Directory path
            parent_dir = "dataset/"

            # Path
            path = os.path.join(parent_dir, directory)

            os.mkdir(path)
            print("Directory '% s' created" % directory)

            # starting video cam
            vid_cam = cv2.VideoCapture(0)

            # detecting face using haarcascade
            face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            # initial count
            count = 0

            # looping
            while True:

                # capture image from video
                ret, img_frame = vid_cam.read()

                # now converting image into gray scale image
                gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)

                # detecting face rectangle in frame
                face = face_detector.detectMultiScale(gray, 1.3, 6)

                # loop for each face
                for (x, y, w, h) in face:
                    # cropping image frame into face rectangle
                    cv2.rectangle(img_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    img = gray[y:y + h, x:x + w]
                    count += 1

                    # saving the capture face rectangle

                    cv2.imwrite(os.path.join(path, "" + str(count) + ".jpg"), img)

                    # create a on screen counter  to show no of face captured
                    cv2.putText(img_frame, str(count), (30, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 1)
                    # cv2.putText(img_frame, str(student_id), (40, 40), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 1)

                    # show frame with rectangle on face
                    cv2.imshow("capturing frame", img_frame)

                if count == 100:
                    print("capture complete")
                    break
                elif cv2.waitKey(1) & 0xff == ord('q'):
                    break

            conn = mysql.connect()
            cursor = conn.cursor()

            # cursor.execute("SELECT * from todotask where id=2")
            cursor.execute("UPDATE face_recog.account set status='1' where id_number=%s", (student_id))
            # data = cursor.fetchone()
            conn.commit()
            # session['email'] = email
            # session.pop('email', None)
            # Close connection
            cursor.close()
            conn.close()

            # stop video
            vid_cam.release()

            # close all win
            cv2.destroyAllWindows()
    return render_template('data-status.html')


@app.route('/train')
def trains():
    return render_template('train.html')


@app.route('/starttrain', methods=['POST'])
def starttrain():
    if request.method == "POST":
        import cv2
        import os
        import numpy as np
        from PIL import Image
        import pickle

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(BASE_DIR, "dataset")  # opening the dataset directory where the training set is stored

        recognizer = cv2.face.LBPHFaceRecognizer_create()

        current_id = 0
        label_ids = {}  # dictionary
        y_labels = []  # intialize with empty list
        x_train = []

        for root, dirs, files in os.walk(image_dir):
            for file in files:
                if file.endswith("jpg"):
                    path = os.path.join(root, file)
                    label = os.path.basename(root)
                    if not label in label_ids:
                        label_ids[label] = current_id
                        current_id += 1
                        id_ = label_ids[label]
                        print(label_ids)
                        pil_image = Image.open(path)
                        image_array = np.array(pil_image, "uint8")
                        x_train.append(image_array)
                        y_labels.append(id_)

        with open("labels.pickle", 'wb') as f:
            pickle.dump(label_ids, f)

        recognizer.train(x_train, np.array(y_labels))
        recognizer.save("face-trainner.yml")
    return "your data has been trained successfully"


@app.route('/recogniser')
def recogniser():
    return render_template('recogniser.html')


@app.route('/recognise', methods=['POST'])
def recognise():
    if request.method == "POST":
        import numpy as np
        import cv2
        import pickle

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("face-trainner.yml")

        labels = {"person_name": 1}  # load label from pickle

        with open("labels.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v: k for k, v in og_labels.items()}  # inverting the key value pairs

        cap = cv2.VideoCapture(0)

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
                # roi_color = frame[y:y + h, x:x + w]
                # cv2.rectangle(faces, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id_, conf = recognizer.predict(roi_gray)
                if conf >= 70 and conf <= 80:
                    p = 0
                    if labels[id_]:
                        p = 1
                        if p == 1:
                            session['level'] = labels[id_]
                            levels = session['level']
                            conn = mysql.connect()
                            cursor = conn.cursor()
                            date1 = dd.date.today()
                            mydate = str(date1)
                            time1 = tt.localtime()
                            time1 = tt.strftime("%H:%M:%S", time1)
                            cursor.execute("SELECT * from registration where id_number=%s and date1 = %s", (levels, mydate))
                            results = cursor.fetchone()

                            if cursor.rowcount > 0:
                                return render_template('notification.html', levels="Attendance already marked as "+ levels)
                            else:
                                cursor.execute("INSERT INTO registration(id_number, time1, date1) VALUES(%s, %s, %s)", (levels, time1, date1))
                                conn.commit()
                                cursor.close()
                                conn.close()
                                return render_template('notification.html', levels="Attendance has been Marked as " + levels)
                                # return render_template('index.html', levels=levels)
                            p += 1

                    # level = labels[id_]
                    # session['level'] = level
                    # level = session['level']
                    # render_template('index.html', level=level)

                    # this is the id no. of the student detected. This result has to be entered in spreadsheet
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    name = labels[id_]
                    color = (255, 255, 255)
                    stroke = 2
                    cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

                color = (255, 0, 0)  # BGR
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

            cv2.imshow('frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        return 'Recognition stopped'


@app.route('/login')
def login():
    if 'email' in session:
        return redirect(url_for('index'))
        # return render_template('index.html')
    else:
        return render_template('login.html')



@app.route('/registration')
def registration():
    if 'email' in session:
        return redirect(url_for('index'))
        # return render_template('index.html')
    else:
        return render_template('registration.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('email', None)
    return redirect(url_for('index'))


# registration form
@app.route('/registration', methods=['POST'])
def regi():
    if request.method == "POST":
        regi1 = request.form
        name = regi1['signname']
        id_num = regi1['id_number']
        email = regi1['signemail']
        phone = regi1['signphone']
        password = regi1['signpass']
        confirmpassword = regi1['signpass1']

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * from account where id_number = %s", (id_num,))
        data = cursor.fetchone()
        # count = cursor.rowcount
        if cursor.rowcount > 0:
            return render_template('signupstatus.html', status="Account Already Exists. Failed to Register.")

        elif password != confirmpassword:
            return render_template('signupstatus.html', status="Opps!!! password didn't match. Failed to Register.")
        else:
            # cursor.execute("SELECT * from todotask where id=2")
            cursor.execute("INSERT INTO account(name, id_number, email, phone, password,type) VALUES(%s, %s,%s, %s, %s, %s)", (name, id_num, email, phone, password,'0'))
            # data = cursor.fetchone()
            conn.commit()
            # session['email'] = email
            # session.pop('email', None)
            # Close connection
            cursor.close()
            conn.close()
            # return redirect(url_for('add'))
            return render_template('signupstatus.html', status="Registration Successful")


# login form
@app.route('/login', methods=['POST'])
def log():
    if request.method == "POST":
        login1 = request.form
        email = login1['logemail']
        password = login1['logpass']

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * from account where email=%s and password = %s", (email, password))
        # records = cursor.fetchall()
        # cursor.execute("INSERT INTO account(name) VALUES(%s)", (name)
        results = cursor.fetchone()
        if cursor.rowcount > 0:
            if str(results[6]) == '1':
                email1 = str(results[3])
                session['email'] = email1
                email1 = session['email']
                return render_template('index.html', level="Hi! " + email1)
            else:
                return render_template('login-status.html', level="Sorry!!! Student's Login System is Not Available.")
        else:
            return render_template('login-status.html')
        cursor.close()
        conn.close()

        # conn.commit():
        # fetchmany () or fetchall ()
        # session['email'] = email
        # session.pop('email', None)
        # Close connection

        # return redirect(url_for('add'))
        # return "Logged in"


# login using face-recognition
@app.route('/facelogin', methods=['POST'])
def facelogin():
    if request.method == "POST":
        import numpy as np
        import cv2
        import pickle

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("face-trainner.yml")

        labels = {"person_name": 1}  # load label from pickle

        with open("labels.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v: k for k, v in og_labels.items()}  # inverting the key value pairs

        cap = cv2.VideoCapture(0)

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
                # roi_color = frame[y:y + h, x:x + w]
                # cv2.rectangle(faces, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id_, conf = recognizer.predict(roi_gray)
                if conf >= 70 and conf <= 80:
                    p = 0
                    if labels[id_]:
                        p = 1
                        if p == 1:
                            session['level'] = labels[id_]
                            levels = session['level']
                            conn = mysql.connect()
                            cursor = conn.cursor()
                            date1 = dd.date.today()
                            mydate = str(date1)
                            time1 = tt.localtime()
                            time1 = tt.strftime("%H:%M:%S", time1)
                            cursor.execute("SELECT * from account where id_number=%s", (levels))
                            results = cursor.fetchone()
                            if cursor.rowcount > 0:
                                if str(results[6]) == '1':
                                    email1 = str(results[3])
                                    session['email'] = email1
                                    email1 = session['email']

                                    return render_template('index.html', level="Hi! " + email1)
                                else:
                                    return render_template('login-status.html',
                                                           level="Sorry!!! Student's Login System is Not Available.")
                            p += 1

                    font = cv2.FONT_HERSHEY_SIMPLEX
                    name = labels[id_]
                    color = (255, 255, 255)
                    stroke = 2
                    cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

                color = (255, 0, 0)  # BGR
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

            cv2.imshow('frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        return 'Recognition stopped'

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * from account where email=%s and password = %s", (email, password))
        # records = cursor.fetchall()
        # cursor.execute("INSERT INTO account(name) VALUES(%s)", (name)
        results = cursor.fetchone()
        if cursor.rowcount > 0:
            if str(results[6]) == '1':
                email1 = str(results[3])
                session['email'] = email1
                email1 = session['email']
                return render_template('index.html', level="Hi! " + email1)
            else:
                return render_template('login-status.html', level="Sorry!!! Student's Login System is Not Available.")
        else:
            return render_template('login-status.html')
        cursor.close()
        conn.close()

        # conn.commit():
        # fetchmany () or fetchall ()
        # session['email'] = email
        # session.pop('email', None)
        # Close connection

        # return redirect(url_for('add'))
        # return "Logged in"


# attendance
@app.route('/attend', methods=['POST'])
def attend():
    if request.method == "POST":
        date1 = dd.date.today()
        mydate = str(date1)

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * from account,registration where (registration.date1=%s) and (account.id_number=registration.id_number) and (registration.id_number!='00000') and (registration.id_number between 53000 and 53999)", (mydate))
        results = cursor.fetchall()
        if cursor.rowcount > 0:
            return render_template('attendance.html', level=results)
        cursor.close()
        conn.close()


@app.route('/second', methods=['POST'])
def second():
    if request.method == "POST":
        date1 = dd.date.today()
        mydate = str(date1)

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * from account,registration where (registration.date1=%s) and (account.id_number=registration.id_number) and (registration.id_number!='00000') and (registration.id_number between 52000 and 52999)", (mydate))
        results = cursor.fetchall()
        if cursor.rowcount > 0:
            return render_template('attendance.html', level=results)
        cursor.close()
        conn.close()


@app.route('/third', methods=['POST'])
def third():
    if request.method == "POST":
        date1 = dd.date.today()
        mydate = str(date1)

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * from account,registration where (registration.date1=%s) and (account.id_number=registration.id_number) and (registration.id_number!='00000') and (registration.id_number between 51000 and 51999)", (mydate))
        results = cursor.fetchall()
        # account.id_number=registration.id_number and
        if cursor.rowcount > 0:
            return render_template('attendance.html', level=results)
        cursor.close()
        conn.close()


@app.route('/final', methods=['POST'])
def final():
    if request.method == "POST":
        date1 = dd.date.today()
        mydate = str(date1)

        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * from account,registration where (registration.date1=%s) and (account.id_number=registration.id_number) and (registration.id_number!='00000') and (registration.id_number between 50000 and 50999)", (mydate))
        results = cursor.fetchall()
        if cursor.rowcount > 0:
            return render_template('attendance.html', level=results)
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)