from flask import Blueprint, Flask, redirect, render_template, request
import models
from models.biting import Biting
from repositories import biting_repository, human_repository, zombie_repository

bitings_blueprint = Blueprint("bitings", __name__)

# INDEX


@bitings_blueprint.route("/bitings")
def bitings():
    bitings = biting_repository.select_all()
    return render_template("bitings/index.html", bitings=bitings)

# NEW


@bitings_blueprint.route("/bitings/new")
def new_biting():
    humans = human_repository.select_all()
    zombies = zombie_repository.select_all()
    return render_template("bitings/new.html", humans=humans, zombies=zombies)

# CREATE


@bitings_blueprint.route("/bitings", methods=["POST"])
def create_biting():
    human_id = request.form["human_id"]
    zombie_id = request.form["zombie_id"]
    human = human_repository.select(human_id)
    zombie = zombie_repository.select(zombie_id)
    new_biting = Biting(human, zombie)
    biting_repository.save(new_biting)
    return redirect("/bitings")

# EDIT

# UPDATE

# DELETE
