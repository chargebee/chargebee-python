from chargebee.result import Result


class ListResult(list):
    
    def __init__(self, response, next_offset, response_header=None):
        self.response = response
        self.next_offset = next_offset
        self._response_header = response_header
        self._init_items()

    def _init_items(self):
        for item in self.response:
            self.append(Result(item))
    
    @property
    def get_response_headers(self):
        return self._response_header
