import logging
import sys

# 当没有明确配置输出到文件时，信息将会被输出到标准错误输出流中
logging.debug('debug信息')
logging.info('info信息')
# logging模块的默认日志级别为WARNING，所以只会输出大于等于WARNING级别日志日志
# logging模块的日志级别等级：DEBUG(10) < INFO(20) < WARNING(30) < ERROR(40) < FATAL或CRITICAL(50)
logging.warning('warning信息')
logging.error('error信息')
logging.critical('critical信息')


class Log:
    def log_test(self,msg):
        log = logging.getLogger('Console')
        log.setLevel(logging.INFO)
        fmt = logging.Formatter('%(asctime)s %(thread)d %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        console_handler = logging.StreamHandler(sys.stdout)  # 明确指定日志输出到标准输出流中
        console_handler.setFormatter(fmt)
        log.addHandler(console_handler)
        log.info(msg)


# if __name__ == '__main__':
#     Log().log_test("这个是个log")
