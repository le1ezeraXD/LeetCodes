'''252.会议室
给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，请你判断一个人是否能够参加这里面的全部会议。

 

示例 1：

输入：intervals = [[0,30],[5,10],[15,20]]
输出：false
示例 2：

输入：intervals = [[7,10],[2,4]]
输出：true'''

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    	#按会议开始时间进行排序
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals)-1):
        	#如果这一段会议的结束时间比下一场会议的开始时间要晚
        	#则两场会议有冲突，返回False
            if intervals[i][-1] > intervals[i+1][0]:
                return False

        return True