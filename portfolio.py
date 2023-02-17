from flask import Flask, render_template,request,url_for,redirect
import csv

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

#@app.route('/index.html')
#def home():
#    return render_template('index.html')

#@app.route('/about.html')
#def about():
#    return render_template('about.html')

#@app.route('/works.html')
#def works():
 #   return render_template('works.html')

#@app.route('/contact.html')
#def contact():
#    return render_template('contact.html')

@app.route('/<string:page_name>')
def customed(page_name):
    return render_template(page_name)

# def text_data(data):
#     with open('database.txt',mode='a') as my_txt:
#         email=data["email"]
#         sub=data["subject"]
#         msg=data["message"]
#         my_txt.write(f'\n {email},{sub},{msg}')

def csv_data(data):
    with open('database.csv',newline='',mode='a') as my_csv:
        email=data["email"]
        sub=data["subject"]
        msg=data["message"]
        csv_write = csv.writer(my_csv, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,sub,msg])


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':

        #email=request.form['email']
        #sub=request.form['subject']
        #msg=request.form['message']
        #with open('names.csv', 'a', newline='') as csvfile:
            #fieldnames = ['email', 'subject','message']
            #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            #writer.writeheader()
            #writer.writerow({'email': email, 'subject': sub,'message':msg})
            
        #data=request.form.to_dict()
        #with open('data.txt',mode='a') as file:
            #file.write(str(data))

        data=request.form.to_dict()
        # text_data(data)
        csv_data(data)
        return redirect('thankyou.html')
    else:
        return "some trouble is facing"

