import logging
import ggt

logging.basicConfig(
    handlers=[
                logging.FileHandler(filename="runtime.log", encoding='utf-8', mode='a+')
             ],
    format="%(asctime)s %(name)s:%(levelname)s:%(filename)s:%(lineno)d：%(message)s",
    datefmt="%F %A %T",
    level=logging.INFO)


if __name__ == "__main__":
    ggt.update() 