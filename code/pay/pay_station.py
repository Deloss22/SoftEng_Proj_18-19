class pay_station(system, exit_system):
    def __init__(self):
        pass

    def check(): #sinallagma
        c_list=super.request('change')
        for chag in c_list:
            if chag <= 0:
                super.send('low_change') #h send tha kalesei thn alert()
        return
    def check_payment(self,payvariable,ticket_price):
		if payvariable==ticket_price
		return True

    def detect_violation():
        if insertedticket != True and bar_state == 0:
            super.report_violation('Alert! someone left without paying')
        return

	def insert(self,t_input,payment):
		if self.t_input==True:
			q=super.request("ticket_price")
			super.show_msg('q')
			u=check_payment(payment,q)
			if u==True:
				super.update(ticket)
			elif
				super.payment_failure()
				super.show_msg("Είσαγετε το κατάλληλο ποσό πληρωμής")
        return
