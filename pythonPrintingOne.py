def main():

	print('Printing a String Literal using a Variable')
	words = 'String Literal Stored in a Variable'
	print(words)

	print('Printing an Integer Literal: ', end=' ')
	print(50)
	value = 100
	print('Printing a Number using a Variable')


	print('Printing a String Literal using a User Input')
	words = input('Enter a String: ')
	print(f'You Entered: {words}')

	print('Printing an Integer Literal using User Input: ')
	value = int(input('Enter an Integer: '))
	print(f'You Entered: {value}')

if __name__ == '__main__':

	main()