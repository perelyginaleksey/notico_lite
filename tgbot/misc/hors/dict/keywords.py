from typing import List


class Keywords:

    AFTER = ['через', 'in']
    AFTER_POSTFIX = ['спустя', 'later']
    PREVIOUS_POSTFIX = ['назад', 'ago']
    NEXT = ['следующий', 'будущий', 'next']
    PREVIOUS = ['прошлый', 'прошедший', 'предыдущий', 'last', 'previous']
    CURRENT = ['этот', 'текущий', 'нынешний', 'current', 'this']
    CURRENT_NEXT = ['ближайший', 'грядущий', 'upcoming', 'nearest']

    TODAY = ['сегодня', 'today']
    TOMORROW = ['завтра', 'tomorrow']
    AFTER_TOMORROW = ['послезавтра', 'day after tomorrow', 'the day after tomorrow']
    YESTERDAY = ['вчера', 'yesterday']
    BEFORE_YESTERDAY = ['позавчера', 'day before yesterday']

    HOLIDAY = ['выходной', 'holiday']

    SECOND = ['секунда', 'сек', 'second', 'sec', 'seconds']
    MINUTE = ['минута', 'мин', 'minute', 'min', 'minutes']
    HOUR = ['час', 'ч', 'hour', 'hr', 'hours']

    DAY = ['день', 'day', 'days']
    WEEK = ['неделя', 'week', 'weeks']
    MONTH = ['месяц', 'мес', 'month', 'months']
    YEAR = ['год', 'year', 'years']

    NOON = ['полдень', 'noon']
    MORNING = ['утро', 'morning', 'am', 'a.m.']
    EVENING = ['вечер', 'evening', 'pm', 'p.m.' ]
    NIGHT = ['ночь', 'night']

    HALF = ['половина', 'пол', 'half']
    QUARTER = ['четверть', 'quarter']

    DAY_IN_MONTH = ['число', 'date']

    JANUARY = ['январь', 'янв', 'january', 'jan']
    FEBRUARY = ['февраль', 'фев', 'february', 'feb']
    MARCH = ['март', 'мар', 'march', 'mar']
    APRIL = ['апрель', 'апр', 'april', 'apr']
    MAY = ['май', 'мая', 'may']
    JUNE = ['июнь', 'июн', 'june', 'jun']
    JULY = ['июль', 'июл', 'july', 'jul']
    AUGUST = ['август', 'авг', 'august', 'aug']
    SEPTEMBER = ['сентябрь', 'сен', 'сент', 'september', 'sep']
    OCTOBER = ['октябрь', 'окт', 'october', 'oct']
    NOVEMBER = ['ноябрь', 'ноя', 'нояб', 'november', 'nov']
    DECEMBER = ['декабрь', 'дек', 'december', 'dec']

    MONDAY = ['понедельник', 'пн', 'monday', 'mon']
    TUESDAY = ['вторник', 'вт', 'tuesday', 'tue']
    WEDNESDAY = ['среда', 'ср', 'wednesday', 'wed']
    THURSDAY = ['четверг', 'чт', 'thursday', 'thu']
    FRIDAY = ['пятница', 'пт', 'friday', 'fri']
    SATURDAY = ['суббота', 'сб', 'saturday', 'sat']
    SUNDAY = ['воскресенье', 'вс', 'sunday', 'sun']

    DAYTIME_DAY = ['днём', 'днем', 'daytime', 'noon']
    TIME_FROM = ['в', 'с', 'from', 'at', 'for', 'the', 'on']
    TIME_TO = ['до', 'по', 'to', 'until']
    TIME_ON = ['на', 'on', 'for', 'the']

    @staticmethod
    def months() -> List[List[str]]:
        return [
            Keywords.JANUARY,
            Keywords.FEBRUARY,
            Keywords.MARCH,
            Keywords.APRIL,
            Keywords.MAY,
            Keywords.JUNE,
            Keywords.JULY,
            Keywords.AUGUST,
            Keywords.SEPTEMBER,
            Keywords.OCTOBER,
            Keywords.NOVEMBER,
            Keywords.DECEMBER
        ]

    @staticmethod
    def days_of_week() -> List[List[str]]:
        return [
            Keywords.MONDAY,
            Keywords.TUESDAY,
            Keywords.WEDNESDAY,
            Keywords.THURSDAY,
            Keywords.FRIDAY,
            Keywords.SATURDAY,
            Keywords.SUNDAY
        ]