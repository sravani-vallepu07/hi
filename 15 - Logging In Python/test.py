import logging  # Correct import

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def add(a, b):
    logging.debug("This addition operation is taking place")
    return a + b

logging.debug("The addition function is called")
result = add(10, 15)
print("Result:", result)  # Optional: Print result
