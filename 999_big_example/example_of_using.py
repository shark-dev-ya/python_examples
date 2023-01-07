from time import sleep

from reports.JsonReporter import JsonReporter

if __name__ == '__main__':
    json_reporter = JsonReporter('json_logs')
    json_reporter.log('voltage : 13.34V')
    sleep(1)
    json_reporter.log_list([123, 445, 54353])
    sleep(1)
    json_reporter.log_dict(magickey='magic value', anotherKey=13, third_key=53.5465)
    json_reporter.print()
