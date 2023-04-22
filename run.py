''' Project Name : TB Grocery Store '''
''' Project Description : This is a website that is made for a grocery store and is having all the
features neeeded for the store to grow. '''
''' Author : Hameed Cuddapah '''

''' FILE DESCRIPTION : THIS IS THE MAIN FILE THAT RUNS THE PROJECT '''

from views import createApp 

app = createApp() 

if __name__ == '__main__':
    app.run(debug=True,port=5001) 