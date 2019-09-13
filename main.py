from flask import Flask,render_template,request,session,url_for,redirect,flash
import sqlite3
import os
import glob
#import magic
import urllib.request
from upload_config import app
from werkzeug.utils import secure_filename


# to decide who is in session
x = 0

app.secret_key = os.urandom(24)


@app.route('/')
def first():
    return render_template('Home_Page.html')


@app.route('/submit')
def submit():
    return render_template('login.html')


@app.route('/logout')
def logout():
    if 'py' in session:
        session.pop('py')
        return render_template('Home_Page.html')
    else:
        return render_template('login.html')


@app.route('/std_login',methods=['POST'])
def log():
    if 'py' in session and x == 1:
        con = sqlite3.connect('User_Data.db')
        cursor = con.cursor()
        data = cursor.execute('select * from USERS where Email=(?)', [session['py']])
        data = list(data)
        return render_template('Student_Landing_Page.html', email=session['py'], name=data[0][0])
    else:
        return render_template('login.html')


@app.route('/fac_login', methods=['POST'])
def log_1():
    if 'py' in session and x == 2:
        con = sqlite3.connect('User_Data.db')
        cursor = con.cursor()
        data = cursor.execute('select * from USERS where Email=(?)', [session['py']])
        data = list(data)
        return render_template('Faculty_Landing_Page.html', email=session['py'], name=data[0][0])
    else:
        return render_template('login.html')


@app.route('/faculty_landing_page')
def fourth_1():
    return render_template('Faculty_Landing_Page.html')


@app.route('/student_landing_page')
def fourth_2():
    return render_template('Student_Landing_Page.html')


@app.route('/image_gallery')
def fifth():
    return render_template('Home_Page_Images.html')


@app.route('/image_gallery_2')
def sixth():
    return render_template('b_tech_img.html')


@app.route('/image_gallery_3')
def seventh():
    return render_template('Diploma_img.html')


@app.route('/image_gallery_4')
def eighth():
    return render_template('b_sc_agriculture_img.html')


@app.route('/image_gallery_5')
def nineth():
    return render_template('bba_img.html')


@app.route('/image_gallery_6')
def tenth():
    return render_template('b_pharma_img.html')


@app.route('/image_gallery_7')
def eleventh():
    return render_template('m_tech_img.html')


@app.route('/image_gallery_8')
def twelveth():
    return render_template('mba_img.html')


@app.route('/image_gallery_9')
def thirteenth():
    return render_template('events_img.html')


@app.route('/image_gallery_10')
def fourteenth():
    image = []
    gallery_image = glob.glob('static/uploads/B.tech/1_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('b_tech_1_img.html',filename=image)


@app.route('/image_gallery_11')
def fifteenth():
    image = []
    gallery_image = glob.glob('static/uploads/B.tech/2_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('b_tech_2_img.html', filename=image)


@app.route('/image_gallery_12')
def sixteenth():
    image = []
    gallery_image = glob.glob('static/uploads/B.tech/3_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('b_tech_3_img.html', filename=image)


@app.route('/image_gallery_13')
def seventeenth():
    image = []
    gallery_image = glob.glob('static/uploads/B.tech/4_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('b_tech_4_img.html', filename=image)


@app.route('/image_gallery_14')
def eighteenth():
    image = []
    gallery_image = glob.glob('static/uploads/B.tech/5_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('b_tech_alm_img.html', filename=image)


@app.route('/image_gallery_15')
def nineteenth():
    image = []
    gallery_image = glob.glob('static/uploads/BBA/1_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('bba_1_img.html', filename=image)


@app.route('/image_gallery_16')
def twenty():
    image = []
    gallery_image = glob.glob('static/uploads/BBA/2_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('bba_2_img.html', filename=image)


@app.route('/image_gallery_17')
def twenty_one():
    image = []
    gallery_image = glob.glob('static/uploads/BBA/3_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('bba_3_img.html', filename=image)


@app.route('/image_gallery_18')
def twenty_two():
    image = []
    gallery_image = glob.glob('static/uploads/BBA/4_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('bba_alm_img.html', filename=image)


@app.route('/image_gallery_19')
def twenty_three():
    image = []
    gallery_image = glob.glob('static/uploads/B.pharma/1_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('bp_1_img.html', filename=image)


@app.route('/image_gallery_20')
def twenty_four():
    image = []
    gallery_image = glob.glob('static/uploads/B.pharma/2_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('bp_2_img.html', filename=image)


@app.route('/image_gallery_21')
def twenty_five():
    image = []
    gallery_image = glob.glob('static/uploads/B.pharma/3_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('bp_3_img.html', filename=image)


@app.route('/image_gallery_22')
def twenty_six():
    image = []
    gallery_image = glob.glob('static/uploads/B.pharma/4_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('bp_4_img.html', filename=image)


@app.route('/image_gallery_23')
def twenty_seven():
    image = []
    gallery_image = glob.glob('static/uploads/B.pharma/5_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('bp_alm_img.html', filename=image)


@app.route('/image_gallery_24')
def twenty_eight():
    image = []
    gallery_image = glob.glob('static/uploads/B.sc_Agri/1_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('bsc_1_img.html', filename=image)


@app.route('/image_gallery_25')
def twenty_nine():
    image = []
    gallery_image = glob.glob('static/uploads/B.sc_Agri/2_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('bsc_2_img.html', filename=image)


@app.route('/image_gallery_26')
def thirty():
    image = []
    gallery_image = glob.glob('static/uploads/B.sc_Agri/3_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('bsc_3_img.html', filename=image)


@app.route('/image_gallery_27')
def thirty_one():
    image = []
    gallery_image = glob.glob('static/uploads/B.sc_Agri/4_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('bsc_4_img.html', filename=image)


@app.route('/image_gallery_28')
def thirty_two():
    image = []
    gallery_image = glob.glob('static/uploads/B.sc_Agri/5_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('bsc_alm_img.html', filename=image)


@app.route('/image_gallery_29')
def thirty_three():
    image = []
    gallery_image = glob.glob('static/uploads/Diploma/1_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('dp_1_img.html', filename=image)


@app.route('/image_gallery_30')
def thirty_four():
    image = []
    gallery_image = glob.glob('static/uploads/Diploma/2_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('dp_2_img.html', filename=image)


@app.route('/image_gallery_31')
def thirty_five():
    image = []
    gallery_image = glob.glob('static/uploads/Diploma/3_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('dp_3_img.html', filename=image)


@app.route('/image_gallery_32')
def thirty_six():
    image = []
    gallery_image = glob.glob('static/uploads/Diploma/4_yr/*')
    for i in range(0,len(gallery_image)):
        image.append(gallery_image[i][15:])
    print(image)
    return render_template('dp_alm_img.html', filename=image)


@app.route('/image_gallery_33')
def thirty_seven():
    return render_template('event_1_img.html')


@app.route('/image_gallery_34')
def thirty_eight():
    return render_template('event_2_img.html')


@app.route('/image_gallery_35')
def thirty_nine():
    return render_template('event_3_img.html')


@app.route('/image_gallery_36')
def fourty():
    return render_template('event_4_img.html')


@app.route('/image_gallery_37')
def fourty_one():
    return render_template('mba_1_img.html')


@app.route('/image_gallery_38')
def fourty_two():
    return render_template('mba_2_img.html')


@app.route('/image_gallery_39')
def fourty_three():
    return render_template('mba_alm_img.html')


@app.route('/image_gallery_40')
def fourty_four():
    return render_template('mtch_1_img.html')


@app.route('/image_gallery_41')
def fourty_five():
    return render_template('mtch_2_img.html')


@app.route('/image_gallery_42')
def fourty_six():
    return render_template('mtech_alm_img.html')


@app.route('/video_gallery')
def fourty_seven():
    return render_template('Home_Page_Videos.html')


@app.route('/video_gallery_1')
def fourty_eight():
    return render_template('video_player.html')

#---------------upload--------------

ALLOWED_EXTENSIONS = set(['txt','jpeg','jpg','png','mp4','avi'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload')
def fourty_nine():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        branch = request.form['Branch']
        year = request.form['Year']
    #check if the post request has the file part
        if 'file' not in request.files:
            flash('No File Found')
            return redirect(request.url)
        file = request.files['file']
        #file.filename = "temp_1.jpg"
        if file.filename == '':
            flash('No Files Selected For Uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if branch == "B.Tech" and year == "1":
                file.save(os.path.join(app.config['B_Tech_Folder_1'], filename))
                flash('File Successfully Uploaded')
            elif branch == "B.Tech" and year == "2":
                file.save(os.path.join(app.config['B_Tech_Folder_2'], filename))
                flash('File Successfully Uploaded')
            elif branch == "B.Tech" and year == "3":
                file.save(os.path.join(app.config['B_Tech_Folder_3'], filename))
                flash('File Successfully Uploaded')
            elif branch == "B.Tech" and year == "4":
                file.save(os.path.join(app.config['B_Tech_Folder_4'], filename))
                flash('File Successfully Uploaded')
            elif branch == "B.Tech" and year == "5":
                file.save(os.path.join(app.config['B_Tech_Folder_5'], filename))
                flash('File Successfully Uploaded')
            elif branch == "bba" and year == "1":
                file.save(os.path.join(app.config['Bba_Tech_Folder_1'], filename))
                flash('File Successfully Uploaded')
            elif branch == "bba" and year == "2":
                file.save(os.path.join(app.config['Bba_Tech_Folder_2'], filename))
                flash('File Successfully Uploaded')
            elif branch == "bba" and year == "3":
                file.save(os.path.join(app.config['Bba_Tech_Folder_3'], filename))
                flash('File Successfully Uploaded')
            elif branch == "bba" and year == "4":
                file.save(os.path.join(app.config['Bba_Tech_Folder_4'], filename))
                flash('File Successfully Uploaded')
            elif branch == "Diploma" and year == "1":
                file.save(os.path.join(app.config['Diploma_Folder_1'], filename))
                flash('File Successfully Uploaded')
            elif branch == "Diploma" and year == "2":
                file.save(os.path.join(app.config['Diploma_Folder_2'], filename))
                flash('File Successfully Uploaded')
            elif branch == "Diploma" and year == "3":
                file.save(os.path.join(app.config['Diploma_Folder_3'], filename))
                flash('File Successfully Uploaded')
            elif branch == "Diploma" and year == "4":
                file.save(os.path.join(app.config['Diploma_Folder_4'], filename))
                flash('File Successfully Uploaded')
            elif branch == "B.sc_agri" and year == "1":
                file.save(os.path.join(app.config['Bsc_Folder_1'], filename))
                flash('File Successfully Uploaded')
            elif branch == "B.sc_agri" and year == "2":
                file.save(os.path.join(app.config['Bsc_Folder_2'], filename))
                flash('File Successfully Uploaded')
            elif branch == "B.sc_agri" and year == "3":
                file.save(os.path.join(app.config['Bsc_Folder_3'], filename))
                flash('File Successfully Uploaded')
            elif branch == "B.sc_agri" and year == "4":
                file.save(os.path.join(app.config['Bsc_Folder_4'], filename))
                flash('File Successfully Uploaded')
            elif branch == "B.sc_agri" and year == "5":
                file.save(os.path.join(app.config['Bsc_Folder_5'], filename))
                flash('File Successfully Uploaded')
            elif branch == "b.pharma" and year == "1":
                file.save(os.path.join(app.config['B_pharma_Folder_1'], filename))
                flash('File Successfully Uploaded')
            elif branch == "b.pharma" and year == "2":
                file.save(os.path.join(app.config['B_pharma_Folder_2'], filename))
                flash('File Successfully Uploaded')
            elif branch == "b.pharma" and year == "3":
                file.save(os.path.join(app.config['B_pharma_Folder_3'], filename))
                flash('File Successfully Uploaded')
            elif branch == "b.pharma" and year == "4":
                file.save(os.path.join(app.config['B_pharma_Folder_4'], filename))
                flash('File Successfully Uploaded')
            elif branch == "b.pharma" and year == "5":
                file.save(os.path.join(app.config['B_pharma_Folder_5'], filename))
                flash('File Successfully Uploaded')
            elif branch == "d.pharma" and year == "1":
                file.save(os.path.join(app.config['D_pharma_Folder_1'], filename))
                flash('File Successfully Uploaded')
            elif branch == "d.pharma" and year == "2":
                file.save(os.path.join(app.config['D_pharma_Folder_2'], filename))
                flash('File Successfully Uploaded')
            elif branch == "d.pharma" and year == "3":
                file.save(os.path.join(app.config['D_pharma_Folder_3'], filename))
                flash('File Successfully Uploaded')
            elif branch == "d.pharma" and year == "4":
                file.save(os.path.join(app.config['D_pharma_Folder_4'], filename))
                flash('File Successfully Uploaded')
            else:
                flash('Please Select Branch and Year')

            return redirect('/upload')
        else:
            flash('Allowed file types are txt, jpeg, jpg, png, mp4, avi')
            return redirect(request.url)


@app.route('/signup', methods=['POST'])
def signup():
    msg = None
    msg_1 = None
    conn = sqlite3.connect('User_Data.db')
    try:
        if request.method == 'POST':
            firstname = request.form['FirstName']
            lastname = request.form['LastName']
            fullname = firstname + ' ' + lastname
            branch = request.form['Branch']
            year = request.form['Year']
            position = request.form['Position']
            email = request.form['Email']
            password = request.form['inputPassword']
            confirm_password = request.form['inputConfirmPassword']
            cursor = conn.cursor()
            email_confirm = cursor.execute('select Email from USERS')
            email_confirm = list(email_confirm)
            for y in range(len(email_confirm)):
                if email == email_confirm[y][0]:
                    msg = 'You are already registered. Please Login!!'
                    break
            else:
                cur = conn.cursor()
                if password != confirm_password:
                    msg_1 = 'Password do not match'
                    return render_template('Home_Page.html', msg_1=msg_1)
                cur.execute('Insert into USERS values(?,?,?,?,?,?,?)',[fullname, branch, year, position, email, password, confirm_password])
                conn.commit()
                return render_template('login.html')
        return render_template('login.html', msg=msg)

    except Exception as e:
        print(e)
    finally:
        conn.close()



@app.route('/signin', methods=['POST'])
def student_login():
    error = None
    try:
        if request.method == 'POST':
            conn = sqlite3.connect('User_Data.db')
            email = request.form['Email']
            pwd = request.form['password']
            cursor = conn.cursor()
            data = cursor.execute('select Full_Name,Email,Password,Position from USERS where Email=(?) and Password=(?)', [email, pwd])
            data = list(data)
            global x
            if data == []:
                error = 'Invalid Credentials. Please try again!!'
            elif data != []:
                if data[0][3] == 'Student':
                    session['py'] = email
                    x = 1
                    return render_template('Student_Landing_Page.html', name=data[0][0])
                elif data[0][3] == 'Faculty':
                    session['py'] = email
                    x = 2
                    return render_template('Faculty_Landing_Page.html', name=data[0][0])
        return render_template('login.html', error=error)

    except Exception as c:
        print(c)


if __name__ == '__main__':
    app.run(debug=True,port=70)
