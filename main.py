"""

"""

import logging
import NerdGraphClient as NerdGraph
import get_account_details
import CsvFileManager

# Configure logging
logging.basicConfig(
    filename="application.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filemode="w"
)


def main():
    """
    This is the main method for the application. Primary variables and control flow are here.
    :return: No data returned.
    """

    logging.info("Starting the NerdGraph Interactions application.")

    nerdgraph = NerdGraph.NerdGraphClient()

    accounts = get_account_details.get_account_details(nerdgraph)

    print(accounts)

    csv_writer = CsvFileManager.CsvFileManager("accounts.csv")
    csv_writer.write_csv(accounts, as_dict=True)

    logging.info("Finished the NerdGraph Interactions application.")


if __name__ == '__main__':
    main()