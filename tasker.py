# This program was created to simply save todo list to a file named notes.txt and completed liat to completed.txt
# displays contents of each list.
# used click so that we dont have to worry about invalid commmands and easy cli for the user

import click
from datetime import datetime
from sys import path

@click.group()
def start():
	''' Commandline todo manager '''
	pass
	
@click.command()
#@click.argument('file_name', type=click.File('r'))
@click.option('--c/--l',default=True)
def list(c):
	''' To list the todo items '''
	if c:
		file_name = path[0]+'/notes.txt'
	else:
		file_name = path[0]+'/completed.txt'
	counter = 0
	with open (file_name,'r') as files:
		for line in files:
			line=line.rstrip()
			counter += 1
			click.secho(f"{counter} {line}",nl=1,fg='blue')
			
@click.command()
@click.argument('item')
def create(item):
	''' To create an item '''
	#today = date.today()
	today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	todos_file = path[0]+'/notes.txt'
	with open(todos_file,'a') as files:
		files.write(f"{today}\t{item}\n")

@click.command()
@click.argument('del_ind',type=int)
def delete(del_ind):
	''' To delete an accidently created item '''
	todos_file = path[0]+'/notes.txt'
	with open(todos_file,'r') as files:
		lines = files.readlines()
	count=0
	with open(todos_file,'w') as files:
		for line in lines:
			count+=1
			if(count!=del_ind):
				files.write(line)
			else:
				del_line = line
				click.secho(f"deleted the item {del_line}",fg="red")

@click.command()
@click.argument('comp_ind',type=int)
def completed(comp_ind):
	''' Mark an item as completed '''
	todos_file = path[0]+'/notes.txt'
	compls_file = path[0]+'/completed.txt'
	with open(todos_file,'r') as files:
		lines = files.readlines()
	count=0
	with open(todos_file,'w') as files:
		for line in lines:
			count+=1
			if(count!=comp_ind):
				files.write(line)
			else:
				del_line = line
				#today = date.today()
				today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				with open(compls_file,'a') as f:
					f.write(f"{del_line} {today}")
				del_line = del_line.strip()
				click.secho(f"marked the item \t{del_line} as completed",fg="green")


start.add_command(list)
start.add_command(create)
start.add_command(delete)
start.add_command(completed)

if __name__ == '__main__':
	start()
