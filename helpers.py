import re


ticker_regex = re.compile(r'\$(?P<ticker>[A-Za-z]+)')

def find_ticker(haystack: str):
    needle = ticker_regex.search(haystack)
    return None if needle is None else needle.group('ticker').upper()[:10]
