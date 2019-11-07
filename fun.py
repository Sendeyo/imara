import data
from passlib.hash import sha256_crypt
import ast


def Data():
    names = ["Python", "Java", "C", "C++", "Assembly",
             "Javascript", "Dart", "Arduino", "PHP"]
    return names


def Check_email(email):
    try:
        query = 'select Email from Users where Email = "{}";'.format(email)
        returned = data.read(query)
        return returned[0][0]
    except Exception as e:
        return ""


def Authenticate(attempted_email, attempted_password):
    query = 'select * from Users where Email = "{}";'.format(attempted_email)
    info = data.read(query)
    try:
        password = info[0][3]
        user = {"Username":info[0][1], "Email":info[0][2], "Category":info[0][4], "State":info[0][5],}
    except:
        return ""
    Similer = sha256_crypt.verify(str(attempted_password), password)
    print(Similer)
    if Similer:
        return user
    else:
        return ""

def Register(username, email, password):
    val = Check_email(email)
    if val:
        return val
    else:
        try:
            password = sha256_crypt.hash(password)
            query = 'insert into Users (Username, Email, Pass, Category) values ("{}","{}","{}","Guest");'.format(username, email, password)
            print(query)
            data.data_write(query)
        except Exception as e:
            return ""


def getUserType(email):
    query = 'select Category from Users where Email="{}";'.format(email)
    category = data.read(query)
    category = category[0][0]
    return category


def getUserInfo(email):
    query = 'select * from Users where Email="{}";'.format(email)
    category = data.read(query)
    category = category[0]
    return category


def getRoutes():
    query = 'select Name from Routes;'
    routes = data.read(query)
    return routes


def Reservations(email):
    query = 'select * from Reservation where Email like "{}";'.format(email)
    reservations = data.read(query)
    return reservations


def FreeSeats(reservation_id):
    a = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    # a=[1,2,3,4,5,6,7,8,9,10,11]
    t = []
    query = 'select Route, Date, Time from Reservation where Id ="{}"'.format(
        reservation_id)
    info = data.read(query)
    query = 'select Seat from Reservation where Route ="{}" and Date ="{}" and Time ="{}"'.format(
        info[0][0], info[0][1], info[0][2])
    taken_seats = data.read(query)
    #taken_seats = ast.literal_eval(taken_seats)
    for x in taken_seats:
        t.append(x[0])
    b = [x for x in a if x not in t]
    freeSeats = b
    return freeSeats


def CheckSeat(reservation_id, seat_no):
    query = 'update Reservation set Seat = "{}" where Id = "{}"'.format(
        seat_no, reservation_id)
    return query


def CheckPayment(details, email):
    details = ast.literal_eval(details)
    query = 'select Route from Reservation where Id = "{}"'.format(details[0])
    route = data.read(query)
    route = route[0][0]
    query = 'select Cost from Routes where Name = "{}"'.format(route)
    price = data.read(query)
    price = price[0][0]
    query = 'select Coupons from Users where Email = "{}"'.format(email)
    coupons = data.read(query)
    coupons = coupons[0][0]

    if coupons > price:
        balance = coupons - price
        query = 'update Reservation set Seat = "{}" where Id = "{}"'.format(
            details[1], details[0])
        info = data.data_write(query)
        query = 'update Reservation set Payment = "{}" where Id = "{}"'.format(
            price, details[0])
        info = data.data_write(query)
        query = 'update Users set Coupons = "{}" where Email = "{}"'.format(
            balance, email)
        info = data.data_write(query)
        return "Payment successful"
    else:
        return "cant afford"


def Check_email_existance(email):
    query = 'select Email from Users'
    info = data.read(query)
    if email in info[0]:
        return str(email)


def Check_token_existance(email):
    query = 'select Token from Users where Email ="{}"'.format(email)
    info = data.read(query)
    return info
