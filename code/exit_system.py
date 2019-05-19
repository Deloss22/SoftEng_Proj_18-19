class exit_system(ticket,system,bar):
    bar_state = 0 #h 1 analoga me tin periptosi

    def __init__(self,insertedticket):
        if self.insertedticket==True:
            y=super.ticket_indetification('kapio id')
            if y=True:
                ticket_paid=super.check_ticket() #apo to sistima
                if ticket_paid == True:
                	super.open()
                	super.carleft()
                	super.close()
                else: #ticketpaid
        	       super.show_msg("Pay your ticket please")
        else:
         return error

    def check_ticket(self,paid):
        #if self.paid==True:
