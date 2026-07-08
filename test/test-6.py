#date and time
from datetime import datetime
now = datetime.now()
print(now)

#each line 
print(now.year)
print(now.month)
print(now.day)

#strftime
print(now.strftime)

#in detail
print(now.strftime("%d:%M %p"))