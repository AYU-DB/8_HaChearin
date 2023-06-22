for i in range(1, 51):
    with open(str(i)+"주차.txt", "w", encoding = "utf-8") as report_file:
        report_file.write("-{0}주차 주간보고-\n" .format(i))
        report_file.write("부서: \n")
        report_file.write("이름: \n")
        report_file.write("요약: \n")