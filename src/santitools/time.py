class Date:
    from datetime import datetime, date as dat
    time = datetime.utcnow()
    def get_time(self, base: int):
        if base == 12:
            return self.time.utcnow().strftime("%I:%M:%S %p")
        elif base == 24:
            return self.time.utcnow().strftime("%H:%M:%S")
        else:
            raise TypeError("Invalid base")
    def get_iso_date(self):
            return self.time.utcnow().isoformat()
    def get_utc_date(self):
            return self.time.utcnow().strftime('%a, %d %b %Y %H:%M:%S %Z')
    def get_unix(self):
        time_tuple = self.time.utcnow().utctimetuple()
        return self.__timestamp__(tuple(time_tuple))
    def refresh(self):
        self.time = self.datetime.utcnow()
        return self
    def __timestamp__(self, tuple):
        EPOCH = 1970
        _EPOCH_ORD = self.dat(EPOCH, 1, 1).toordinal()
        """Unrelated but handy function to calculate Unix timestamp from GMT."""
        year, month, day, hour, minute, second = tuple[:6]
        days = self.dat(year, month, 1).toordinal() - _EPOCH_ORD + day - 1
        hours = days*24 + hour
        minutes = hours*60 + minute
        seconds = minutes*60 + second
        return seconds 
    
    def _abs_(self):
        return self.get_time(24).split(':')
    def get_hours(self):
        return self._abs_()[0]
    def get_minutes(self):
        return self._abs_()[1]
    def get_seconds(self):
        return self._abs_()[2]

class Timer:
    start_time = -1
    end_time = -1
    diff = -1
    def __init__(self):
        # There is no need for logic here.
        pass
    def start(self):
        now = Date()
        self.start_time = now.get_unix()

        return self
    def end(self):
        now = Date()
        self.end_time = now.get_unix()
        self.diff = self.end_time - self.start_time

        return self
    def stop(self):
        return self.end()
class AsyncTimer(Timer):
    async def start(self):
        return super().start()
    async def end(self):
        return super().end()
    async def stop(self):
        return super().stop()
    