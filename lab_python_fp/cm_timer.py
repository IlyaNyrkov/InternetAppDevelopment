import datetime


class cm_timer_1():
    def __init__(self, scope_name):
        self.begin_time = datetime.datetime.now()
        self.scope_name = scope_name
    def __del__(self):
        end_time = datetime.datetime.now()
        print(self.scope_name, 'finished in: ',
              (end_time - self.begin_time).total_seconds(), ' seconds')
