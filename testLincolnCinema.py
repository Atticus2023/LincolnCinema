import pytest
from model import  BaseModel, Customer, Admin, Staff, Movie, Hall, Seat, Screening, Booking, Payment, DiscountCoupon, Notification


def test_admin_creation():
    admin = Admin("admin1", "password123", "John", "Doe", "123 Main St", "john@example.com", "1234567890")
    assert admin.username == "admin1"
    assert admin.email == 'john@example.com'

def test_staff_creation():
    staff = Staff("staff1", "password123", "John", "Doe", "123 Main St", "john@example.com", "1234567890")
    assert staff.username == "staff1"
    assert staff.email == 'john@example.com'

def test_customer_creation():
    customer = Customer("customer1", "password123", "John", "Doe", "123 Main St", "john@example.com", "1234567890")
    assert customer.username == "customer1"
    assert customer.email == 'john@example.com'

def test_movie_creation():
    movie = Movie("Sample Movie", "Description", "Country", "Language", "Genre", "2023-01-01", 120, "image.jpg")
    assert movie.title == "Sample Movie"
    
# Test Screening class
def test_screening():
    hall = Hall(1, 100)
    instance = Screening("Movie Title", "2023-11-02", "15:00", "17:00", hall, 10.99)
    assert hasattr(instance, 'movieTitle')
    assert hasattr(instance, 'seats')

# Test Hall class
def test_hall():
    instance = Hall(1, 100)
    assert hasattr(instance, 'hallID')
    assert hasattr(instance, 'capacity')
    assert hasattr(instance, 'hallScreenings')

# Test Seat class
def test_seat():
    instance = Seat(False)
    assert hasattr(instance, 'isReserved')

# Test Booking class
def test_booking():
    customer = Customer("customer1", "password123", "John", "Doe", "123 Main St", "john@example.com", "1234567890")
    hall = Hall(1,100)
    screening = Screening("Movie Title", "2023-11-02", "15:00", "17:00", hall, 10.99)
    instance = Booking(customer, screening)
    assert hasattr(instance, 'customer')
    assert hasattr(instance, 'screening')
    assert hasattr(instance, 'bookingseats')

# Test Payment class
def test_payment():
    customer = Customer("customer1", "password123", "John", "Doe", "123 Main St", "john@example.com", "1234567890")
    hall = Hall(1,100)
    screening = Screening("Movie Title", "2023-11-02", "15:00", "17:00", hall, 10.99)
    booking = Booking(customer, screening)
    instance = Payment(booking, 20.0, "Credit Card", None)
    assert hasattr(instance, 'booking')
    assert hasattr(instance, 'amount')
    assert hasattr(instance, 'method')
    assert hasattr(instance, 'discountCoupon')

# Test DiscountCoupon class
def test_discount_coupon():
    instance = DiscountCoupon("CODE123", 10)
    assert hasattr(instance, 'promoCode')
    assert hasattr(instance, 'discount')

# Test Notification class
def test_notification():
    instance = Notification("This is a notification.")
    assert hasattr(instance, 'message')


# controller pytest
@pytest.fixture
def controller():
    from controller import LincolnCinemaController
    return LincolnCinemaController()

# Test register
def test_register_user(controller):
    result = controller.register("testuser", "password", "John", "Doe", "123 Main St", "test@example.com", "1234567890")
    assert result == True

# Test Login
def test_login_user(controller):
    controller.register("testuser", "password", "John", "Doe", "123 Main St", "test@example.com", "1234567890")
    user = controller.login("testuser", "password")
    assert user is not None

# Test logout
def test_logout_user(controller):
    controller.register("testuser", "password", "John", "Doe", "123 Main St", "test@example.com", "1234567890")
    user = controller.login("testuser", "password")
    controller.logout()
    assert controller.loggedInUser is None

# Test get movie by id
def test_get_movie_by_id(controller):
    movie = controller.getMovieByID(2)  
    assert movie is not None

# Test get movie by title
def test_get_movie_by_title(controller):
    movie = controller.getMovieByTitle("The Avengers")  # 请替换为实际的电影标题
    assert movie is not None

# Test get hall by id
def test_get_hall_by_id(controller):
    hall = controller.getHallByID(1)  # 假设有一个 ID 为 1 的影厅
    assert hall is not None

# Test get user by username
def test_get_user_by_username(controller):
    user = controller.getUserByUsername("staff")  # 请替换为实际的用户名
    assert user is not None

# Test get screening by id
def test_get_screening_by_id(controller):
    screening = controller.getScreeningByID(31)  # 假设有一个 ID 为 1 的放映
    assert screening is not None

# Test get coupon by code
def test_get_discount_coupon_by_code(controller):
    discount_coupon = controller.getDiscountCouponByCode("aaa")  # 请替换为实际的优惠券代码
    assert discount_coupon is not None

# Test add movie
def test_add_movie(controller):
    title = "Test Movie"
    description = "Test Description"
    country = "Test Country"
    language = "Test Language"
    genre = "Test Genre"
    releaseDate = "2023-01-01"
    duration = 120
    imagePath = "test_image.jpg"

    result = controller.add_movie(title, description, country, language, genre, releaseDate, duration, imagePath)
    assert result is True

    # Test same movie title
    result = controller.add_movie(title, description, country, language, genre, releaseDate, duration, imagePath)
    assert result is False

# Test delete movie
def test_delete_movie(controller):    
    movie = Movie("Test Movie", "Test Description", "Test Country", "Test Language", "Test Genre", "2023-01-01", 120, "test_image.jpg")
    controller.movies.append(movie)

    result = controller.deleteMovie(movie)
    assert result is True

    # Test not exist movie
    result = controller.deleteMovie(Movie("Non-Existent Movie", "Description", "Country", "Language", "Genre", "2023-01-01", 120, "image.jpg"))
    assert result is False

# Test add screening
def test_add_screening(controller):    
    movie_title = "Titanic"
    date = "2023-11-15"
    start_time = "14:00"
    end_time = "16:00"
    hall_id = 1
    price = 10.0
    result = controller.addScreening(movie_title, date, start_time, end_time, hall_id, price)
    assert result is True

# Test cancel screening
def test_cancel_screening(controller):    
    movie_title = "Titanic"
    date = "2023-11-15"
    start_time = "14:00"
    end_time = "16:00"
    hall_id = 1
    price = 10.0

    controller.addScreening(movie_title, date, start_time, end_time, hall_id, price)
    movie = controller.getMovieByTitle(movie_title)
    screening = movie.movieScreenings[0]

    result = controller.cancelScreening(movie, screening)

    assert result is True 

# Test check promotion code
def test_check_promo_code(controller):    
    promo_code = "aaa"
    discount = 0.9  
    result = float(controller.checkPromoCode(promo_code))
    assert result == discount  

# Test sent notification to all customers
def test_send_notice_to_all(controller):    
    message = "Important notice to all customers"
    controller.sendNoticeToAll(message)    
    for customer in controller.customers:
        assert message in [notice.message for notice in customer.notificationList]

# Test sent notification to the customer
def test_send_notice_to_customer(controller):
    customer = Customer("username", "password", "John", "Doe", "123 Main St", "johndoe@example.com", "555-555-5555")
    message = "Important notice for a specific customer"
    controller.sendNoticeToCustomer(customer, message)   
    assert message in [notice.message for notice in customer.notificationList]