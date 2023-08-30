import logging


def get_account_details(nerdgraph_client):
    """
    This function returns a list of accounts for the given API key.
    :param nerdgraph_client: A NerdGraphClient object.
    :return: A dictionary containing the accounts.
    """

    logging.info("Retrieving account details.")

    query_variables = {
        "Scope": "GLOBAL"
    }

    graphql_query = """
    query ($Scope: AccountScope!) {
      actor {
        accounts(scope: $Scope) {
          id
          name
        }
      }
    }
    """

    query_results = nerdgraph_client.send_query(graphql_query, query_variables)
    accounts = process_response(query_results)

    return accounts


def process_response(response):
    account_list = []  # This will be a list of dictionaries containing entity names and GUIDs

    accounts = response["data"]["actor"]["accounts"]

    try:
        for account in accounts:
            account_list.append({"id": account["id"], "name": account["name"]})
    except KeyError as e:
        logging.error(f"KeyError: {e}")

    return account_list
