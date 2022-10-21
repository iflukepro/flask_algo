from flask import Flask, render_template, request
from con import get_db_connection
app = Flask(__name__)



@app.route("/form_get", methods=["GET"])
def FormGET_index():
    if request.method == "GET":
        conn = get_db_connection()
        data = conn.execute("select id,username,firstname,lastname from 'user_table' ").fetchall()
        conn.close()
        print("data",len(data))
        print(data)
        if len(data) != 0:
            for w in data:
                print(w[0],w[1],w[2],w[3])
            print(len(request.args))
            if len(request.args) != 0:
                print(request.args)
                #Firstname = request.args['firstname'] 
                Firstname = request.args.get('firstname')
                Lastname = request.args.get('lastname')
                print(Firstname,Lastname)    
                conn = get_db_connection()
                data = conn.execute("select id,username,firstname,lastname from 'user_table' where firstname=? and lastname=?"\
                    ,[Firstname,Lastname]).fetchall()
                
                conn.close()
                print(data)
                if data is None:
                    #return if search data is none
                    return render_template("form_get.html")
                else:
                    for k in data:
                        print(k[0],k[1],k[2],k[3])
                    #return from search query
                    return render_template("form_get.html",data = data)
            #return if we query all data sucessfuly
            return render_template("form_get.html",data = data)
        #return if len data from query all is 0
        return render_template("form_get.html")

@app.route("/form_post", methods=["GET","POST"])
def FormPOST_index():
    if request.method == "GET":
        return render_template("form_post.html")
    elif request.method == "POST":
        print(len(request.form))
        if len(request.form) != 0:
            print(request.form)
            for key,value in request.form.items():
                print(key,value)
            Firstname = request.form.get('firstname')
            Lastname = request.form.get('lastname')
            print(Firstname,Lastname)
            return render_template("form_post.html",data= [Firstname,Lastname])
if __name__ == "main" :
    app.run(debug=True)
