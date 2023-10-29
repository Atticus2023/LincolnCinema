from abc import ABC
from typing import List
import datetime

class BaseModel:
    _id_counter = 1 

    def __init__(self):
        self.id = self._generate_id()

    @classmethod
    def _generate_id(cls):
        new_id = cls._id_counter
        cls._id_counter += 1
        return new_id
    
class User(BaseModel):
  def __init__(self,  userRole,username, password, firstName,lastName, address, email, phoneNum):
    super().__init__()   
    self.userRole = userRole
    self.username = username
    self.password = password
    self.firstName = firstName
    self.lastName = lastName
    self.address = address
    self.email = email
    self.phoneNum = phoneNum

class Admin(User):
  def __init__(self,  username, password, firstName, lastName, address, email, phoneNum):
    super().__init__( "admin", username, password, firstName, lastName, address, email, phoneNum)

class Staff(User):
  def __init__(self,  username, password, firstName, lastName, address, email, phoneNum):
    super().__init__( "staff", username, password, firstName, lastName, address, email, phoneNum)
    self.payments = []
  
  def receivePayment(self, payment):
    if payment not in self.payments:
      self.payments.append(payment)

class Customer(User):
  def __init__(self,  username, password, firstName,lastName, address, email, phoneNum):
    super().__init__( "customer", username, password, firstName,lastName, address, email, phoneNum)
    self.bookingList = []    
    self.notificationList = []

  def makeBooking(self, booking):
    if booking not in self.bookingList:
      self.bookingList.append(booking)
  
  def receiveNotice(self, notification):
    if notification not in self.notificationList:
      self.notificationList.append(notification)

class Movie(BaseModel):
  def __init__(self,  title, description, country, language, genre, releaseDate, duration, imagePath):  
      super().__init__()      
      self.title = title
      self.description = description
      self.country = country
      self.language = language
      self.genre = genre
      self.releaseDate = releaseDate
      self.duration = duration
      self.imagePath = imagePath
      self.movieScreenings = []
  
  def movieAddScreening(self, screening):
    if screening not in self.movieScreenings:
      self.movieScreenings.append(screening)
     

class Screening(BaseModel):
  def __init__(self, date, startTime, endTime, hall, price):
    super().__init__()   
    self.date = date
    self.startTime = startTime
    self.endTime = endTime
    self.hall = hall
    self.price = price

class Hall:
  def __init__(self, hallID, capacity):
    self.hallID = hallID
    self.capacity = capacity
    self.seatsList = [Seat(isReserved=False) for _ in range(capacity)]

class Seat(BaseModel):
  def __init__(self,  isReserved): 
    super().__init__()      
    self.isReserved = isReserved

class Booking(BaseModel):
  def __init__(self, customer, screening):
    super().__init__()   
    self.customer = customer
    self.screening = screening
    self.bookingseats = []

  def appendSeat(self, seat):
    if seat not in self.bookingseats:
      self.bookingseats.append(seat)

class Payment(BaseModel):
  def __init__(self,  booking, amount, method, discountCoupon):
    super().__init__()   
    self.booking = booking
    self.amount = amount
    self.method = method
    self.discountCoupon = discountCoupon

class DiscountCoupon(BaseModel):
  def __init__(self,  promoCode, discount):
    super().__init__()   
    self.promoCode = promoCode
    self.discount = discount

class Notification(BaseModel):
  def __init__(self, message):
    self.message = message