from src.contest.contest import Contest

if __name__ == "__main__":
	contest = Contest(1752)
	contest.selectTask(int(input()))
	print(list(contest.task.tests))