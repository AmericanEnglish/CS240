import sqlite3
def display(cursorobj):
	pass


def main():
	con =  sqlite3.connect('census.db')
	cursor = con.cursor()
	cursor.execute("CREATE TABLE Density (province TEXT, population INTEGER, area REAL)")
	cursor.execute("INSERT INTO Density VALUES ('Newfoundland and Labrador', 512930, 370501.69)")
	cursor.execute("INSERT INTO Density VALUES ('Prince Edward Island', 135294, 5684.39)")
	cursor.execute("INSERT INTO Density VALUES ('Nova Scotia', 908007, 52917.43)")
	cursor.execute("INSERT INTO Density VALUES ('New Brunswick', 729498, 71355.67)")
	cursor.execute("INSERT INTO Density VALUES ('Quebec', 7237479, 1357743.08)")
	cursor.execute("INSERT INTO Density VALUES ('Ontario', 11410046, 907655.59)")
	cursor.execute("INSERT INTO Density VALUES ('Manitoba', 1119583, 551937.87)")
	cursor.execute("INSERT INTO Density VALUES ('Saskatchewan', 978933, 586561.35)")
	cursor.execute("INSERT INTO Density VALUES ('Alberta', 2974807, 639987.12)")
	cursor.execute("INSERT INTO Density VALUES ('British Columbia', 3907738, 926492.48)")
	cursor.execute("INSERT INTO Density VALUES ('Yukon Territory', 28674, 474706.97)")
	cursor.execute("INSERT INTO Density VALUES ('Northwest Territories', 37360, 1141108.37)")
	cursor.execute("INSERT INTO Density VALUES ('Nunavut', 26745, 1925460.18)")


if __name__ == '__main__':
	main()