import re

kill =       '((?:(?:[0-1][0-9])|(?:[2][0-3])|(?:[0-9])):(?:[0-5][0-9])(?::[0-5][0-9])?(?:\\s?(?:am|AM|pm|PM))?).*?Player.*?(".*?").*?id=(\\d+).*?has been killed by.*?player.*?(".*?").*?id=(\\d+)'
connect =    '((?:(?:[0-1][0-9])|(?:[2][0-3])|(?:[0-9])):(?:[0-5][0-9])(?::[0-5][0-9])?(?:\\s?(?:am|AM|pm|PM))?).*?Player.*?(".*?").*?is connected.*?id=(\\d+)'
disconnect = '((?:(?:[0-1][0-9])|(?:[2][0-3])|(?:[0-9])):(?:[0-5][0-9])(?::[0-5][0-9])?(?:\\s?(?:am|AM|pm|PM))?).*?Player.*?(".*?").*?id=(\\d+).*?has been disconnected'
day =        'AdminLog started on ((?:(?:[1]{1}\\d{1}\\d{1}\\d{1})|(?:[2]{1}\\d{3}))[-:\\/.](?:[0]?[1-9]|[1][012])[-:\\/.](?:(?:[0-2]?\\d{1})|(?:[3][01]{1})))(?![\\d]) at ((?:(?:[0-1][0-9])|(?:[2][0-3])|(?:[0-9])):(?:[0-5][0-9])(?::[0-5][0-9])?(?:\\s?(?:am|AM|pm|PM))?)'

kill_c = re.compile(kill,re.IGNORECASE|re.DOTALL)
connect_c = re.compile(connect,re.IGNORECASE|re.DOTALL)
disconnect_c = re.compile(disconnect,re.IGNORECASE|re.DOTALL)
day_c = re.compile(day,re.IGNORECASE|re.DOTALL)