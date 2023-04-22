'''
FILE DESCRIPTION :- THIS FILE WILL HANDLE THE ROUTE RELATED TO THE SEARCH OF THE WEBSITE
'''

from flask import Blueprint,render_template 

search = Blueprint('search',__name__,static_folder='static',template_folder='templates') 
@search.route('/')
def renderSearchPage():
    ''' This is the function that will run when someone called for '/search' route '''
    return render_template('search.html') 