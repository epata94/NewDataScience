def calc_monthly_salary(annual_salary):
    monthly_pay=annual_salary//12
    print(f"월 급여는 {monthly_pay}입니다.")

monthly_pay=int(input("연봉을 입력하여 주세요 : "))
calc_monthly_salary(monthly_pay)