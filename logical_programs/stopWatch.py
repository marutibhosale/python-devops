"""
author -Maruti Bhosale
date -16-11-2020
time -11:30
package -logical_programs
Statement -program for stop watch

"""


class StopWatch:

    def inputStartTime(self):
        """taking input for start hour,start minutes and start seconds"""
        try:
            hoursStart = int(input("Enter starting hour: "))
            minutesStart = int(input("Enter starting minutes: "))
            secondStart = int(input("Enter starting seconds: "))
        except Exception as e:
            print(e)
            self.inputStartTime()

        if hoursStart > 24:
            print("hours should be between 1 to 24")
            self.inputStartTime()
        if minutesStart > 59 or secondStart > 59:
            print("minutes and seconds both should be between 1 to 59")
            self.inputStartTime()

        self.totalStartSecond = (hoursStart*60*60) + (minutesStart * 60) + secondStart

    def inputEndTime(self):
        """taking input for end hour,end minutes and end seconds"""
        try:
            hoursEnd = int(input("Enter ending hour: "))
            minutesEnd = int(input("Enter ending minutes: "))
            secondEnd = int(input("Enter ending seconds: "))
        except Exception as e:
            print(e)
            self.inputEndTime()

        if hoursEnd > 24:
            print("hours should be between 1 to 24")
            self.inputEndTime()
        if minutesEnd > 59 or secondEnd > 59:
            print("minutes and seconds both should be between 1 to 59")
            self.inputEndTime()
        self.totalEndSecond = (hoursEnd*60*60)+(minutesEnd*60)+secondEnd

    def findElapseTime(self):
        """
        finding elapsed time between start and end time
        :return: returns elapse time
        """
        totalTimeDiff = self.totalEndSecond - self.totalStartSecond
        minutes = totalTimeDiff//60
        seconds = totalTimeDiff % 60
        hours = 0
        if minutes > 59:
            hours = minutes//60
            minutes = minutes % 60
        return str(hours)+':'+str(minutes)+':'+str(seconds)


if __name__ == "__main__":
    stopWatch = StopWatch()
    stopWatch.inputStartTime()
    stopWatch.inputEndTime()
    elapseTime = stopWatch.findElapseTime()
    print("Elapse time is: ", elapseTime)
