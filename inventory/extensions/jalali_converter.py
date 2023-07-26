'''
Jalali calender Converter V 0.0.1
Dev : #ABS
'''

from jalali_date import datetime2jalali

def jalali_converter(time):
    # This function returns jalali calendar output
    jmonths = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    time = datetime2jalali(time)
    time_str = time.strftime("%Y, %m, %d, %H,%M,%S")
    time_list = time_str.split(",")

    for index, month in enumerate(jmonths):
        if int(time_list[1]) == index + 1:
            time_list[1] = month
            break

    output = "{} / {} / {}.".format(
        time_list[2],
        time_list[1],
        time_list[0],
    )

    return output

def cardex_jalali_converter(time):
    # This function returns jalali calendar output
    jmonths = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    time = datetime2jalali(time)
    time_str = time.strftime("%Y, %m, %d, %H,%M,%S")
    time_list = time_str.split(",")

    for index, month in enumerate(jmonths):
        if int(time_list[1]) == index + 1:
            time_list[1] = month
            break

    output = "{} / {} / {}.".format(
        time_list[2],
        time_list[1],
        time_list[0],
    )

    return output