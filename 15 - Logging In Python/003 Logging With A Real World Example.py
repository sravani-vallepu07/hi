import logging 
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app5.log"),
        logging.StreamHandler()
    ]
)
logger=logging.getLogger("arthematicapp")
def add(a,b):
    result=a+b
    logger.debug(f"adding {a}+{b}={result}")
    return result
def sub(a,b):
    result=a+b
    logger.debug(f"subtracting {a}+{b}={result}")
    return result
def mul(a,b):
    result=a*b
    logger.debug(f"multiplicating {a}*{b}={result}")
    return result
def div(a,b):
    try:
        result=a/b
        logger.debug(f"div {a}+{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("division by zero")
        return None
add(10,15)
sub(15,10)
mul(10,20)
div(20,10)