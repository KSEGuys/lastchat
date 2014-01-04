import datetime

class message:
    '''
        message
    '''
    def __init__(self):
        self.name = ''
        self.timestamp = datetime.datetime.now()
        self.content = 'This is a test message'
        self.styleClass = ''

    @classmethod
    def sample(cls):
        results = []
        for i in range(1,10):
            a = cls()
            a.name = 'user' + str(i)
            a.content = 'Test message' + str(i)
            if i%3 == 0:
                a.styleClass = 'self'
            results.append(a)
        return results

