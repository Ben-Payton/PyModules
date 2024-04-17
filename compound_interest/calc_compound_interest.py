#########################################################################################################################
# This module is meant to contain python functions that will automate the calculation of interest.
#########################################################################################################################



#########################################################################################################################
# Function Name:
#   calc_amount()
# Function Arguments:
#   principle - <float> The ammount of money you start with.
#   rate - <float> The interest rate of the account.
#   frequency - <float> The frequency with which the interest rate is applied per year.
#   time_interval - <float> The number of years the money will be in the account.
# Return:
#   <float> the amount of money you will have in your account at the end of the time_interval.
#########################################################################################################################

def calc_amount(principle,rate,frequency,time_interval):
    amount = principle * (1+(rate/100)/frequency)**(frequency*time_interval)
    return round(amount,2)

#########################################################################################################################
# Function Name:
#   calc_profit()
# Function Arguments:
#   principle - <float> The ammount of money you start with.
#   rate - <float> The interest rate of the account.
#   frequency - <float> The frequency with which the interest rate is applied per year.
#   time_interval - <float> The number of years the money will be in the account.
# Return:
#   <float> the amount of money you will have gained in your account, rounded to the nearest cent at the end of the 
#   time_interval.
#########################################################################################################################

def calc_profit(principle,rate,frequency,time_interval):
    profit = calc_amount(principle,rate,frequency,time_interval) - principle
    return round(profit,2)

#########################################################################################################################
# Function Name:
#   calc_profit_percent()
# Function Arguments:
#   principle - <float> The ammount of money you start with.
#   rate - <float> The interest rate of the account.
#   frequency - <float> The frequency with which the interest rate is applied per year.
#   time_interval - <float> The number of years the money will be in the account.
# Return:
#   <float> the amount of money you will have gained in your account at the end of the time_interval in percentage 
#   rounded to the nearest hudredth of a percent.
#########################################################################################################################

def calc_profit_percent(principle,rate,frequency,time_interval):
    profit = calc_profit(principle,rate,frequency,time_interval)
    percent = ((profit)/principle) * 100
    return round(percent,2)

#########################################################################################################################
# Function Name:
#   summarize()
# Function Arguments:
#   principle - <float> The ammount of money you start with.
#   rate - <float> The interest rate of the account.
#   frequency - <float> The frequency with which the interest rate is applied per year.
#   time_interval - <float> The number of years the money will be in the account.
# Return:
#   <str> A summary of the gains in your account at the end of the time_interval.
#########################################################################################################################

def summarize(principle,rate,frequency,time_interval):
    summary_dict ={
            "principle":principle,
            "rate": rate,
            "frequency": frequency,
            "time_interval": time_interval,
            "amount": calc_amount(principle,rate,frequency,time_interval),
            "profit": calc_profit(principle,rate,frequency,time_interval),
            "profit_percent": calc_profit_percent(principle,rate,frequency,time_interval)
            }
    summary = """
Your ${principle} at {rate}% growth will become ${amount} after {time_interval} years.
This represents {profit_percent}% growth.
    """
    return summary.format(**summary_dict)


#########################################################################################################################
# This section only runs if this is being run as a script.
#########################################################################################################################

if __name__ == "__main__":
    def main():
        principle = float(input("What is your principle amount?: $"))
        rate = float(input("What is the percent interest?: "))
        frequency = float(input("How many times in a year are you given interest?: "))
        time_interval = float(input("How many years are you planning on keeping that money there?: "))
        print(summarize(principle,rate,frequency,time_interval))
    main()
