class Call(object):
    def __init__(self, unique_id, caller_name, caller_phonenumber, time_of_call, reason):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phonenumber = caller_phonenumber
        self.time_of_call = time_of_call
        self.reason = reason
    def display(self):
        print "Unique ID:", self.unique_id
        print "Caller Name:", self.caller_name
        print "Caller Phone Number:", self.caller_phonenumber
        print "Time of call:", self.time_of_call
        print "Reason for call:", self.reason

call1 = Call("1", "Masato", "555-555-5555", "10PM", "Reason 1").display()
call2 = Call("2", "Cindy", "555-777-7777", "11PM", "Reason 2").display()

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue= len(self.calls)
    def new_call(self, incomming):
        self.calls.append(incomming)
        return self
        #add call to the end of call list
    def remove(self):
        self.calls.pop(0)
        return self
        #removes call from the beginning of the list(index 0)
    def info(self):
        for queue in self.calls:
            print queue.caller_name
            print queue.caller_phonenumber

        print "Queue is currently:", len(self.calls)
        #shows name and phone number for each call in the queue as well as length of queue

center1 = CallCenter().new_call(Call("1", "Bob", "777-777-7777", "11PM", "Reason 2")).new_call(Call("2", "Bob", "777-777-7777", "11PM", "Reason 2")).info()
