from flask import Blueprint, render_template, request, jsonify

formu = Blueprint('formu', __name__, template_folder="template")

@formu.route('/', methods=['GET'])
def form_get():
    return render_template("form.html")

@formu.route('/', methods=['POST'])
def form_post():
    dados = request.form
    print(jsonify(dados))
    return jsonify(dados), 200