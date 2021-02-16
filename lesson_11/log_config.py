import logging
import sys

logging.basicConfig(
    filename = "info.log",
    format = "%(levelname)-10s %(asctime)s %(message)s",
    level = logging.INFO
)


#чтобы вызвать лог необходимо создать ему имя
log = logging.getLogger("info")

# StreamHandler - вывод в консоль
# stderr - вывод в консоль в ошибки (еще и в консоль в ошибки выводи)
# stdout - обычный вывод в консоль
# stdin - ввод в консоль
log.addHandler(logging.StreamHandler(sys.stderr))
