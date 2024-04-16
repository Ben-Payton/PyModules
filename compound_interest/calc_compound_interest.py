





def calc_amount(principle,rate,frequency,time_interval):
    amount = principle * (1+(rate/100)/frequency)**(frequency*time_interval)
    return amount

def calc_profit(principle,rate,frequency,time_interval):
    profit = calc_amount(principle,rate,frequency,time_interval) - principle
    return profit

if __name__ == "__main__":
    def main():
        print(calc_amount(1,7,4,10))
        print(calc_profit(1,7,4,10))
    main()
