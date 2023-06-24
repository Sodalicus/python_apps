#!/usr/bin/env

# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

todo = []

app = Flask(__name__)

def next_id(todo):
    # get max id from the list of all id's of dicts in TODO list, and +1
    # or return 1 if the list is empty
    if len(todo) == 0:
        return 1
    else:
        new_id = max([ x.get("id") for x in todo])+1
        return new_id

@app.route("/", methods=["POST", "GET"])
def index():
    global todo
    if request.method == "POST":
        data = request.form

        # Adding new task
        if "new_task" in data.keys(): # if there was text field "new_task" submited in the form 
            if data["new_task"] != "": # if it's not empty
                todo.append({ "id": next_id(todo), "text": data["new_task"], "done" : False }) # add new task to the todo list

        # HTML forms don't send anything if checkbox wasn't ticked
        # so we check for what was ticked and we compare it with our list 
        # Deleteting task(s)
        if "delete" in data.keys():

            # for dictionary in list, if dictionary[id] is not in data["delete"] append dictionary to the new list 
            todo[:] = [ task for task in todo if str(task["id"]) not in data.getlist("delete")]
        # changing status of the task(s)
        if "done" in data.keys():
            for task in todo:
                if str(task["id"]) in data.getlist("done"):
                    task["done"] = not task["done"]


        return render_template("todo.html", todo=todo)


    return render_template("todo.html", todo=todo)

if __name__ == "__main__":
    app.run(debug=True)

