class entrance_system(system,Mobile_app):
    def __init__(self):

        begin=super.check_state(1)
        if begin == True:

        av=super.check_availability()
        if av==True:
            super.show_msg("Welcome")
            super.show_msg("parking_info")
        else:
            super.show_msg("No availability")
            super.find_nearest_parking()

        return
