from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.secret_key = 'lincolncinema'

from controller import LincolnCinemaController

controller = LincolnCinemaController()

app.config['UPLOAD_FOLDER'] = 'static/images'  

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def filterData():
    movies = controller.movies
    unique_countries = list(set(movie.country for movie in movies))
    unique_years = list(set(movie.releaseDate for movie in movies))
    unique_genres = list(set(movie.genre for movie in movies))
    return movies,unique_countries,unique_years,unique_genres

@app.route('/')
def index():
    movies = controller.movies  
    unique_countries = list(set(movie.country for movie in movies))
    unique_years = list(set(movie.releaseDate for movie in movies))
    unique_genres = list(set(movie.genre for movie in movies))

    return render_template('index.html', movies=movies, unique_countries=unique_countries,unique_years=unique_years,unique_genres=unique_genres)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        address = data.get('address')
        email = data.get('email')
        phoneNum = data.get('phoneNum')
        
        result = controller.register(username, password, firstName,lastName, address, email, phoneNum)
       
        if result:
            session['username'] = username
            session['userRole'] = 'customer'
            session['firstName'] = firstName
            session['lastName'] = lastName
            session['address'] = address
            session['email'] = email
            session['phoneNum'] = phoneNum

            response = {'success': True, 'message': 'Registration successful'}
            return jsonify(response), 200
        else:
            response = {'success': False, 'message': 'Registration failed: Username already taken'}
            return jsonify(response), 400

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password') 
    user = controller.login(username, password)
    if user: 
        session['username'] = user.username
        session['userRole'] = user.userRole
        session['firstName'] = user.firstName
        session['lastName'] = user.lastName
        session['address'] = user.address
        session['email'] = user.email
        session['phoneNum'] = user.phoneNum
        if user.userRole == 'admin':
            return jsonify({'userRole': 'admin'})

        if user.userRole == 'staff':
            return jsonify({'userRole': 'staff'})

        if user.userRole == 'customer':            
            return jsonify({'userRole': 'customer'})

    return jsonify({'userRole': 'guest'})

@app.route('/logout')
def logout():
    session.clear()
    controller.logout
    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search_movies():
    title = request.args.get('title')
    country = request.args.get('country')
    language = request.args.get('language')
    genre = request.args.get('genre')
    releaseDate = request.args.get('releaseDate')
    
    matching_movies = controller.searchMovies(title, country, language, genre, releaseDate)

    return jsonify(matching_movies)

@app.route('/adminDashboard')
def adminDashboard():
    if 'username' in session:
        movies, unique_countries, unique_years, unique_genres = filterData()
        username = session['username']        
        user = controller.getUserByUsername(username) 
        movies = controller.movies
        return render_template('adminDashboard.html', user=user,movies=movies, unique_countries=unique_countries,unique_years=unique_years,unique_genres=unique_genres)


@app.route('/addMovie', methods=['POST'])
def add_movie():
    try:        
        title = request.form.get('title')        
        description = request.form.get('description')
        country = request.form.get('country')
        language = request.form.get('language')
        genre = request.form.get('genre')
        releaseDate = request.form.get('releaseDate')
        duration = request.form.get('duration')

        if 'image' in request.files:
            image = request.files['image']
           
            if image:
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                image.save(image_path)                  
                controller.add_movie(title, description, country, language, genre, releaseDate, duration, image_path)
                return jsonify({'message': 'Movie added successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to add movie', 'details': str(e)}), 400

@app.route('/addScreening/<movieTitle>', methods=['GET','POST'])
def addScreening(movieTitle):    
    movieTitle = request.args.get('movieTitle')        
    if request.method == 'POST':
        date = request.form.get('date')
        startTime = request.form.get('startTime')
        endTime = request.form.get('endTime')
        hallID = request.form.get('hallID')            
        price = request.form.get('price')            

        result = controller.addScreening(movieTitle,date,startTime, endTime, hallID, price)
        if result:
            flash('Add screening successfully!', 'info')
            return redirect(url_for('adminDashboard'))

    return render_template('addScreening.html', movieTitle = movieTitle)


@app.route('/deleteMovie/<movieTitle>')
def deleteMovie(movieTitle):
    if session['userRole'] == 'admin':
        movie = controller.getMovieByTitle(movieTitle)
        result = controller.deleteMovie(movie)
        if result:
            return redirect(url_for('adminDashboard'))
    else:
      return redirect('/login')     
    

@app.route('/movieDetails', methods=['GET'])
def movieDetails(): 
    movieID = request.args.get("movieID")  
    movie = controller.getMovieByID(movieID)        
    movie_screenings_data = []
    for screening in movie.movieScreenings:
        screening_data = {
            "movieID": movieID,
            "screeningID": screening.id,
            "date": screening.date,
            "startTime": screening.startTime,
            "endTime": screening.endTime,
            "hall": {
                "hallID": screening.hall.hallID,
                "capacity": screening.hall.capacity                
            }
        }
        movie_screenings_data.append(screening_data)    
    return render_template('movieDetails.html',   movie=movie, movie_screenings_data=movie_screenings_data)  

  
@app.route('/cancelScreening/<screeningID>')
def cancelScreening(screeningID):
    if session['userRole'] == 'admin':
        screening = controller.getScreeningByID(screeningID)
        result = controller.cancelScreening(screening)
        if result:
            return redirect(url_for('movieDetails'))
    else:
      return redirect('/login')     
    
@app.route('/staffDashboard')
def staffDashboard():
    if 'username' in session:
        username = session['username']        
        user = controller.getUserByUsername(username)        
        movies, unique_countries, unique_years, unique_genres = filterData()
        if user:           
            return render_template('staffDashboard.html', user=user, movies=movies, unique_countries=unique_countries,unique_years=unique_years,unique_genres=unique_genres)
        else:
            return "User not found"
    else:
        return redirect('/login')
    
   
@app.route('/staff/allBookings')
def staffViewBookings():
    if 'username' in session:
        allBookings = controller.bookings
        return render_template('staffViewBookings.html', allBookings=allBookings) 

@app.route('/customerDashboard')
def customer_dashboard():
    if 'username' in session:
        username = session['username']        
        user = controller.getUserByUsername(username)        
        movies, unique_countries, unique_years, unique_genres = filterData()
        if user:           
            return render_template('customerDashboard.html', user=user, movies=movies, unique_countries=unique_countries,unique_years=unique_years,unique_genres=unique_genres)
        else:
            return "User not found"
    else:
        return redirect('/login')

@app.route('/movieScreening', methods=['GET'])
def movieScreening(): 
    movieID = request.args.get("movieID")  
    movie = controller.getMovieByID(movieID)        
    movie_screenings_data = []
    for screening in movie.movieScreenings:
        screening_data = {
            "movieID": movieID,
            "screeningID": screening.id,
            "date": screening.date,
            "startTime": screening.startTime,
            "endTime": screening.endTime,
            "hall": {
                "hallID": screening.hall.hallID,
                "capacity": screening.hall.capacity                
            }
        }
        movie_screenings_data.append(screening_data)
            
    today = datetime.now().date()
    today_str = today.strftime('%Y-%m-%d')
    tomorrow = today + timedelta(days=1)
    tomorrow_str = tomorrow.strftime('%Y-%m-%d')
    day_after_tomorrow = today + timedelta(days=2)
    day_after_tomorrow_str = day_after_tomorrow.strftime('%Y-%m-%d')
    
    return render_template('movieScreening.html',   movie=movie, movie_screenings_data=movie_screenings_data,today=today_str, tomorrow=tomorrow_str, day_after_tomorrow=day_after_tomorrow_str)
    

@app.route('/hallScreening', methods=['GET'])
def hallScreening():  
    hallID = request.args.get("hallID")  
    hall = controller.getHallByID(hallID)        
    hall_screenings_data = []
    for screening in hall.hallScreenings:
        screening_data = {
            "hallID": hallID,
            "screeningID": screening.id,
            "date": screening.date,
            "startTime": screening.startTime,
            "endTime": screening.endTime,
            "hall": {
                "hallID": screening.hall.hallID,
                "capacity": screening.hall.capacity,
                "seats": [
                    {
                        "seatID": seat.id,
                        "isReserved": seat.isReserved
                    }
                    for seat in screening.hall.seatsList
                ]
            }
        }
        hall_screenings_data.append(screening_data)
            
    today = datetime.now().date()
    today_str = today.strftime('%Y-%m-%d')
    tomorrow = today + timedelta(days=1)
    tomorrow_str = tomorrow.strftime('%Y-%m-%d')
    day_after_tomorrow = today + timedelta(days=2)
    day_after_tomorrow_str = day_after_tomorrow.strftime('%Y-%m-%d')
    
    return render_template('movieScreening.html',   hall=hall, hall_screenings_data=hall_screenings_data,today=today_str, tomorrow=tomorrow_str, day_after_tomorrow=day_after_tomorrow_str)

@app.route('/makeBooking', methods=['GET'])
def makeBooking():
    if 'username' in session:
        username = session['username']       
        userRole = session['userRole'] 
        screeningID = request.args.get('screeningID')            
        movieID = request.args.get('movieID')
        user = controller.getUserByUsername(username)  
        movie = controller.getMovieByID(movieID)
        screening = controller.getScreeningByID(screeningID) 
        if userRole == 'staff':
            return render_template('staffMakeBooking.html', user=user, movie=movie, screening=screening)
        elif userRole == 'customer':
            return render_template('makeBooking.html', user=user, movie=movie, screening=screening)
    else:
        flash('You have not login', 'info')
        return redirect('/')
        
@app.route('/submitBooking', methods=['POST'])
def submit_booking():
    if request.method == 'POST':
        data = request.get_json()
        selectedSeats = data.get('selectedSeats', [])
        screeningID = data.get('screeningID')
        movieID = data.get('movieID')
        selectedSeatsList = []
        for seatID in selectedSeats:
            seat = controller.getSeatByID(seatID,screeningID)
            selectedSeatsList.append(seat)
        
        screening = controller.getScreeningByID(screeningID)  
        if session['userRole'] == 'customer':
            username = session['username']
            user = controller.getUserByUsername(username) 
            booking = controller.makeBooking(user, screening, selectedSeatsList)
        elif session['userRole'] == 'staff':
            username = data.get('customerName')            
            user = controller.getUserByUsername(username)            
            booking = controller.makeBooking(user, screening, selectedSeatsList)
       
        return jsonify({'message': 'Booking successful','bookingID': booking.id})

    return jsonify({'error': 'Invalid request method'})

@app.route('/payment', methods=['GET'])
def payment():
    #  booking, amount, method, discountCoupon
    if 'username' in session:
        bookingID = request.args.get('bookingID')
        booking = controller.getBookingByID(bookingID)
        amount = float(booking.screening.price) * len(booking.bookingseats)        

        return render_template('payment.html', booking=booking, amount=amount)
    else:
        flash('You have not login', 'info')
        return redirect('/')
    
@app.route('/validatePromoCode', methods=['POST'])
def validatePromoCode():
    data = request.json
    promoCode = data.get('promoCode')
    amount = data.get('totalAmount')
    
    discount = controller.checkPromoCode(promoCode)
    
    if discount:
        discountedAmount = float(amount)*float(discount)
        print(discountedAmount)
        return jsonify({'valid': True,'discountedAmount': discountedAmount})  
    else:
        return jsonify({'valid': False})  

@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.json
    bookingID = data.get('bookingId')
    customerName = data.get('customerName')
    screeningID = data.get('screeningId')
    selectedPaymentMethod = data.get('selectedPaymentMethod')
    bookingSeats = data.get('bookingSeats')
    amount = data.get('totalAmount')
    promoCode = data.get('promoCode')

    booking = controller.getBookingByID(bookingID)
    customer = controller.getUserByUsername(customerName)
    screening = controller.getScreeningByID(screeningID)
    discountCoupon = controller.getDiscountCouponByCode(promoCode)

    message = f" {customerName} {screening.date} {screening.startTime} {screening.hall.hallID} {bookingSeats} "
    controller.sendNoticeToCustomer(customer, message)
    controller.payment(booking, amount, selectedPaymentMethod, discountCoupon)
    if session['userRole'] == 'staff':
        return jsonify({'success': True, 'message': 'Payment successful', 'userRole': 'Staff' }), 200
    if session['userRole'] == 'customer':
        return jsonify({'success': True, 'message': 'Payment successful', 'userRole': 'Customer' }), 200

@app.route('/bookingList')
def bookingList():
    if 'username' in session:
        username = session['username'] 
        
        user = controller.getUserByUsername(username)
        bookingList = user.bookingList
        
        if bookingList:
            return render_template('bookingList.html', bookingList=bookingList)
        flash('You have not book any screening', 'info')
        return redirect('/customerDashboard')
    

@app.route('/cancelBooking/<int:bookingID>', methods=['POST'])
def cancelBooking(bookingID):
    if 'username' in session and session['userRole'] == 'customer':
        username = session['username'] 
        print('cus========yanzheng11111')
        print(username)
        user = controller.getUserByUsername(username)
        print('cus========yanzheng')
        print(user.username)
        result = controller.cancelBooking(user, bookingID)

    elif session['userRole'] == 'staff':
        data = request.json
        username = data.get('username')
        print('staff=========111')
        print(username)
        user = controller.getUserByUsername(username)
        print('staff=========222')
        print(user.username)
        result = controller.cancelBooking(user, bookingID)

    if result:
        return  jsonify({'success': True, 'message': 'Cancel successful'}), 200
    else:
        return jsonify({'success': False, 'message': 'error'})

if __name__ == '__main__':
    app.run()