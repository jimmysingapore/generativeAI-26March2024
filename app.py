#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
app = Flask(__name__)
from flask import request, render_template
@app.route("/", methods = ["GET", "POST"])
def i():
    if request.method == "POST":
        num = float(request.form.get("rates"))
        return(render_template("index.html", result = 90.2-(50.6*num)))
    else:
        time.sleep(60)
        return render_template("index.html", result ="Waiting……….")
if __name__=="__main__":
    app.run()


# In[ ]:




