"""
author -Maruti Bhosale
date -16-11-2020
time -11:30
package -logical_programs
Statement -program for stop watch

"""


class StopWatch:

    def inputStartTime(self):
        """
        taking input for start hour,start minutes and start seconds
        :return: addition all seconds
        """
        while True:
            try:
                hoursStart = int(input("Enter starting hour between 1-24: "))
                minutesStart = int(input("Enter starting minutes between 1-59: "))
                secondStart = int(input("Enter starting seconds between 1-59: "))
                if hoursStart not in range(1, 25) or (minutesStart or secondStart) not in range(1, 60):
                    print("Enter number should be in mention range")
                    continue
                break
            except Exception as e:
                print(e)

        return (hoursStart*60*60) + (minutesStart * 60) + secondStart

    def inputEndTime(self):
        """taking input for end hour,end minutes and end seconds
        :return: return addition of all seconds
        """
        while True:
            try:
                hoursEnd = int(input("Enter ending hour between 1-24: "))
                minutesEnd = int(input("Enter ending minutes between 1-60: "))
                secondEnd = int(input("Enter ending seconds between 1-60: "))
                if hoursEnd not in range(1, 25) or (minutesEnd or secondEnd) not in range(1,60):
                    print("Enter numbers should be in mention range")
                    continue
                break
            except Exception as e:
                print(e)

        return (hoursEnd*60*60)+(minutesEnd*60)+secondEnd

    def findElapseTime(self, totalEndSecond, totalStartSecond):
        """
        finding elapsed time between start and end time
        :return: returns elapse time
        """
        totalTimeDiff = totalEndSecond - totalStartSecond
        minutes = totalTimeDiff//60
        seconds = totalTimeDiff % 60
        hours = 0
        if minutes > 59:
            hours = minutes//60
            minutes = minutes % 60
        return str(hours)+':'+str(minutes)+':'+str(seconds)


if __name__ == "__main__":
    stopWatch = StopWatch()
    startTime = stopWatch.inputStartTime()
    endTime = stopWatch.inputEndTime()
    elapseTime = stopWatch.findElapseTime(endTime, startTime)
    print("Elapse time is: ", elapseTime)
