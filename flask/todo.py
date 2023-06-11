#!/usr/bin/env

# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

TODO = [{ "text" : "Zadanie nr 1", "done" : False },
        { "text" : "Zadanie nr 2", "done" : True} ]

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        data = request.form

        if "new_task" in data.keys(): # if there was text field "new_task" submited in the form 
            if data["new_task"] != "": # if it's not empty
                TODO.append({ "text": data["new_task"], "done" : False }) # add new task to the todo list
        
        # HTML forms don't send anything if checkbox wasn't ticked
        # so we have to check for what's missing
        for i in range(0, len(TODO)):
            if i in data.keys():
                pass
            else:
                pass
        return render_template("todo.html", todo=TODO)
    
    
    return render_template("todo.html", todo=TODO)

if __name__ == "__main__":
    app.run(debug=True)

