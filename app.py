from flask import Flask, render_template, session,request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import flask_admin as admin




app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recruitment.db'  # SQLite database
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@<host>:3306/<db>'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 36000

app.config['SECRET_KEY'] = '123456790'
db = SQLAlchemy(app)

class Users(db.Model):
    regno = db.Column(db.String(9), unique=True, primary_key=True)
    passwd =  db.Column(db.String(64), nullable=False)

class DataSync(db.Model):
    id = db.Column(db.Integer(), unique=True, primary_key = True)
    allowed = db.Column(db.Boolean())

class Admins(db.Model):
    name = db.Column(db.String(64), nullable=False)
    regno = db.Column(db.String(9), unique=True, primary_key=True)
    passwd = db.Column(db.String(64))

class SlotBookedApplicants(db.Model):
    name = db.Column(db.String(128), unique=False, nullable=False)
    regno = db.Column(db.String(9), unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String(128), nullable=False, unique=False)
    phoneNo = db.Column(db.String(32), unique=True, nullable=False)
    department1 = db.Column(db.String(32))
    department2 = db.Column(db.String(32))
    slot1_status = db.Column(db.Integer())
    slot2_status = db.Column(db.Integer())
    slot1 = db.Column(db.String(320))
    slot2 = db.Column(db.String(320))

class Slots(db.Model):
    slot_id = db.Column(db.Integer(), unique=True, primary_key = True, autoincrement=True)
    slot_num = db.Column(db.Integer())
    department = db.Column(db.String(32))
    slot = db.Column(db.String(128))
    seats = db.Column(db.Integer())
    seats_left = db.Column(db.Integer())


class Booked_Slots(db.Model):
    id = db.Column(db.Integer(), unique=True, nullable=False,primary_key = True, autoincrement=True)
    regno = db.Column(db.String(9))
    department = db.Column(db.String(32))
    slot = db.Column(db.String(64))
    
class All_Candidates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    tech1 = db.Column(db.Text, nullable=True, unique=False)
    tech2 = db.Column(db.Text, nullable=True, unique=False)
    tech3 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_5 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_5 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_5 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_5 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_5 = db.Column(db.Text, nullable=True, unique=False)
    mang1 = db.Column(db.Text, nullable=True, unique=False)
    mang2 = db.Column(db.Text, nullable=True, unique=False)
    mang3 = db.Column(db.Text, nullable=True, unique=False)
    mang4 = db.Column(db.Text, nullable=True, unique=False)
    mang5 = db.Column(db.Text, nullable=True, unique=False)
    ops1 = db.Column(db.Text, nullable=True, unique=False)
    ops2 = db.Column(db.Text, nullable=True, unique=False)
    media1 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_1 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_2 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_3 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_4 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_5 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_1 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_2 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_3 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_4 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_5 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_1 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_2 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_3 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_4 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_5 = db.Column(db.Text, nullable=True, unique=False)
    media_video_1 = db.Column(db.Text, nullable=True, unique=False)
    media_video_2 = db.Column(db.Text, nullable=True, unique=False)
    media_video_3 = db.Column(db.Text, nullable=True, unique=False)
    media_video_4 = db.Column(db.Text, nullable=True, unique=False)
    media_video_5 = db.Column(db.Text, nullable=True, unique=False)
    content1 = db.Column(db.Text, nullable=True, unique=False)
    content2 = db.Column(db.Text, nullable=True, unique=False)
    content3 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_5 = db.Column(db.Text, nullable=True, unique=False)
    
class Operations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    ops1 = db.Column(db.Text, nullable=True, unique=False)
    ops2 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)

class Technical_Rec(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    tech1 = db.Column(db.Text, nullable=True, unique=False)
    tech2 = db.Column(db.Text, nullable=True, unique=False)
    tech3 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)

class Technical_Cybersec(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    tech1 = db.Column(db.Text, nullable=True, unique=False)
    tech2 = db.Column(db.Text, nullable=True, unique=False)
    tech3 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)
    

class Technical_Frontend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    tech1 = db.Column(db.Text, nullable=True, unique=False)
    tech2 = db.Column(db.Text, nullable=True, unique=False)
    tech3 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)
    
class Technical_Backend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    tech1 = db.Column(db.Text, nullable=True, unique=False)
    tech2 = db.Column(db.Text, nullable=True, unique=False)
    tech3 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)
    
class Technical_Devops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    tech1 = db.Column(db.Text, nullable=True, unique=False)
    tech2 = db.Column(db.Text, nullable=True, unique=False)
    tech3 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)
    
class Technical_CP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    tech1 = db.Column(db.Text, nullable=True, unique=False)
    tech2 = db.Column(db.Text, nullable=True, unique=False)
    tech3 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)

class Management(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    mang1 = db.Column(db.Text, nullable=True, unique=False)
    mang2 = db.Column(db.Text, nullable=True, unique=False)
    mang3 = db.Column(db.Text, nullable=True, unique=False)
    mang4 = db.Column(db.Text, nullable=True, unique=False)
    mang5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)

    
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    content1 = db.Column(db.Text, nullable=True, unique=False)
    content2 = db.Column(db.Text, nullable=True, unique=False)
    content3 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)
    
class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    media1 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_1 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_2 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_3 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_4 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_5 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_1 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_2 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_3 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_4 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_5 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_1 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_2 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_3 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_4 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_5 = db.Column(db.Text, nullable=True, unique=False)
    media_video_1 = db.Column(db.Text, nullable=True, unique=False)
    media_video_2 = db.Column(db.Text, nullable=True, unique=False)
    media_video_3 = db.Column(db.Text, nullable=True, unique=False)
    media_video_4 = db.Column(db.Text, nullable=True, unique=False)
    media_video_5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)
    
@app.route('/', methods=['POST','GET'])
def login():
    if request.method == "POST":
        details = request.form
        regno = details["regno"]
        password = details["password"]
        ab = Admins.query.filter(Admins.regno == regno).first()
        if ab:
            if ab.passwd == password:
                session['user'] = 'admin'
                session['regno'] = regno
                session['department'] = 'admin'
                return redirect('/admin/')
    if 'user' in session:
        if session['user'] == 'admin':
            return redirect('/admin/')
    return render_template('login.html')

app.secret_key = 'supersecret'



class MyModelView(ModelView):
       # column_display_pk = True
        def is_accessible(self):
            if session['user'] == 'admin':
                return True
            else:
                return redirect('/')

class CandidateView(MyModelView):
    #column_display_pk = True # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    column_searchable_list = ['regno', 'name','email']
    column_filters = ['prefDept','prefDept2']


class UserView(MyModelView):
    column_display_pk = True # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    form_columns = ('regno', 'passwd')

class AdminView(MyModelView):
    column_display_pk = True # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    form_columns = ('name', 'regno','passwd')
    
class SlotsView(MyModelView):
    column_display_pk = False # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    form_columns = ('slot_num','department','slot','seats','seats_left')
    column_filters = ['department','slot_num','slot']
    form_choices = {
                 'department': [
                     ('Technical Department - Frontend', 'Technical Department - Frontend'),
                     ('Technical Department - Backend', 'Technical Department - Backend'),
                     ('Technical Department - Cybersec', 'Technical Department - Cybersec'),
                     ('Technical Department - CP', 'Technical Department - CP'),
                     ('Technical Department - DevOps', 'Technical Department - DevOps'),
                     ('Technical Department - Linux', 'Technical Department - Linux'),
                     ('Management Department', 'Management Department'),
                     ('Operations Department', 'Operations Department'),
                     ('Media Department', 'Media Department'),
                     ('Content Department','Content Department')
                ]
           }

    
class SlotBookedApplicantsView(MyModelView):
    column_display_pk = True # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    form_columns = ('name', 'regno','email','phoneNo','department1','department2','slot1_status','slot2_status','slot1','slot2')    
    column_searchable_list = ['regno', 'name','email']
    column_filters = ['department1','department2','slot1','slot2']


class BookedSlotsView(MyModelView):
    column_display_pk = False # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    form_columns = ('regno','department','slot')
    column_searchable_list = ['regno', 'department','slot']
    column_filters = ['department','slot']


class TechnicalView(MyModelView):
    #column_display_pk = True # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    column_list = ('shortlisted','slotbooked','slot','interviewed','issues','remarks','score','name','regno','email','contact','prefDept','prefDept2','whatLinux','whyLinux','expLinux','tech1','tech2','tech3','tech_linux_1','tech_linux_2','tech_linux_3','tech_linux_4','tech_linux_5')
    column_searchable_list = ['regno', 'name','email']
    column_editable_list = ['shortlisted','interviewed','remarks','issues','score']
    column_sortable_list = ['shortlisted','interviewed','score','slot']
    column_filters = ['shortlisted','prefDept','prefDept2','interviewed','score','slotbooked','slot']
    
    def on_model_change(self, form, model, is_created):
        if 'shortlisted' in form.data and form.shortlisted.data ==1:
            dpt = 'Technical Department - Linux'
            flag1=False
            flag2=False
            lb = SlotBookedApplicants.query.filter(SlotBookedApplicants.regno == model.regno).first()
            if model.prefDept == dpt:
                flag1 = True
            if model.prefDept2 == dpt:
                flag2 = True

            if lb:
                if flag1:
                    lb.department1=dpt
                if flag2:
                    lb.department2=dpt
                db.session.commit()
            else:
                
                if flag1:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt
                        
                    )
                
                if flag2:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department2=dpt
                        
                    )
                    
                if flag1 == True and flag2 == True:
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt,
                        department2=dpt            
                    )
                
            
                db.session.add(slotbooked_applicants)
                db.session.commit()
            flash(f'{model.name} has been shortlisted and moved to Slot Booked Applicants.', 'success')
        
        
        super(TechnicalView, self).on_model_change(form, model, is_created)

    
    
class TechnicalCybersecView(MyModelView):
    column_hide_backrefs = False
    column_list = ('shortlisted','slotbooked','slot','interviewed','issues','remarks','score','name','regno','email','contact','prefDept','prefDept2','whatLinux','whyLinux','expLinux','tech1','tech2','tech3','tech_cybersec_1','tech_cybersec_2','tech_cybersec_3','tech_cybersec_4','tech_cybersec_5')
    column_searchable_list = ['regno', 'name','email']
    column_editable_list = ['shortlisted','interviewed','remarks','issues','score']
    column_sortable_list = ['shortlisted','interviewed','score','slot']
    column_filters = ['shortlisted','prefDept']
    def on_model_change(self, form, model, is_created):
        if 'shortlisted' in form.data and form.shortlisted.data ==1:
            dpt = 'Technical Department - Cybersec'
            flag1=False
            flag2=False
            lb = SlotBookedApplicants.query.filter(SlotBookedApplicants.regno == model.regno).first()
            if model.prefDept == dpt:
                flag1 = True
            if model.prefDept2 == dpt:
                flag2 = True

            if lb:
                if flag1:
                    lb.department1=dpt
                if flag2:
                    lb.department2=dpt
                db.session.commit()
            else:
                
                if flag1:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt
                        
                    )
                
                if flag2:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department2=dpt
                        
                    )
                    
                if flag1 == True and flag2 == True:
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt,
                        department2=dpt            
                    )
                
            
                db.session.add(slotbooked_applicants)
                db.session.commit()
            flash(f'{model.name} has been shortlisted and moved to Slot Booked Applicants.', 'success')
        
        
        super(TechnicalCybersecView, self).on_model_change(form, model, is_created)
    
    
class TechnicalFrontendView(MyModelView):
    column_hide_backrefs = False
    column_list = ('shortlisted','slotbooked','slot','interviewed','issues','remarks','score','name','regno','email','contact','prefDept','prefDept2','whatLinux','whyLinux','expLinux','tech1','tech2','tech3','tech_frontend_1','tech_frontend_2','tech_frontend_3','tech_frontend_4','tech_frontend_5')
    column_searchable_list = ['regno', 'name','email']
    column_editable_list = ['shortlisted','interviewed','remarks','issues','score']
    column_sortable_list = ['shortlisted','interviewed','score','slot']
    column_filters = ['shortlisted','prefDept','prefDept2','interviewed','score','slotbooked','slot']
    
    def on_model_change(self, form, model, is_created):
        if 'shortlisted' in form.data and form.shortlisted.data ==1:
            dpt = 'Technical Department - Frontend'
            flag1=False
            flag2=False
            lb = SlotBookedApplicants.query.filter(SlotBookedApplicants.regno == model.regno).first()
            if model.prefDept == dpt:
                flag1 = True
            if model.prefDept2 == dpt:
                flag2 = True

            if lb:
                if flag1:
                    lb.department1=dpt
                if flag2:
                    lb.department2=dpt
                db.session.commit()
            else:
                
                if flag1:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt
                        
                    )
                
                if flag2:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department2=dpt
                        
                    )
                    
                if flag1 == True and flag2 == True:
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt,
                        department2=dpt            
                    )
                
            
                db.session.add(slotbooked_applicants)
                db.session.commit()
            flash(f'{model.name} has been shortlisted and moved to Slot Booked Applicants.', 'success')
        
        
        super(TechnicalFrontendView, self).on_model_change(form, model, is_created)
   
class TechnicalBackendView(MyModelView):
    column_hide_backrefs = False
    column_list = ('shortlisted','slotbooked','slot','interviewed','issues','remarks','score','name','regno','email','contact','prefDept','prefDept2','whatLinux','whyLinux','expLinux','tech1','tech2','tech3','tech_backend_1','tech_backend_2','tech_backend_3','tech_backend_4','tech_backend_5')
    column_searchable_list = ['regno', 'name','email']
    column_editable_list = ['shortlisted','interviewed','remarks','issues','score']
    column_sortable_list = ['shortlisted','interviewed','score','slot']
    column_filters = ['shortlisted','prefDept','prefDept2','interviewed','score','slotbooked','slot']
    
    def on_model_change(self, form, model, is_created):
        if 'shortlisted' in form.data and form.shortlisted.data ==1:
            dpt = 'Technical Department - Backend'
            flag1=False
            flag2=False
            lb = SlotBookedApplicants.query.filter(SlotBookedApplicants.regno == model.regno).first()
            if model.prefDept == dpt:
                flag1 = True
            if model.prefDept2 == dpt:
                flag2 = True

            if lb:
                if flag1:
                    lb.department1=dpt
                if flag2:
                    lb.department2=dpt
                db.session.commit()
            else:
                
                if flag1:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt
                        
                    )
                
                if flag2:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department2=dpt
                        
                    )
                    
                if flag1 == True and flag2 == True:
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt,
                        department2=dpt            
                    )
                
            
                db.session.add(slotbooked_applicants)
                db.session.commit()
            flash(f'{model.name} has been shortlisted and moved to Slot Booked Applicants.', 'success')
        
        
        super(TechnicalBackendView, self).on_model_change(form, model, is_created)
    
class TechnicalDevOpsView(MyModelView):
    column_hide_backrefs = False
    column_list = ('shortlisted','slotbooked','slot','interviewed','issues','remarks','score','name','regno','email','contact','prefDept','prefDept2','whatLinux','whyLinux','expLinux','tech1','tech2','tech3','tech_devops_1','tech_devops_2','tech_devops_3','tech_devops_4','tech_devops_5')
    column_searchable_list = ['regno', 'name','email']
    column_editable_list = ['shortlisted','interviewed','remarks','issues','score']
    column_sortable_list = ['shortlisted','interviewed','score','slot']
    column_filters = ['shortlisted','prefDept','prefDept2','interviewed','score','slotbooked','slot']
    def on_model_change(self, form, model, is_created):
        if 'shortlisted' in form.data and form.shortlisted.data ==1:
            dpt = 'Technical Department - DevOps'
            flag1=False
            flag2=False
            lb = SlotBookedApplicants.query.filter(SlotBookedApplicants.regno == model.regno).first()
            if model.prefDept == dpt:
                flag1 = True
            if model.prefDept2 == dpt:
                flag2 = True

            if lb:
                if flag1:
                    lb.department1=dpt
                if flag2:
                    lb.department2=dpt
                db.session.commit()
            else:
                
                if flag1:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt
                        
                    )
                
                if flag2:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department2=dpt
                        
                    )
                    
                if flag1 == True and flag2 == True:
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt,
                        department2=dpt            
                    )
                
            
                db.session.add(slotbooked_applicants)
                db.session.commit()
            flash(f'{model.name} has been shortlisted and moved to Slot Booked Applicants.', 'success')
        
        
        super(TechnicalDevOpsView, self).on_model_change(form, model, is_created)
    
class TechnicalCPView(MyModelView):
    column_hide_backrefs = False
    column_list = ('shortlisted','slotbooked','slot','interviewed','issues','remarks','score','name','regno','email','contact','prefDept','prefDept2','whatLinux','whyLinux','expLinux','tech1','tech2','tech3','tech_cp_1','tech_cp_2','tech_cp_3','tech_cp_4','tech_cp_5')
    column_searchable_list = ['regno', 'name','email']
    column_editable_list = ['shortlisted','interviewed','remarks','issues','score']
    column_sortable_list = ['shortlisted','interviewed','score','slot']
    column_filters = ['shortlisted','prefDept','prefDept2','interviewed','score','slotbooked','slot']
    def on_model_change(self, form, model, is_created):
        if 'shortlisted' in form.data and form.shortlisted.data ==1:
            dpt = 'Technical Department - CP'
            flag1=False
            flag2=False
            lb = SlotBookedApplicants.query.filter(SlotBookedApplicants.regno == model.regno).first()
            if model.prefDept == dpt:
                flag1 = True
            if model.prefDept2 == dpt:
                flag2 = True

            if lb:
                if flag1:
                    lb.department1=dpt
                if flag2:
                    lb.department2=dpt
                db.session.commit()
            else:
                
                if flag1:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt
                        
                    )
                
                if flag2:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department2=dpt
                        
                    )
                    
                if flag1 == True and flag2 == True:
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt,
                        department2=dpt            
                    )
                
            
                db.session.add(slotbooked_applicants)
                db.session.commit()
            flash(f'{model.name} has been shortlisted and moved to Slot Booked Applicants.', 'success')
        
        
        super(TechnicalCPView, self).on_model_change(form, model, is_created)
    
    
    
class ManagementView(MyModelView):
    #column_display_pk = True # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    column_list = ('shortlisted','slotbooked','slot','interviewed','issues','remarks','score','name','regno','email','contact','prefDept','prefDept2','whatLinux','whyLinux','expLinux','mang1','mang2','mang3','mang4','mang5')
    column_searchable_list = ['regno', 'name','email']
    column_editable_list = ['shortlisted','interviewed','remarks','issues','score']
    column_sortable_list = ['shortlisted','interviewed','score','slot']
    column_filters = ['shortlisted','prefDept','prefDept2','interviewed','score','slotbooked','slot']
    def on_model_change(self, form, model, is_created):
        if 'shortlisted' in form.data and form.shortlisted.data ==1:
            dpt = 'Management Department'
            flag1=False
            flag2=False
            lb = SlotBookedApplicants.query.filter(SlotBookedApplicants.regno == model.regno).first()
            if model.prefDept == dpt:
                flag1 = True
            if model.prefDept2 == dpt:
                flag2 = True

            if lb:
                if flag1:
                    lb.department1=dpt
                if flag2:
                    lb.department2=dpt
                db.session.commit()
            else:
                
                if flag1:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt
                        
                    )
                
                if flag2:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department2=dpt
                        
                    )
                    
                if flag1 == True and flag2 == True:
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt,
                        department2=dpt            
                    )
                
            
                db.session.add(slotbooked_applicants)
                db.session.commit()
            flash(f'{model.name} has been shortlisted and moved to Slot Booked Applicants.', 'success')
        
        
        super(ManagementView, self).on_model_change(form, model, is_created)
    
class OperationsView(MyModelView):
    #column_display_pk = True # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    column_list = ('shortlisted','slotbooked','slot','interviewed','issues','remarks','score','name','regno','email','contact','prefDept','prefDept2','whatLinux','whyLinux','expLinux','ops1','ops2')
    column_searchable_list = ['regno', 'name','email']
    column_editable_list = ['shortlisted','interviewed','remarks','issues','score']
    column_sortable_list = ['shortlisted','interviewed','score','slot']
    column_filters = ['shortlisted','prefDept','prefDept2','interviewed','score','slotbooked','slot']
    def on_model_change(self, form, model, is_created):
        if 'shortlisted' in form.data and form.shortlisted.data ==1:
            dpt = 'Operations Department'
            flag1=False
            flag2=False
            lb = SlotBookedApplicants.query.filter(SlotBookedApplicants.regno == model.regno).first()
            if model.prefDept == dpt:
                flag1 = True
            if model.prefDept2 == dpt:
                flag2 = True

            if lb:
                if flag1:
                    lb.department1=dpt
                if flag2:
                    lb.department2=dpt
                db.session.commit()
            else:
                
                if flag1:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt
                        
                    )
                
                if flag2:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department2=dpt
                        
                    )
                    
                if flag1 == True and flag2 == True:
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt,
                        department2=dpt            
                    )
                
            
                db.session.add(slotbooked_applicants)
                db.session.commit()
            flash(f'{model.name} has been shortlisted and moved to Slot Booked Applicants.', 'success')
        
        
        super(OperationsView, self).on_model_change(form, model, is_created)
    
class ContentView(MyModelView):
    #column_display_pk = True # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    column_list = ('shortlisted','slotbooked','slot','interviewed','issues','remarks','score','name','regno','email','contact','prefDept','prefDept2','whatLinux','whyLinux','expLinux','content1','content2','content3')
    column_searchable_list = ['regno', 'name','email']
    column_editable_list = ['shortlisted','interviewed','remarks','issues','score']
    column_sortable_list = ['shortlisted','interviewed','score','slot']
    column_filters = ['shortlisted','prefDept','prefDept2','interviewed','score','slotbooked','slot']
    def on_model_change(self, form, model, is_created):
        if 'shortlisted' in form.data and form.shortlisted.data ==1:
            dpt = 'Content Department'
            flag1=False
            flag2=False
            lb = SlotBookedApplicants.query.filter(SlotBookedApplicants.regno == model.regno).first()
            if model.prefDept == dpt:
                flag1 = True
            if model.prefDept2 == dpt:
                flag2 = True

            if lb:
                if flag1:
                    lb.department1=dpt
                if flag2:
                    lb.department2=dpt
                db.session.commit()
            else:
                
                if flag1:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt
                        
                    )
                
                if flag2:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department2=dpt
                        
                    )
                    
                if flag1 == True and flag2 == True:
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1=dpt,
                        department2=dpt            
                    )
                
            
                db.session.add(slotbooked_applicants)
                db.session.commit()
            flash(f'{model.name} has been shortlisted and moved to Slot Booked Applicants.', 'success')
        
        
        super(ContentView, self).on_model_change(form, model, is_created)
    
class MediaView(MyModelView):
    #column_display_pk = True # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    column_list = ('shortlisted','slotbooked','slot','interviewed','issues','remarks','score','name','regno','email','contact','prefDept','prefDept2','whatLinux','whyLinux','expLinux','media1','media_photo_1','media_photo_2','media_photo_3','media_photo_4','media_photo_5','media_graphic_1','media_graphic_2','media_graphic_3','media_graphic_4','media_graphic_5','media_social_media_1','media_social_media_2','media_social_media_3','media_social_media_4','media_social_media_5','media_video_1','media_video_2','media_video_3','media_video_4','media_video_5')
    column_searchable_list = ['regno', 'name','email','prefDept','prefDept2']
    column_editable_list = ['shortlisted','interviewed','remarks','issues','score']
    column_sortable_list = ['shortlisted','interviewed','score','slot']
    column_filters = ['shortlisted','prefDept','prefDept2','interviewed','score','slotbooked','slot']
    
    def on_model_change(self, form, model, is_created):
        if 'shortlisted' in form.data and form.shortlisted.data ==1:
            dpt = 'Media'
            flag1=False
            flag2=False
            lb = SlotBookedApplicants.query.filter(SlotBookedApplicants.regno == model.regno).first()
            if dpt in model.prefDept:
                flag1 = True
            if dpt in model.prefDept2:
                flag2 = True

            if lb:
                if flag1:
                    lb.department1='Media Department'
                if flag2:
                    lb.department2='Media Department'
                db.session.commit()
            else:
                
                if flag1:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1='Media Department'
                        
                    )
                
                if flag2:
                    
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department2='Media Department'
                        
                    )
                
                if flag1 == True and flag2 == True:
                    slotbooked_applicants = SlotBookedApplicants(
                        name=model.name,
                        regno=model.regno,
                        email=model.email,
                        phoneNo=model.contact,
                        department1='Media Department',
                        department2='Media Department'            
                    )
                    
                
            
                db.session.add(slotbooked_applicants)
                db.session.commit()
            flash(f'{model.name} has been shortlisted and moved to Slot Booked Applicants.', 'success')
        
        
        super(MediaView, self).on_model_change(form, model, is_created)

admin = Admin(app)
admin.add_view(UserView(Users, db.session))
#admin.add_view(AdminView(Admins, db.session))
admin.add_view(SlotsView(Slots, db.session))
admin.add_view(SlotBookedApplicantsView(SlotBookedApplicants, db.session))
admin.add_view(BookedSlotsView(Booked_Slots, db.session))
admin.add_view(CandidateView(All_Candidates, db.session))
admin.add_view(TechnicalView(Technical_Rec,db.session))
admin.add_view(TechnicalCybersecView(Technical_Cybersec,db.session))
admin.add_view(TechnicalFrontendView(Technical_Frontend,db.session))
admin.add_view(TechnicalBackendView(Technical_Backend,db.session))
admin.add_view(TechnicalDevOpsView(Technical_Devops,db.session))
admin.add_view(TechnicalCPView(Technical_CP,db.session))
admin.add_view(ManagementView(Management, db.session))
admin.add_view(OperationsView(Operations, db.session))
admin.add_view(MediaView(Media,db.session))
admin.add_view(ContentView(Content,db.session))



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        app.run(debug=True)
