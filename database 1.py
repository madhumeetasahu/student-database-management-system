# from crypt import methods
from flask import Flask, render_template, request

# import pymongo
# Student=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
# mydb=Student['Vinay']
# collection=mydb["vinay_database"]
# collection2=mydb["vinay2"]

app = Flask(__name__)

@app.route('/', methods=['POST'])
def First():
   if request.methods=='POST':
      return render_template('index.html')           
   return render_template('Login.html')
 
@app.route('/')
def login():
    # login code goes here
   #  password=request.form['password']
   #  email = request.form['email']
   #  password_1 = 'password'
   #  print(password)
   # #  remember = True if request.form.get('remember') else False

   # #  user = User.query.filter_by(email=email).first()

   #  # check if the user actually exists
   #  # take the user-supplied password, hash it, and compare it to the hashed password in the database
   #  if password_1 != password:
   #    #   flash('Please check y  our login details and try again.')
   #      return render_template("Login.html") # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    return render_template('Login.html')

@app.route('/index')
def index():  
   return render_template('index.html')

@app.route('/About_Us')
def About_Us():
   return render_template('About_Us.html')

@app.route('/Home')
def Home():
       return render_template('Home.html')
    
@app.route('/Akanksha',methods=["POST","GET"])
def Akanksha():
   if request.method=="POST":
      # print(request.get_json())

      first_name=request.get_json()["fname"]
      last_name=request.get_json()["lname"]
      roll_no=request.get_json()["roll"]
      email_value=request.get_json()["email"]
      gender_type=request.get_json()["gender"]
      sem=request.get_json().get("sem")

      record = {
         "firstname":first_name,a
         "lastname":last_name,
         "rollno":roll_no,
         "email_id":email_value,
         "gender_id":gender_type,
         "semester":sem
      }
      collection.insert_one(record)
      
      # return"your name is "+first_name+last_name
   return render_template('Akanksha.html')

@app.route('/Database',methods=["GET","POST"])
def Database():
   alldocs=collection2.find({})
   print(alldocs)
   
   return render_template('Database.html',alldocs=alldocs)

@app.route('/Calculations',methods=["POST","GET"])
def Calculations():
   
   if request.method=="POST":
         #  x={}
         #  x = request.form
         #  print(x)
         #  print(request.form["ass"])
         #  print(request.form["pract"])
         #  print(request.form["ut"])
         #  print(request.form["tl"])
         #  print(request.form["sub"])
      first_name=request.get_json()["fname"]
      last_name=request.get_json()["lname"]
      roll_no=request.get_json()["roll"]
      email_value=request.get_json()["email"]
      gender_type=request.get_json()["gender"]
      sem=request.get_json().get("sem")
      avg_assignmnet=request.get_json()["assignment"]
      avg_practical=request.get_json()["practical"]
      avg_unit=request.get_json()["unit"]
      total_marks=request.get_json()["total"]
      subject_name=request.get_json()["subject"]


      average  = {
         "fname":first_name,
         "lname":last_name,
         "roll":roll_no,
         "email":email_value,
         "gender":gender_type,
         "sem":sem,
         "assignment":avg_assignmnet,
         "pratical":avg_practical,
         "unit":avg_unit,
         "total":total_marks,
         "subject":subject_name,
      }
      
      print(average)
      collection2.insert_one(average)
      print("data posted",request.form)
   return render_template('Calculation.html')



    
if __name__ == '__main__':
    app.run(debug=True, port='5000' ,use_debugger=False, use_reloader=True)
    Database()
