from chargebee.result import Result


class ListResult(list):

    def __init__(self, response):
        self.response = response

        self._init_items()

    def _init_items(self):
        for item in self.response:
            self.append(Result(item))
