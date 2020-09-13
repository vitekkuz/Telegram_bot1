import requests
import lxml.html


pages = [["Main page", "https://tv.yandex.ru/?date=2020-09-05&period=now"],
         ["History", "https://tv.yandex.ru/channel/history-1104"],
         ["СТС", "https://tv.yandex.ru/channel/sts-8"],
         ["РЕН ТВ", "https://tv.yandex.ru/channel/ren-30"],
         ["ТВ-3", "https://tv.yandex.ru/channel/tv-3-17"],
         ["ТНТ", "https://tv.yandex.ru/channel/tnt-33"]]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/81.0.4044.113 YaBrowser/20.4.1.225 Yowser/2.5 \
    Yptp/1.23 Safari/537.36',
    'accept': '*/*'}


def get_xml(url, params=None):
    session = requests.Session()
    response = session.get(url, headers=HEADERS, params=params)
    return response


def parse(url):
    response = get_xml(url=url)

    tree = lxml.html.document_fromstring(response.text)
    all_schedule = tree.xpath(
        '//*[@class="channel-schedule__list"]')[0]
    all_events = all_schedule.xpath('./li[position()<4]')

    two_events = get_two_closest_event(all_events)

    # Output
    for i in range(0, len(two_events)):
        print(two_events[i])


def get_two_closest_event(event: list) -> list:
    list_program = []
    # list_program = [['title', 'start', 'end', 'url']]

    for i in range(0, len(event)):
        event_url = event[i].xpath('./a/@href')[0]
        event_time_start = event[i].xpath('./time/text()')[0]
        if len(list_program) > 0:
            list_program[len(list_program)-1][2] = event_time_start
        event_title = event[i].xpath('./div/h3/span[1]/text()')[0]

        list_program.append([event_title, event_time_start, '0', 'https://tv.yandex.ru/' + event_url])
    del list_program[-1]

    return list_program


def main():
    for i in range(1, len(pages)):
        parse(url=pages[i][1])
        print('\n')


if __name__ == "__main__":
    main()
