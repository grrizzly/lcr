from flask import Blueprint, current_app, request, make_response, url_for, render_template
import models
import resourcecontroller
import contentcontroller

api = Blueprint('api', __name__, url_prefix='/api')

# Content CRUD routes ---------------------------------
# Create (supports optional inline and multi parameters)
@api.route('/create/content/', methods=['POST'])
def CreateContent():
	return contentcontroller.create(request) 

# Retrieve
@api.route('/content/<id>', methods=['GET'])
def RetrieveContent(id):
	return contentcontroller.retrieve(request, id) 

# Update
@api.route('/update/content/<id>', methods=['POST'])
def UpdateContent(id):
	return contentcontroller.update(request, id) 

# Delete
@api.route('/delete/content/<id>', methods=['POST'])
def DeleteContent(id):
	return contentcontroller.delete(request, id) 

# Resource CRUD routes ---------------------------------
# Create (supports optional multi parameters)
@api.route('/create/resource/<id>', methods=['POST'])
def CreateResource(id):
	return resourcecontroller.create(request, id) 

# Retrieve
@api.route('/resource/<id>', methods=['GET'])
def RetrieveResource(id):
	return resourcecontroller.retrieve(request, id) 

# Update (supports metadata parameter)
@api.route('/update/resource/<id>', methods=['POST'])
def UpdateResource(id):
	return resourcecontroller.update(request, id) 

# Delete
@api.route('/delete/resource/<id>', methods=['POST'])
def DeleteResource(id):
	return resourcecontroller.content(request, id)