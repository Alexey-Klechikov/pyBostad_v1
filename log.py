import telegram_send


class Log:
    def __init__(self, log):
        telegram_send.send(messages=[self.parse_log(log)])

    def parse_log(self, log):

        message = ''

        for row in log:
            site = row.split(': ')[0]
            message += f'{site}\n'

            statuses = row.split('(')[1:]
            for s in statuses:
                message += f'> {s.split(")")[0]}\n'

            message += '\n'

        return message
