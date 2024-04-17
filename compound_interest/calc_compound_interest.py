





def calc_amount(principle,rate,frequency,time_interval):
    amount = principle * (1+(rate/100)/frequency)**(frequency*time_interval)
    return round(amount,2)

def calc_profit(principle,rate,frequency,time_interval):
    profit = calc_amount(principle,rate,frequency,time_interval) - principle
    return round(profit,2)

def calc_profit_percent(principle,rate,frequency,time_interval):
    profit = calc_profit(principle,rate,frequency,time_interval)
    percent = ((profit)/principle) * 100
    return round(percent,2)

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
if __name__ == "__main__":
    def main():
        print(calc_amount(1,7,4,10))
        print(calc_profit(1,7,4,10))
        print(summarize(1,3.5,4,12))
    main()
