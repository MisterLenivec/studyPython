"""
Мы сохраняем время присутствия каждого пользователя на уроке  виде интервалов.
В функцию передается словарь, содержащий три списка с таймстемпами
(время в секундах):
— lesson – начало и конец урока
— pupil – интервалы присутствия ученика
— tutor – интервалы присутствия учителя
Интервалы устроены следующим образом – это всегда список из четного количества
элементов. Под четными индексами (начиная с 0) время входа на урок, под нечетными
- время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами и возвращает
время общего присутствия ученика и учителя на уроке (в секундах).
"""


def get_intervals_and_borders(min_val, max_val, intervals):
    if min_val < intervals['lesson'][0] < max_val:
        return intervals['lesson'][0], max_val
    elif min_val < intervals['lesson'][1] < max_val:
        return min_val, intervals['lesson'][1]
    return min_val, max_val


def get_connecting_intervals(t, intervals):
    for timestamps in intervals:
        min_val = intervals[timestamps][0]
        max_val = intervals[timestamps][1]
        if len(intervals[timestamps]) < 3:
            min_val, max_val = get_intervals_and_borders(
                min_val, max_val, intervals)
            t[timestamps].extend([min_val, max_val])

        for i in range(0, len(intervals[timestamps])-1, 2):
            if intervals[timestamps][i] > max_val and i == len(intervals[timestamps])-2:
                t[timestamps].extend([min_val, max_val])
                min_val, max_val = get_intervals_and_borders(
                    intervals[timestamps][i], intervals[timestamps][i + 1], intervals)
                t[timestamps].extend([min_val, max_val])
            elif intervals[timestamps][i] > max_val:
                min_val, max_val = get_intervals_and_borders(min_val, max_val, intervals)
                t[timestamps].extend([min_val, max_val])
                min_val, max_val = get_intervals_and_borders(
                    intervals[timestamps][i], intervals[timestamps][i + 1], intervals)
            if intervals[timestamps][i] < max_val < intervals[timestamps][i + 1]:
                max_val = intervals[timestamps][i + 1]
            min_val, max_val = get_intervals_and_borders(min_val, max_val, intervals)


def remove_and_adjust_intervals(t, t2):
    for timestamps in t:
        for i in range(0, len(t[timestamps])-1, 2):
            if t[timestamps][i] < t['lesson'][0] > t[timestamps][i + 1]:  # До урока
                pass
            elif t[timestamps][i] > t['lesson'][1] < t[timestamps][i + 1]:  # После
                pass
            elif t[timestamps][i] < t['lesson'][0] < t[timestamps][i + 1]:  # Начало
                t2[timestamps].extend([t['lesson'][0], t[timestamps][i + 1]])
            elif t[timestamps][i] > t['lesson'][0] > t[timestamps][i + 1]:  # Конец
                t2[timestamps].extend([t[timestamps][i], t['lesson'][1]])
            else:
                t2[timestamps].extend([t[timestamps][i], t[timestamps][i + 1]])  # Во время


def get_total_time(t2):
    events = []
    cnt = 0
    start = -1
    time = 0

    for timestamps in t2.values():
        for i, stamp in enumerate(timestamps):
            events.append((stamp, 1 - 2*(i % 2)))  # +-1 для чётного и нечетного индекса

    for event in sorted(events):
        cnt += event[1]
        if cnt == 3:
            start = event[0]
        if cnt == 2 and start > 0:
            time += event[0] - start
            start = -1

    return time


def appearance(intervals):
    t = {'lesson': [], 'pupil': [], 'tutor': []}
    t2 = {'lesson': [], 'pupil': [], 'tutor': []}

    get_connecting_intervals(t, intervals)
    remove_and_adjust_intervals(t, t2)
    return get_total_time(t2)


tests = [
    {'data': {
        'lesson': [1594663200, 1594666800],
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
    }, 'answer': 3117},
    {'data': {
        'lesson': [1594702800, 1594706400],
        'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513,
                  1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009,
                  1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773,
                  1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                  1594706524, 1594706524, 1594706579, 1594706641],
        'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
    }, 'answer': 3577},
    {'data': {
        'lesson': [1594692000, 1594695600],
        'pupil': [1594692033, 1594696347],
        'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
    }, 'answer': 3565},
]


if __name__ == '__main__':
    for idx, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], \
            f'Error on test case {idx}, got {test_answer}, expected {test["answer"]}'
