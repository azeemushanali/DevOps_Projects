import logging
import string
import sys

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pangram_check.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

def is_pangram(commit_message):
    """Check if a given string is a pangram."""
    try:
        # Convert the string to lowercase and create a set of characters
        commit_message = commit_message.lower()
        # Use a set of all the lowercase alphabets
        alphabet_set = set(string.ascii_lowercase)

        # Create a set of the characters in the input string
        s_set = set(commit_message)

        # Check if all alphabets are present in the string
        if alphabet_set.issubset(s_set):
            logging.info(f"The commit message is a pangram: '{commit_message}'")
            return True
        else:
            logging.warning(f"The commit message is NOT a pangram: '{commit_message}'")
            return False

    except Exception as e:
        logging.error(f"Error occurred while checking the commit message: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logging.error("Invalid number of arguments. Usage: python check_pangram.py '<commit_message>'")
        sys.exit(1)

    commit_message = sys.argv[1]
    is_pangram(commit_message)
