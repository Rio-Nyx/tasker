import click
from datetime import date
 
@click.group()
def start():
	pass
	
@click.command()
#@click.argument('file_name', type=click.File('r'))
def list():
	counter = 0
	with open ('notes.txt','r') as files:
		for line in files:
			line=line.rstrip()
			counter += 1
			click.echo(line)
			
@click.command()
@click.argument('item')
def create(item):
	today = date.today()
	with open('notes.txt','a') as files:
		files.write(f"\n{today}\t{item}")

@click.command()
@click.argument('del_ind',type=int)
def delete(del_ind):
	with open('notes.txt','r') as files:
		lines = files.readlines()
	count=0
	with open('notes.txt','w') as files:
		for line in lines:
			count+=1
			if(count!=del_ind):
				files.write(line)
			else:
				click.echo(f"deleted the item {line}")

start.add_command(list)
start.add_command(create)
start.add_command(delete)

if __name__ == '__main__':
	start()

