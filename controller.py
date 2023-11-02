from model import  BaseModel, Customer, Admin, Staff, Movie, Hall, Screening, Booking, Payment, DiscountCoupon, Notification

user1 = Admin(  "admin", "password", "John", "Smith", "1 Lincoln Rd", "admin@lincoln.com", "0211234561")
user2 = Staff( "staff", "password", "Moon", "Smith", "2 Lincoln Rd", "staff@lincoln.com", "0211234562")
user3 = Customer( "customer1", "password", "Jim", "Smith", "3 Lincoln Rd", "customer1@lincoln.com", "0211234563")
user4 = Customer( "customer2", "password", "Tom", "Smith", "4 Lincoln Rd", "customer2@lincoln.com", "0211234564")

hall1 = Hall(1, 120)
hall2 = Hall(2, 90)
hall3 = Hall(3, 110)
hall4 = Hall(4, 80)

movie1 = Movie( "Gone with the Wind", "A story of a strong-willed woman's love during the American Civil War and Reconstruction periods.", "Japan", "English", "Drama, Romance, War", "1939", 238, "static/images/images2.jpeg")
screening1 = Screening("Gone with the Wind","2023-11-03", "19:00", "23:00", hall1, price=10.0)
screening2 = Screening("Gone with the Wind","2023-11-03", "10:00", "14:00", hall2, price=15.0)
screening3 = Screening("Gone with the Wind","2023-11-04", "15:00", "19:00", hall1, price=10.0)
screening4 = Screening("Gone with the Wind","2023-11-04", "10:00", "14:00", hall3, price=12.0)
screening5 = Screening("Gone with the Wind","2023-11-09", "15:00", "19:00", hall4, price=10.0)
screening6 = Screening("Gone with the Wind","2023-11-09", "10:00", "14:00", hall4, price=12.0)
movie1.movieScreenings.append(screening1)
movie1.movieScreenings.append(screening2)
movie1.movieScreenings.append(screening3)
movie1.movieScreenings.append(screening4)
movie1.movieScreenings.append(screening5)
movie1.movieScreenings.append(screening6)

hall1.hallScreenings.append(screening1)
hall1.hallScreenings.append(screening3)
hall2.hallScreenings.append(screening2)
hall3.hallScreenings.append(screening4)
hall4.hallScreenings.append(screening5)
hall4.hallScreenings.append(screening6)

movie2 = Movie( "Star Wars", "A science fiction film depicting the struggle between the Rebel Alliance and the Galactic Empire, along with the power of the Force.", "France", "English", "Sci-Fi, Action, Adventure", "1977", 121, "static/images/images7.jpeg")
screening7 = Screening("Star Wars","2023-11-06", "19:00", "23:00", hall1, price=10.0)
screening8 = Screening("Star Wars","2023-11-07", "10:00", "14:00", hall2, price=15.0)
screening9 = Screening("Star Wars","2023-11-07", "15:00", "19:00", hall1, price=10.0)
screening10 = Screening("Star Wars","2023-11-05", "10:00", "14:00", hall3, price=12.0)
screening11 = Screening("Star Wars","2023-11-04", "15:00", "19:00", hall4, price=10.0)
screening12 = Screening("Star Wars","2023-11-04", "10:00", "14:00", hall4, price=12.0)
movie2.movieScreenings.append(screening7 )
movie2.movieScreenings.append(screening8 )
movie2.movieScreenings.append(screening9 )
movie2.movieScreenings.append(screening10)
movie2.movieScreenings.append(screening11)
movie2.movieScreenings.append(screening12)

hall1.hallScreenings.append(screening7)
hall1.hallScreenings.append(screening9)
hall2.hallScreenings.append(screening8)
hall3.hallScreenings.append(screening10)
hall4.hallScreenings.append(screening11)
hall4.hallScreenings.append(screening12)

movie3 = Movie( "Modern Times", "A classic comedy featuring Charlie Chaplin as the Tramp in a series of comedic situations in the industrialized world.", "China", "Silent", "Comedy", "1936", 87, "static/images/images2.jpeg")
screening13 = Screening("Modern Times","2023-11-06", "19:00", "23:00", hall1, price=10.0)
screening14 = Screening("Modern Times","2023-11-07", "10:00", "14:00", hall2, price=15.0)
screening15 = Screening("Modern Times","2023-11-07", "15:00", "19:00", hall1, price=10.0)
screening16 = Screening("Modern Times","2023-11-05", "10:00", "14:00", hall3, price=12.0)
screening17 = Screening("Modern Times","2023-11-04", "15:00", "19:00", hall4, price=10.0)
screening18 = Screening("Modern Times","2023-11-04", "10:00", "14:00", hall1, price=12.0)
movie3.movieScreenings.append(screening13)
movie3.movieScreenings.append(screening14)
movie3.movieScreenings.append(screening15)
movie3.movieScreenings.append(screening16)
movie3.movieScreenings.append(screening17)
movie3.movieScreenings.append(screening18)
hall1.hallScreenings.append(screening13)
hall1.hallScreenings.append(screening15)
hall2.hallScreenings.append(screening14)
hall3.hallScreenings.append(screening16)
hall4.hallScreenings.append(screening17)
hall1.hallScreenings.append(screening18)

movie4 = Movie( "Pulp Fiction", "A non-linear crime film that weaves together multiple interconnected stories, with violence, humor, and memorable characters.", "USA", "English", "Crime, Drama, Thriller", "1994", 154, "static/images/images8.jpeg")
screening19 = Screening("Pulp Fiction","2023-11-06", "19:00", "23:00", hall1, price=10.0)
screening20 = Screening("Pulp Fiction","2023-11-07", "10:00", "14:00", hall2, price=15.0)
screening21 = Screening("Pulp Fiction","2023-11-07", "15:00", "19:00", hall1, price=10.0)
screening22 = Screening("Pulp Fiction","2023-11-05", "10:00", "14:00", hall3, price=12.0)
screening23 = Screening("Pulp Fiction","2023-11-04", "15:00", "19:00", hall4, price=10.0)
screening24 = Screening("Pulp Fiction","2023-11-04", "10:00", "14:00", hall1, price=12.0)
movie4.movieScreenings.append(screening19)
movie4.movieScreenings.append(screening20)
movie4.movieScreenings.append(screening21)
movie4.movieScreenings.append(screening22)
movie4.movieScreenings.append(screening23)
movie4.movieScreenings.append(screening24)
hall1.hallScreenings.append(screening19)
hall1.hallScreenings.append(screening21)
hall1.hallScreenings.append(screening24)
hall3.hallScreenings.append(screening22)
hall2.hallScreenings.append(screening20)
hall4.hallScreenings.append(screening23)

movie5 = Movie( "The Godfather", "A crime epic following the powerful Corleone family, their patriarch Vito Corleone, and the world of organized crime.", "USA", "English", "Crime, Drama", "1972", 175, "static/images/images2.jpeg")
screening25 = Screening("The Godfather","2023-11-06", "19:00", "23:00", hall1, price=10.0)
screening26 = Screening("The Godfather","2023-11-07", "10:00", "14:00", hall2, price=15.0)
screening27 = Screening("The Godfather","2023-11-07", "15:00", "19:00", hall1, price=10.0)
screening28 = Screening("The Godfather","2023-11-05", "10:00", "14:00", hall3, price=12.0)
screening29 = Screening("The Godfather","2023-11-04", "15:00", "19:00", hall4, price=10.0)
screening30 = Screening("The Godfather","2023-11-04", "10:00", "14:00", hall1, price=12.0)
movie5.movieScreenings.append(screening25)
movie5.movieScreenings.append(screening26)
movie5.movieScreenings.append(screening27)
movie5.movieScreenings.append(screening28)
movie5.movieScreenings.append(screening29)
movie5.movieScreenings.append(screening30)
movie6 = Movie( "The Shawshank Redemption", "The story of two imprisoned men who form a deep bond, finding solace and eventual redemption through acts of common decency.", "USA", "English", "Drama", "1994", 142, "static/images/images7.jpeg")
screening31 = Screening("The Shawshank Redemption", "2023-11-06", "19:00", "23:00", hall1, price=10.0)
screening32 = Screening("The Shawshank Redemption", "2023-11-07", "10:00", "14:00", hall2, price=15.0)
screening33 = Screening("The Shawshank Redemption", "2023-11-07", "15:00", "19:00", hall1, price=10.0)
screening34 = Screening("The Shawshank Redemption", "2023-11-05", "10:00", "14:00", hall3, price=12.0)
screening35 = Screening("The Shawshank Redemption", "2023-11-04", "15:00", "19:00", hall4, price=10.0)
screening36 = Screening("The Shawshank Redemption", "2023-11-04", "10:00", "14:00", hall1, price=12.0)
movie6.movieScreenings.append(screening31)
movie6.movieScreenings.append(screening32)
movie6.movieScreenings.append(screening33)
movie6.movieScreenings.append(screening34)
movie6.movieScreenings.append(screening35)
movie6.movieScreenings.append(screening36)
movie7 = Movie( "Schindler's List", "A historical drama about Oskar Schindler, a German businessman who saved the lives of more than a thousand Polish-Jewish refugees during the Holocaust.", "USA", "English", "Biography, Drama, History", "1993", 195, "static/images/images2.jpeg")
screening37 = Screening("Schindler's List", "2023-11-06", "19:00", "23:00", hall1, price=10.0)
screening38 = Screening("Schindler's List", "2023-11-07", "10:00", "14:00", hall2, price=15.0)
screening39 = Screening("Schindler's List", "2023-11-07", "15:00", "19:00", hall1, price=10.0)
screening40 = Screening("Schindler's List", "2023-11-05", "10:00", "14:00", hall3, price=12.0)
screening41 = Screening("Schindler's List", "2023-11-04", "15:00", "19:00", hall4, price=10.0)
screening42 = Screening("Schindler's List", "2023-11-04", "10:00", "14:00", hall1, price=12.0)
movie7.movieScreenings.append(screening37)
movie7.movieScreenings.append(screening38)
movie7.movieScreenings.append(screening39)
movie7.movieScreenings.append(screening40)
movie7.movieScreenings.append(screening41)
movie7.movieScreenings.append(screening42)
movie8 = Movie( "Casablanca", "Set during World War II, it's a tale of love and sacrifice at Rick's Café Américain in the Vichy-controlled Moroccan city of Casablanca.", "USA", "English", "Drama, Romance, War", "1942", 102, "static/images/images8.jpeg")
screening43 = Screening( "Casablanca","2023-11-06", "19:00", "23:00", hall1, price=10.0)
screening44 = Screening( "Casablanca","2023-11-07", "10:00", "14:00", hall2, price=15.0)
screening45 = Screening( "Casablanca","2023-11-07", "15:00", "19:00", hall1, price=10.0)
screening46 = Screening( "Casablanca","2023-11-05", "10:00", "14:00", hall3, price=12.0)
screening47 = Screening( "Casablanca","2023-11-04", "15:00", "19:00", hall4, price=10.0)
screening48 = Screening( "Casablanca","2023-11-04", "10:00", "14:00", hall1, price=12.0)
movie8.movieScreenings.append(screening43)
movie8.movieScreenings.append(screening44)
movie8.movieScreenings.append(screening45)
movie8.movieScreenings.append(screening46)
movie8.movieScreenings.append(screening47)
movie8.movieScreenings.append(screening48)
movie9 = Movie( "The Dark Knight", "A superhero film centered around Batman's quest to stop the Joker's reign of chaos in Gotham City.", "USA", "English", "Action, Crime, Drama", "2008", 152, "static/images/images2.jpeg")
screening49 = Screening( "The Dark Knight", "2023-11-06", "19:00", "23:00", hall1, price=10.0)
screening50 = Screening( "The Dark Knight", "2023-11-07", "10:00", "14:00", hall2, price=15.0)
screening51 = Screening( "The Dark Knight", "2023-11-07", "15:00", "19:00", hall1, price=10.0)
screening52 = Screening( "The Dark Knight", "2023-11-05", "10:00", "14:00", hall3, price=12.0)
screening53 = Screening( "The Dark Knight", "2023-11-04", "15:00", "19:00", hall4, price=10.0)
screening54 = Screening( "The Dark Knight", "2023-11-04", "10:00", "14:00", hall1, price=12.0)
movie9.movieScreenings.append(screening49)
movie9.movieScreenings.append(screening50)
movie9.movieScreenings.append(screening51)
movie9.movieScreenings.append(screening52)
movie9.movieScreenings.append(screening53)
movie9.movieScreenings.append(screening54)
movie10 = Movie( "Forrest Gump", "A heartwarming story of Forrest Gump, a man with a low IQ, who inadvertently influences historical events in the 20th century USA.", "USA", "English", "Drama, Romance", "1994", 142, "static/images/images7.jpeg")
screening55 = Screening("Forrest Gump", "2023-11-06", "19:00", "23:00", hall1, price=10.0)
screening56 = Screening("Forrest Gump", "2023-11-07", "10:00", "14:00", hall2, price=15.0)
screening57 = Screening("Forrest Gump", "2023-11-07", "15:00", "19:00", hall1, price=10.0)
screening58 = Screening("Forrest Gump", "2023-11-05", "10:00", "14:00", hall3, price=12.0)
screening59 = Screening("Forrest Gump", "2023-11-04", "15:00", "19:00", hall4, price=10.0)
screening60 = Screening("Forrest Gump", "2023-11-04", "10:00", "14:00", hall1, price=12.0)
movie10.movieScreenings.append(screening55)
movie10.movieScreenings.append(screening56)
movie10.movieScreenings.append(screening57)
movie10.movieScreenings.append(screening58)
movie10.movieScreenings.append(screening59)
movie10.movieScreenings.append(screening60)
movie11 = Movie( "The Matrix", "A sci-fi action film featuring a computer hacker who discovers a dystopian world run by machines and becomes humanity's last hope.", "USA", "English", "Sci-Fi, Action", "1999", 136, "static/images/images2.jpeg")
screening61 = Screening("The Matrix", "2023-11-06", "19:00", "23:00", hall1, price=10.0)
screening62 = Screening("The Matrix", "2023-11-07", "10:00", "14:00", hall2, price=15.0)
screening63 = Screening("The Matrix", "2023-11-07", "15:00", "19:00", hall1, price=10.0)
screening64 = Screening("The Matrix", "2023-11-05", "10:00", "14:00", hall3, price=12.0)
screening65 = Screening("The Matrix", "2023-11-04", "15:00", "19:00", hall4, price=10.0)
screening66 = Screening("The Matrix", "2023-11-04", "10:00", "14:00", hall1, price=12.0)
movie11.movieScreenings.append(screening61)
movie11.movieScreenings.append(screening62)
movie11.movieScreenings.append(screening63)
movie11.movieScreenings.append(screening64)
movie11.movieScreenings.append(screening65)
movie11.movieScreenings.append(screening66)
movie12 = Movie( "The Lord of the Rings: The Fellowship of the Ring", "The first installment of an epic fantasy trilogy involving a young hobbit's journey to destroy a powerful ring.", "USA", "English", "Fantasy, Adventure", "2001", 178, "static/images/images2.jpeg")

movie13 = Movie( "The Avengers", "A superhero ensemble film bringing together iconic Marvel characters to save the world from an extraterrestrial threat.", "USA", "English", "Action, Adventure, Sci-Fi", "2012", 143, "static/images/images8.jpeg")
movie14 = Movie( "Titanic", "A romantic drama set aboard the ill-fated RMS Titanic, starring Jack and Rose's love story amidst the ship's tragic sinking.", "USA", "English", "Drama, Romance", "1997", 195, "static/images/images2.jpeg")
movie15 = Movie( "E.T. the Extra-Terrestrial", "A heartwarming sci-fi tale about a young boy and his newfound alien friend's adventures on Earth.", "UK", "English", "Sci-Fi, Family", "1982", 115, "static/images/images2.jpeg")

discountCoupon1 = DiscountCoupon('aaa', 0.9)
discountCoupon2 = DiscountCoupon('bbb', 0.8)
discountCoupon3 = DiscountCoupon('ccc', 0.7)


class LincolnCinemaController:
  def __init__(self):
    self.users = [user1,user2,user3,user4]
    self.admins = [user1]
    self.staffs = [user2]
    self.customers = [user3,user4]
    self.movies = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10, movie11, movie12, movie13, movie14, movie15]    
    self.halls = [hall1,hall2,hall3,hall4]
    self.bookings = []
    self.payments = []
    self.discountCoupons = [discountCoupon1,discountCoupon2,discountCoupon3]
    self.notifications = []
    self.loggedInUser = None

  def searchMovies(self, title=None, country=None, language=None, genre=None, releaseDate=None):
    # Create an empty list to store matching movies
    matchingMovies = []

    # Iterate through the movies to filter based on search criteria
    for movie in self.movies:
      # Check if the movie's attributes match the search criteria
      if (title is None or title.lower() in movie.title.lower()) and \
        (country is None or country.lower() == movie.country.lower()) and \
        (language is None or language.lower() == movie.language.lower()) and \
        (genre is None or genre.lower() in movie.genre.lower()) and \
        (releaseDate is None or releaseDate == movie.releaseDate):
        matchingMovies.append(movie)

    return matchingMovies 


  def register(self,  username, password, firstName,lastName, address, email, phoneNum):
    if not any(user.username == username for user in self.users):
        newCustomer = Customer( username, password, firstName, lastName, address, email, phoneNum)
        self.users.append(newCustomer)  
        self.customers.append(newCustomer)      
        return True  # Registration successful
    return False  # Registration failed (username already taken)

  def login(self, username, password):
    for user in self.users:
        if user.username == username and user.password == password:            
            self.loggedInUser = user
            return user  # Return the authenticated user object
    return None 
  
  def logout(self):
     self.loggedInUser = None
  
  def getMovieByID(self,movieID):
    for movie in self.movies:
        requested_id = int(movieID)
        # requested_id = int(movieID.strip())
        if movie.id == requested_id:           
            return movie
    return None
  def getMovieByTitle(self,movieTitle):
    for movie in self.movies:        
        if movie.title == movieTitle:           
            return movie
    return None
  
  def getHallByID(self, hallID):     
     for hall in self.halls:
        if hall.hallID == int(hallID):
           return hall
     return None

  def getUserByUsername(self, username):
     for user in self.users:
        if user.username == username:
           return user
     return None
  
  def getSeatByID(self, seatID,screeningID):
    screening = self.getScreeningByID(screeningID)
    for seat in screening.seats:
        if seat.id == int(seatID):
            return seat
    return None
  
  def getScreeningByID(self, screeningID):    
    for movie in self.movies:      
      for screening in movie.movieScreenings:                 
          if screening.id == int(screeningID):            
            return screening 
    return None
  
  def getBookingByID(self, bookingID):
     for booking in self.bookings:
        if booking.id == int(bookingID):          
          return booking
     return None
  
  def getDiscountCouponByCode(self, promoCode):
     for discountCoupon in self.discountCoupons:
        if discountCoupon.promoCode == promoCode:
           return discountCoupon
     return None
  
  def add_movie(self,  title, description, country, language, genre, releaseDate, duration, imagePath):
    if not any(movie.title == title for movie in self.movies):
        new_movie = Movie( title, description, country, language, genre, releaseDate, duration, imagePath)
        self.movies.append(new_movie)
        return True  
    return False 

  def deleteMovie(self, movie):    
    if movie in self.movies:
      self.movies.remove(movie)
      return True
    else:
      return False
  
  def addScreening(self, movieTitle, date, startTime, endTime, hallID, price): 
    
    hall = self.getHallByID(hallID)    
    movie = self.getMovieByTitle(movieTitle)
    new_screening = Screening(movieTitle,date,startTime, endTime, hall, price) 
    if new_screening not in movie.movieScreenings and new_screening not in hall.hallScreenings:
      movie.movieAddScreening(new_screening)
      hall.hallAddScreening(new_screening)
      return True
    else:
      return False
  
  def cancelScreening(self, movie, screening):
    hall = screening.hall
    if screening in movie.movieScreenings and screening in hall.hallScreenings:
      movie.movieScreenings.remove(screening)
      hall.hallScreenings.remove(screening)

      return True
    else:
      return False

  def makeBooking(self, customer, screening, selectedSeats):
    newBooking = Booking(customer, screening)
    for seat in selectedSeats:
      if not seat.isReserved: 
        seat.isReserved = True 
        newBooking.appendSeat(seat)
    self.bookings.append(newBooking)
    customer.makeBooking(newBooking)
    return newBooking
  
  def payment(self, booking, amount, method, discountCoupon):
    newPayment = Payment(booking, amount, method, discountCoupon)    
    self.payments.append(newPayment)
    for staff in self.staffs:
       staff.receivePayment(newPayment)

  def checkPromoCode(self, promoCode):
     for discountCoupon in self.discountCoupons:
        if discountCoupon.promoCode == promoCode:
           return discountCoupon.discount
     return None
  
  def sendNoticeToAll(self,message):
     newNotice = Notification(message)
     self.notifications.append(newNotice)
     for customer in self.customers:
        customer.receiveNotice(newNotice)

  def sendNoticeToCustomer(self, customer, message):
     newNotice = Notification(message)
     self.notifications.append(newNotice)
     customer.receiveNotice(newNotice)

  def cancelBooking(self, customer, bookingID):     
     canceledBooking = self.getBookingByID(bookingID)     
     for seat in canceledBooking.bookingseats:
        seat.isReserved = False
     self.bookings.remove(canceledBooking)
     customer.bookingList.remove(canceledBooking)
     return True

