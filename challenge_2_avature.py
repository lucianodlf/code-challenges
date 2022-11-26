"""
This code solves a challenge in which you must calculate how many times a 
player "X" can start a game session in a given time range, considering 
that the sessions are enabled only every 15 minutes, these times being 
at [0, 15, 30, 45] minutes.

Time in format HH:MM
TS = Time Start
TE = Time End

Assumptions:
* If end minutes match with [0, 15, 30, 45] does not add of possible game session
* Range of time is [00:00 - 23:59]
"""

def solution(TS, TE):
	"""
	Given data inputs: time start and end time. Returns the amount of 
	game sessions that could be started at specific moments of time equal to 
	0, 15, 30, 45 minutes in each hour, from the start time to end.
	
	Arguments:
	TS (String) in format HH:MM - Time Start.
	TE (String) in format HH:MM - Time End.
	

	Tests:
	>>> solution("00:00", "00:00")
	0

	>>> solution("23:45", "00:45")
	4

	>>> solution("00:00", "23:59")
	96

	>>> solution("20:00", "19:59")
	96

	>>> solution("12:00", "12:01")
	1

	>>> solution("01:05", "03:16")
	9

	>>> solution("14:00", "14:45")
	3

	"""
	# Minutes when is possible start a session of game
	START_SESSIONS = [0, 15, 30, 45]
	
	TIME_START = parse_string_time(TS)
	TIME_END = parse_string_time(TE)
	
	amount_play_sessions = 0

	# Define time start
	count_hours = TIME_START[0]
	count_minutes = TIME_START[1]

	#print(f"Hour(START)={TIME_START[0]}; Minutes(START)={TIME_START[1]} | " +
	#f"Hour(END)={TIME_END[0]}; Minutes(END)={TIME_END[1]}")
	
	while True:
		#print(f'count_hours={count_hours}; count_minutes={count_minutes}')

		# Reach the time limit
		if (count_hours == TIME_END[0] and count_minutes == TIME_END[1]):
			break

		if (count_minutes == 59):
			count_minutes = 0
			count_hours += 1

		if (count_hours == 24):
			count_hours = 0

		if (count_minutes in [0, 15, 30, 45]):
			#print(f'New session is possible! (amount_play_sessions={amount_play_sessions})')
			amount_play_sessions += 1

		count_minutes += 1
	
	return amount_play_sessions



# Return parse string in tuple time with format (HH,MM)
def parse_string_time(string_time):
	return tuple([int(x) for x in string_time.split(':')])



# ================================ Test =======================================

data_test = ("00:00", "00:00")
test = solution(data_test[0], data_test[1])
print(f"TIME_START={data_test[0]} | TIME_END={data_test[1]}")
print(f'Amount of game sessions started = ({test}) - Test:result==0?:' + ("\u274C", "\u2705") [test == 0] + '\n')


data_test = ("23:45", "00:45")
test = solution(data_test[0], data_test[1])
print(f"TIME_START={data_test[0]} | TIME_END={data_test[1]}")
print(f'Amount of game sessions started = ({test}) - Test:result==4?:' + ("\u274C", "\u2705") [test == 4] + '\n')


data_test = ("00:00", "23:59")
test = solution(data_test[0], data_test[1])
print(f"TIME_START={data_test[0]} | TIME_END={data_test[1]}")
print(f'Amount of game sessions started = ({test}) - Test:result==96?' + ("\u274C", "\u2705") [test == 96] + '\n')


data_test = ("20:00", "19:59")
test = solution(data_test[0], data_test[1])
print(f"TIME_START={data_test[0]} | TIME_END={data_test[1]}")
print(f'Amount of game sessions started = ({test}) - Test:result==96?' + ("\u274C", "\u2705") [test == 96] + '\n')


data_test = ("12:00", "12:01")
test = solution(data_test[0], data_test[1])
print(f"TIME_START={data_test[0]} | TIME_END={data_test[1]}")
print(f'Amount of game sessions started = ({test}) - Test:result==1?:' + ("\u274C", "\u2705") [test == 1] + '\n')


data_test = ("01:05", "03:16")
test = solution(data_test[0], data_test[1])
print(f"TIME_START={data_test[0]} | TIME_END={data_test[1]}")
print(f'Amount of game sessions started = ({test}) - Test:result==9?:' + ("\u274C", "\u2705") [test == 9] + '\n')

data_test = ("14:00", "14:45")
test = solution(data_test[0], data_test[1])
print(f"TIME_START={data_test[0]} | TIME_END={data_test[1]}")
print(f'Amount of game sessions started = ({test}) - Test:result==3?:' + ("\u274C", "\u2705") [test == 3] + '\n')
