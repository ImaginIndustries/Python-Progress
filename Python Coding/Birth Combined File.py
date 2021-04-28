birth_stone = ['Garnet', 'Amethyst', 'Aquamarine', 'Diamond', 'Emerald', 'Alexandrite', 'Ruby', 'Peridot', 'Sapphire', 'Opal', 'Topaz','Blue Topaz' ]
birth_month = ['Jan', 'Feb', 'March', 'April', 'May' , 'June', 'July', 'August', 'September', 'October', 'November', 'December']
zodiac_animal = ['Dog', 'Sheep', 'Rat', 'Oxen', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster']

print(birth_month)
ans = input('What is your birth month?')
if ans == 'Jan':
    print('Your birth stone is '  +  birth_stone[0])
    your_birth_stone = birth_stone[0]
elif ans =='Feb':
    print('Your birth stone is '   +  birth_stone[1])
    your_birth_stone = birth_stone[1]
elif ans == 'March':
    print('Your birth stone is '   +  birth_stone[2])
elif ans == 'April':
    print('Your birth stone is '   +  birth_stone[3])
elif ans == 'May':
    print('Your birth stone is '   +  birth_stone[4])
elif ans == 'June':
    print('Your birth stone is '   +  birth_stone[5])
elif ans == 'July':
    print('Your birth stone is '   +  birth_stone[6])
elif ans == 'August':
    print('Your birth stone is '   +  birth_stone[7])
    print('Congrats we share the same birth month')
    year = input('what year were you born?')
    birth_year = int(year)
    if birth_year == 2030 or 2018 or 2006 or 1994 or 1982:
        print(' Your Zodiac Animal is a ' + zodiac_animal[0])
    if birth_year == 2031 or 2019 or 2007 or 1995 or 1983:
     print(' Your Zodiac Animal is a ' + zodiac_animal[1])
    if birth_year == 2020 or 2008 or 1996 or 1984 or 1972:
        print(' Your Zodiac Animal is a ' + zodiac_animal[2])
    if birth_year == 2021 or 2009 or 1997 or 1985 or 1973:
        print(' Your Zodiac Animal is a ' + zodiac_animal[3])
    if birth_year == 2022 or 2010 or 1998 or 1986 or 1974:
        print(' Your Zodiac Animal is a ' + zodiac_animal[4])
    if birth_year == 2023 or 2011 or 1999 or 1987 or 1975:
        print(' Your Zodiac Animal is a ' + zodiac_animal[5])
    if birth_year == 2024 or 2012 or 2000 or 1988 or 1976:
        print(' Your Zodiac Animal is a ' + zodiac_animal[6])
    if birth_year == 2025 or 2013 or 2001 or 1989 or 1977:
        print(' Your Zodiac Animal is a ' + zodiac_animal[7])
    if birth_year == 2026 or 2014 or 2002 or 1990 or 1978:
        print(' Your Zodiac Animal is a ' + zodiac_animal[8])
    if birth_year == 2027 or 2015 or 2003 or 1991 or 1979:
        print(' Your Zodiac Animal is a ' + zodiac_animal[9])
    if birth_year == 2028 or 2016 or 2004 or 1992 or 1980:
        print(' Your Zodiac Animal is a ' + zodiac_animal[10])
    if birth_year == 2029 or 2017 or 2005 or 1993 or 1981:
        print(' Your Zodiac Animal is a ' + zodiac_animal[11])

elif ans == 'September':
    print('Your birth stone is '   +  birth_stone[8])
elif ans == 'October':
    print('Your birth stone is '   +  birth_stone[9])
    print('Happy Halloween Month!!!')
elif ans == 'November':
    print('Your birth stone is '   +  birth_stone[10])
elif ans == 'December':
    print('Your birth stone is '   +  birth_stone[11])
print(zodiac_animal)

year = input('what year were you born?')
birth_year = int(year)
if birth_year == 2030 or 2018 or 2006 or 1994 or 1982:
    print(' Your Zodiac Animal is a ' + zodiac_animal[0])

if birth_year == 2031 or 2019 or 2007 or 1995 or 1983:
    print(' Your Zodiac Animal is a ' + zodiac_animal[1])

if birth_year == 2020 or 2008 or 1996 or 1984 or 1972:
    print(' Your Zodiac Animal is a ' + zodiac_animal[2])

if birth_year == 2021 or 2009 or 1997 or 1985 or 1973:
    print(' Your Zodiac Animal is a ' + zodiac_animal[3])

if birth_year == 2022 or 2010 or 1998 or 1986 or 1974:
    print(' Your Zodiac Animal is a ' + zodiac_animal[4])

if birth_year == 2023 or 2011 or 1999 or 1987 or 1975:
    print(' Your Zodiac Animal is a ' + zodiac_animal[5])

if birth_year == 2024 or 2012 or 2000 or 1988 or 1976:
    print(' Your Zodiac Animal is a ' + zodiac_animal[6])

if birth_year == 2025 or 2013 or 2001 or 1989 or 1977:
    print(' Your Zodiac Animal is a ' + zodiac_animal[7])

if birth_year == 2026 or 2014 or 2002 or 1990 or 1978:
    print(' Your Zodiac Animal is a ' + zodiac_animal[8])

if birth_year == 2027 or 2015 or 2003 or 1991 or 1979:
    print(' Your Zodiac Animal is a ' + zodiac_animal[9])

if birth_year == 2028 or 2016 or 2004 or 1992 or 1980:
    print(' Your Zodiac Animal is a ' + zodiac_animal[10])
    
if birth_year == 2029 or 2017 or 2005 or 1993 or 1981:
    print(' Your Zodiac Animal is a ' + zodiac_animal[11])
