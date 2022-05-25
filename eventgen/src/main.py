
from config.config_parser import *
from config.utils import *
from sinks import *

if __name__ == '__main__':
    config = get_config()

    printlog("App args: \n{args}".format(args=config))

    # Load data to MySql
    load_data_mysql(config)

    # Send events to kafka
    send_event_kafka(config)
