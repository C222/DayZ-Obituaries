import re

kill =       '((?:(?:[0-1][0-9])|(?:[2][0-3])|(?:[0-9])):(?:[0-5][0-9])(?::[0-5][0-9])?(?:\\s?(?:am|AM|pm|PM))?).*?Player.*?(".*?").*?id=(\\d+).*?has been killed by.*?player.*?(".*?").*?id=(\\d+)'
connect =    '((?:(?:[0-1][0-9])|(?:[2][0-3])|(?:[0-9])):(?:[0-5][0-9])(?::[0-5][0-9])?(?:\\s?(?:am|AM|pm|PM))?).*?Player.*?(".*?").*?is connected.*?id=(\\d+)'
disconnect = '((?:(?:[0-1][0-9])|(?:[2][0-3])|(?:[0-9])):(?:[0-5][0-9])(?::[0-5][0-9])?(?:\\s?(?:am|AM|pm|PM))?).*?Player.*?(".*?").*?id=(\\d+).*?has been disconnected'

kill_c = re.compile(kill,re.IGNORECASE|re.DOTALL)
connect_c = re.compile(connect,re.IGNORECASE|re.DOTALL)
disconnect_c = re.compile(disconnect,re.IGNORECASE|re.DOTALL)