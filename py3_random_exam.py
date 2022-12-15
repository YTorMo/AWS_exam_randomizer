import json
import time
from random import seed
from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def random_exam():
	seed(int(time.time()))
	num = []
	for _ in range(65):
		value = randint(1, 715)
		num.append(value)
	return num



def check_random(nums):
	check = 0
	i = 0
	j = 0
	for n in nums:
		while i < 65:
			if n == nums[i]:
				j+=1
			i+=1
			if j > 1:
				check = 1
			else:
				j = 0
	return check

def check_answer(c):
	ok = 0
	corr = []
	with open('Answers_correct_dict.JSON') as json_file:
		data = json.load(json_file)
	data_p = str(data[c[1]]).strip().split(' ')
	print(bcolors.HEADER + bcolors.BOLD + 'Correct answer: ' + str(data_p) + bcolors.ENDC)
	if len(data_p) == len(c[0]):
		for r in c[0]:
			for d in data_p:
				if r.upper() == d:
					corr.append(1)
	if len(data_p) == len(corr):
		ok = 1
	return ok

def check_input(answ):
	ok = 1
	i = 0
	for a in answ:
		if len(a) != 1: 
			return 0
		if a.upper() < 'A' or a.upper() > 'F':
			return 0
	for a in answ:
		i = 0
		for b in answ:
			if a == b:
				i += 1
				if i > 1:
					return 0
	return ok

def question_followed_by_answers(data, data2, Ex_quest):
	i = 1
	a_corr = 0
	a_incorr = 0
	for q in Ex_quest:
		print(bcolors.BOLD + bcolors.OKBLUE + str(i) + '. ' + data[str(q)] + bcolors.ENDC)
		answ_r = input(bcolors.OKCYAN + bcolors.BOLD + 'Select your answer:\n' + bcolors.ENDC)
		answ = answ_r.strip().split(' ')
		while check_input(answ) == 0:
			answ_r = input(bcolors.OKCYAN + bcolors.BOLD + 'Incorrect input.\nYou can only choose between A, B, C, D, E, F followed by only 1 space if it is needed\nand you can not repeat answer letters.\nSelect again your answer:\n' + bcolors.ENDC)
			answ = answ_r.strip().split(' ')
		c = [answ, str(q)]
		if check_answer(c) == 1:
			print(bcolors.OKGREEN + bcolors.BOLD + 'CORRECT' + bcolors.ENDC)
			a_corr += 1
		else:
			print(bcolors.FAIL + bcolors.BOLD + 'CAGASTE' + bcolors.ENDC)
			a_incorr += 1
		print(bcolors.BOLD + bcolors.OKGREEN + '\n\n-----------\nEXPLANATION\n-----------\n\n' + bcolors.ENDC)
		print(bcolors.BOLD + bcolors.HEADER + data2[str(q)] + bcolors.ENDC)
		print(bcolors.BOLD + bcolors.HEADER + '\n\nPRESS ENTER TO CONTINUE...' + bcolors.ENDC)
		input()
		i += 1
	print(bcolors.BOLD + '\n\n\n---------------------------------' + bcolors.ENDC)
	print(bcolors.HEADER + bcolors.BOLD + '********\n*SCORES*\n********' + bcolors.ENDC)
	print(bcolors.BOLD + bcolors.WARNING + 'Your score: ' + str(round((a_corr * 100 / 65), 2))+ '%' + bcolors.ENDC)
	print(bcolors.BOLD + bcolors.OKGREEN + 'Answers correct: ' + str(a_corr) + bcolors.ENDC)
	print(bcolors.BOLD + bcolors.FAIL + 'Answers cagaste: ' + str(a_incorr) + bcolors.ENDC)
	print(bcolors.BOLD + '---------------------------------\n\n\n' + bcolors.ENDC)

def question_first_answers_last(data, data2, Ex_quest):
	i = 1
	a_corr = 0
	a_incorr = 0
	c = []
	j = 0
	for q in Ex_quest:
		print(bcolors.BOLD + bcolors.OKBLUE + str(i) + '. ' + data[str(q)] + bcolors.ENDC)
		answ_r = input(bcolors.OKCYAN + bcolors.BOLD + 'Select your answer:\n' + bcolors.ENDC)
		answ = answ_r.strip().split(' ')
		while check_input(answ) == 0:
			answ_r = input(bcolors.OKCYAN + bcolors.BOLD + 'Incorrect input.\nYou can only choose between A, B, C, D, E, F followed by only 1 space if it is needed\nand you can not repeat answer letters.\nSelect again your answer:\n' + bcolors.ENDC)
			answ = answ_r.strip().split(' ')
		c.append([answ, str(q)])
		i += 1
	print(bcolors.BOLD + bcolors.HEADER + '\n\nFINISHED!!!!!!\n\nPRESS ENTER TO CONTINUE...' + bcolors.ENDC)
	input()
	for q in Ex_quest:
		sc = check_all_answers(c, data2, q , j, data)
		j+=1
		if sc == 'co':
			a_corr+=1
		else:
			a_incorr+=1
	print(bcolors.BOLD + '\n\n\n---------------------------------' + bcolors.ENDC)
	print(bcolors.HEADER + bcolors.BOLD + '********\n*SCORES*\n********' + bcolors.ENDC)
	print(bcolors.BOLD + bcolors.WARNING + 'Your score: ' + str(round((a_corr * 100 / 65), 2))+ '%' + bcolors.ENDC)
	print(bcolors.BOLD + bcolors.OKGREEN + 'Answers correct: ' + str(a_corr) + bcolors.ENDC)
	print(bcolors.BOLD + bcolors.FAIL + 'Answers cagaste: ' + str(a_incorr) + bcolors.ENDC)
	print(bcolors.BOLD + '---------------------------------\n\n\n' + bcolors.ENDC)

def check_all_answers(cont, data2, q, j, data):
	if check_answer(cont[j]) == 1:
		print(bcolors.BOLD + bcolors.FAIL + '\n\n**********\n*QUESTION*\n**********\n\n' + bcolors.ENDC)
		print(bcolors.BOLD + bcolors.OKBLUE + str(j) + '. ' + data[str(q)] + bcolors.ENDC)
		print(bcolors.OKGREEN + bcolors.BOLD + 'CORRECT' + bcolors.ENDC)
		sc = 'co'
		print(bcolors.BOLD + bcolors.OKGREEN + '\n\n-----------\nEXPLANATION\n-----------\n\n' + bcolors.ENDC)
		print(bcolors.BOLD + bcolors.HEADER + data2[str(q)] + bcolors.ENDC)
	else:
		print(bcolors.BOLD + bcolors.FAIL + '\n\n**********\n*QUESTION*\n**********\n\n' + bcolors.ENDC)
		print(bcolors.BOLD + bcolors.OKBLUE + str(j) + '. ' + data[str(q)] + bcolors.ENDC)
		print(bcolors.FAIL + bcolors.BOLD + 'CAGASTE' + bcolors.ENDC)
		sc = 'in'
		print(bcolors.BOLD + bcolors.OKGREEN + '\n\n-----------\nEXPLANATION\n-----------\n\n' + bcolors.ENDC)
		print(bcolors.BOLD + bcolors.HEADER + data2[str(q)] + bcolors.ENDC)
	return sc

if __name__ == "__main__":
	Ex_quest = random_exam()
	while check_random(Ex_quest) == 1:
		Ex_quest = random_exam()
	with open('Questions.json') as json_file:
		data = json.load(json_file)
	with open('Explanations.json') as json_file:
		data2 = json.load(json_file)
	print(bcolors.BOLD + bcolors.WARNING +'\n\nInstructions:\nYou can only choose between characters A, B, C, D, E, F. Program is not case sensitive.\nSelect one of then and press enter.' +
			'\nIn case of multiple choice questions you must write the character of the answer followed only by 1 space.\nExample:\nA C D\n' +
			bcolors.ENDC)
	print(bcolors.BOLD + bcolors.HEADER + '\n\nPRESS ENTER TO CONTINUE...' + bcolors.ENDC)
	input()
	print(bcolors.BOLD + bcolors.WARNING + '\n\nPLEASE SELECT MODE AND PRESS ENTER TO CONTINUE:\n\n\n1. IN THIS MODE YOU ANSWER A QUESTION AND INMEDIATELY YOU KNOW IF IT IS CORRECT AND RECIEVE AN EXPLANATION.'+
	'\n\n2. IN THIS MODE YOU ANSWER ALL QUESTIONS FIRST AND THEN YO RECIBE THE EXPLANATION AND SCORE.' + bcolors.ENDC)
	inp = input()
	while (int(inp) < 1 or int(inp) > 2):
		inp = input(bcolors.BOLD + bcolors.WARNING + '\n\nPLEASE SELECT MODE AND PRESS ENTER TO CONTINUE:\n\n\n1. IN THIS MODE YOU ANSWER A QUESTION AND INMEDIATELY YOU KNOW IF IT IS CORRECT AND RECIEVE AN EXPLANATION.'+
				'\n\n2. IN THIS MODE YOU ANSWER ALL QUESTIONS FIRST AND THEN YO RECIBE THE EXPLANATION AND SCORE.\n' + bcolors.ENDC)
	if(inp == 1):
		question_followed_by_answers(data, data2, Ex_quest)
	else:
		question_first_answers_last(data, data2, Ex_quest)
	

