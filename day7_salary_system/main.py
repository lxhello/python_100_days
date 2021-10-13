from employee_Class import Manager,Programming,Saleman


def main():
    emps = [
        Manager(1, 'ma'), Programming(2, 'zhang'),
        Programming(3, 'wang'), Programming(4, "li"),
        Saleman(5, "xiao_li"), Saleman(6, "lao_zhang")
    ]
    for emp in emps:
        if type(emp) == Programming:
            emp.work_hour = int(input("enter work_hour:"))
        elif type(emp) == Saleman:
            emp.sale = float(input("enter sale money:"))
        print(f"{emp.name} salary is:{emp.get_salary()}")


if __name__ == "__main__":
    main()
