from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from calendar import isleap


years_limit = 990
for year in range(1006, 1996, 10):
    dt = datetime(year, 1, 26)
    
    if (dt.strftime('%w') == '1') and isleap(year):
        print(dt)
    dt = dt + relativedelta(years=-1)
    years_limit -= 1

# whom?
# <!-- he ain't the youngest, he is the second -->
# <!-- todo: buy flowers for tomorrow -->
# https://www.onthisday.com/date/1756/january/27 
print("https://www.onthisday.com/date/1756/january/27")
print("mozart")
