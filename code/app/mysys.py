#!/usr/bin/python
#-- coding: utf-8 --
import mysql.connector
from mysql.connector import Error

def show_msg(str):
    print str
    return;

def check_ticket(ticketid):
    try:
        connection = mysql.connector.connect(host='localhost',
                                 database='SmartParking',
                                 user='admin',
                                 password='1234')
        sql_Query = "select state from ticket where idticket=%s"
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_Query, (ticketid, ))
        record = cursor.fetchone()
        state = str(record[0])
        print state
    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return False if state=="not payed" else True

def car_left(sensor):
    return True if sensor==1 else False

def request(str, name):
    if str=="parking_list":
        try:
            connection = mysql.connector.connect(host='localhost',
                                     database='SmartParking',
                                     user='admin',
                                     password='1234')
            sql_Query = "select address, `lat`, `long` from Parking"
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_Query)
            record = cursor.fetchall()
            list=record
            # for row in list:
            #     print row[0], "lat =", row[1], "long =", row[2]
        except Error as e :
            print ("Error while connecting to MySQL", e)
        finally:
            #closing database connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        return list

    if str=="history":
        try:
            connection = mysql.connector.connect(host='localhost',
                                     database='SmartParking',
                                     user='admin',
                                     password='1234')
            sql_Query = "select `plate`, `name`, `date`, `spotname` from `history` WHERE `name`=%s ORDER BY `date` DESC "
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_Query, (name,))
            hist = cursor.fetchall()
        except Error as e :
            print ("Error while connecting to MySQL", e)
        finally:
            #closing database connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        return hist

    if str=="spot_list":
        try:
            connection = mysql.connector.connect(host='localhost',
                                     database='SmartParking',
                                     user='admin',
                                     password='1234')
            sql_Query = "select spotname, parking from spot"
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_Query)
            record = cursor.fetchall()
            for row in record:
                print "spot:", row[0], "in parking:", row[1]
        except Error as e :
            print ("Error while connecting to MySQL", e)
        finally:
            #closing database connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        return record

    if str=="ticket_price":
        try:
            connection = mysql.connector.connect(host='localhost',
                                     database='SmartParking',
                                     user='admin',
                                     password='1234')
            ticketid = raw_input("enter ticket id:")
            sql_Query = "select active_time from ticket where idticket=%s"
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_Query, (ticketid,))
            record = cursor.fetchone()
            time = record[0]
            print time
            query2 = "select timestampdiff(hour, %s, NOW())"
            cursor.execute(query2, (time,))
            record = cursor.fetchone()
            hours=record[0]
            price = hours*5
            print price, 'euro'
        except Error as e :
            print ("Error while connecting to MySQL", e)
        finally:
            #closing database connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        return price

    if str=="change":
        try:
            connection = mysql.connector.connect(host='localhost',
                                     database='SmartParking',
                                     user='admin',
                                     password='1234')
            id = raw_input("Enter pay station id:")
            sql_Query = "select `change` from pay_station where idpay_station=%s"
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_Query, (id,))
            record = cursor.fetchone()
            change=record[0]
        except Error as e :
            print ("Error while connecting to MySQL", e)
        finally:
            #closing database connection.
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        return change
    return

def alert(str):
    if str=="sensor":
        show_msg("Check sensors for mulfunctions")
    if str=="pay_station":
        show_msg("Check pay station for low change")
    return

def send():
    return

def ticket_id(plate, parking):
    try:
        connection = mysql.connector.connect(host='localhost',
                                 database='SmartParking',
                                 user='admin',
                                 password='1234')
        sql_Query = "insert into ticket (idticket, state, active_time, plate, parking) values (default, 'not payed', NOW(), %s,%s)"
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_Query, (plate, parking))
        sql_Query = "select plate from ticket"
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_Query)
        record = cursor.fetchall()
        for row in record:
            print row[0]
    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return

def check_availability():
    try:
        connection = mysql.connector.connect(host='localhost',
                                 database='SmartParking',
                                 user='admin',
                                 password='1234')
        sql_Query = "select idspot from spot where spot_state=0 "
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_Query)
        record = cursor.fetchall()
    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return False if not record else True

def find_nearest_parking():
    return

def check_state(sensor):
    return True if sensor==1 else False

def reserve_spot(plate, name, type):
    if type=="temporary":
        try:
            connection = mysql.connector.connect(host='localhost',
                                                   database='SmartParking',
                                                   user='admin',
                                                   password='1234')
            sql_Query = "select idspot from spot where spot_state=0"
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_Query)
            record = cursor.fetchone()
            sql_Query = "update spot SET `plate`=%s, `spot_state`=1, `spot_type`='temporary' where `idspot`=%s"
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_Query, (plate,record[0]))
            connection.commit()
            sql_Query = "select idspot, spotname, parking from spot where idspot=%s"
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_Query, (record[0],))
            data = cursor.fetchone()
            sql_Query = "insert into history values (default, %s ,%s , NOW(), %s, %s, %s)"
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_Query, (plate,name,data[2],data[0],data[1]))
            connection.commit()
        except Error as e:
            print ("Error while connecting to MySQL", e)
        finally:
              # closing database connection.
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        return
    elif type=="monthly":
        try:
              connection = mysql.connector.connect(host='localhost',
                                                     database='SmartParking',
                                                     user='admin',
                                                     password='1234')
              sql_Query = "select idspot from spot where spot_state=0"
              cursor = connection.cursor(buffered=True)
              cursor.execute(sql_Query)
              record = cursor.fetchone()
              sql_Query = "update spot SET `plate`=%s, `spot_state`=1, `spot_type`='monthly', `monthly`=date_add(now(), interval 30 day) where `idspot`=%s"
              cursor = connection.cursor(buffered=True)
              cursor.execute(sql_Query, (plate,record[0]))
              connection.commit()
              sql_Query = "select idspot, spotname, parking from spot where idspot=%s"
              cursor = connection.cursor(buffered=True)
              cursor.execute(sql_Query, (record[0],))
              data = cursor.fetchone()
              sql_Query = "insert into history values (default, %s ,%s , NOW(), %s, %s, %s)"
              cursor = connection.cursor(buffered=True)
              cursor.execute(sql_Query, (plate,name,data[2],data[0],data[1]))
              connection.commit()
        except Error as e:
              print ("Error while connecting to MySQL", e)
        finally:
              # closing database connection.
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        return
    elif type=="monthly":
        try:
              connection = mysql.connector.connect(host='localhost',
                                                     database='SmartParking',
                                                     user='admin',
                                                     password='1234')
              sql_Query = "select idspot from spot where spot_state=0"
              cursor = connection.cursor(buffered=True)
              cursor.execute(sql_Query)
              record = cursor.fetchone()
              sql_Query = "update spot SET `plate`=%s, `spot_state`=1, `spot_type`='temporary', where `idspot`=%s"
              cursor = connection.cursor(buffered=True)
              cursor.execute(sql_Query, (plate,record[0]))
        except Error as e:
              print ("Error while connecting to MySQL", e)
        finally:
            # closing database connection.
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        return

def check_login(name, password, type):
    try:
        connection = mysql.connector.connect(host='localhost',
                                           database='SmartParking',
                                           user='admin',
                                           password='1234')
        if type=="ADMIN":sql_Query = "select * from ADMIN where name=%s and password=%s"
        elif type=="USER": sql_Query = "select * from USER where name=%s and password=%s"
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_Query, (name,password))
        record = cursor.fetchall()
        state=str(record)
    except Error as e:
        print ("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if (connection.is_connected()):
          cursor.close()
          connection.close()
          print("MySQL connection is closed")
    return False if state =="[]" else True

def check_and_cancel(name):
    try:
        connection = mysql.connector.connect(host='localhost',
                                           database='SmartParking',
                                           user='admin',
                                           password='1234')
        sql_Query = "select `id`,`id_spot` from `history` where `name`=%s order by `date` desc"
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_Query, (name,))
        record = cursor.fetchone()
        id=record[0]
        spotid=record[1]
        print id
        sql_Query = "delete from `history` where `id`=%s"
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_Query, (id,))
        sql_Query = "update spot set `plate`=NULL, `spot_state`=0, `spot_type`=NULL, `monthly`=NULL where idspot=%s"
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_Query, (spotid,))
        connection.commit()
    except Error as e:
        print ("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if (connection.is_connected()):
          cursor.close()
          connection.close()
          print("MySQL connection is closed")
    return

def report_violation():
    return "alert"

def update(spot):
    import mysql.connector
    from mysql.connector import Error
    try:
          connection = mysql.connector.connect(host='localhost',
                                               database='SmartParking',
                                               user='admin',
                                               password='1234')
          sql_Query = "delete from spot where spotname=%s"
          cursor = connection.cursor(buffered=True)
          cursor.execute(sql_Query, (spot,))
    except Error as e:
          print ("Error while connecting to MySQL", e)
    finally:
          # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return

def insert(str):
    if str=="sub":
        spot = raw_input("Enter number of spots to delete")
    if str=="add":
        spot = raw_input("Enter number of spots to add")
    var = spot + str
    return var

def show(parking):
    try:
        connection = mysql.connector.connect(host='localhost',
                                 database='SmartParking',
                                 user='admin',
                                 password='1234')
        sql_Query = "select spotname from spot where parking=%s"
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_Query, (parking, ))
        record = cursor.fetchall()
    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return record

def payment_ok():
    return True

def payment_failure():
    return False

def send_selected(spot):
    return spot

def spot_id(spotname, parking):
    try:
        connection = mysql.connector.connect(host='localhost',
                                 database='SmartParking',
                                 user='admin',
                                 password='1234')
        sql_Query = "select idspot from spot where spotname=%s and parking=%s"
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_Query, (spotname, parking))
        record = cursor.fetchone()
    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return record[0]


av = request("history", "Babis")
# av = check_and_cancel("John")
print av
