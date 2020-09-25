import click
from datetime import date
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
			click.secho(line,nl=1,fg='blue')
			
@click.command()
@click.argument('item')
def create(item):
	''' To create an item '''
	today = date.today()
	todos_file = path[0]+'\nnotes.txt'
	with open(todos_file,'a') as files:
		files.write(f"\n{today}\t{item}")

@click.command()
@click.argument('del_ind',type=int)
def delete(del_ind):
	''' To delete an accidently created item '''
	todos_file = path[0]+'\nnotes.txt'
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
	todos_file = path[0]+'\nnotes.txt'
	compls_file = path[0]+'\ncompleted.txt'
	with open(todos_file,'r') as files:
		lines = files.readlines()
	count=0
	with open(todos_file,'w') as files:
		for line in lines:
			count+=1
			if(count!=comp_ind):
				files.write(line)
			else:
				del_line = line + date.today()
				with open(compls_file,'a') as f:
					f.write(del_line)
				click.secho(f"marked the item {del_line} as completed",fg="green")


start.add_command(list)
start.add_command(create)
start.add_command(delete)
start.add_command(completed)

if __name__ == '__main__':
	start()
