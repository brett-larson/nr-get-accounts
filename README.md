# Get New Relic Accounts
This Python application retrieves the account names and numbers within a given New Relic organization. The account numbers returned will vary depending on the [New Relic User API Key](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/) used within the application.

## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Logging](#logging)

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/brett-larson/nr-get-accounts.git
```

2. Create a virtual environment:

```
python -m venv venv
```

3. Activate the virtual environment:
  - Windows

```
venv\Scripts\activate
```

  - Mac

```
source venv/bin/activate
```

4. Install the required packages:

```
pip install -r requirements.txt
```

## Usage
1. Ensure you have set up the necessary Environment Variables.
2. Run the script in your IDE (PyCharm recommended).
3. Review the output for the account names and numbers.


## Requirements
- Python 3.x
- The following Python libraries:
  - requests
  - os
  - logging
  - dotenv

You can install these packages using the requirements.txt file.

## Environment Variables
The program uses the `dotenv` library to load environment variables. Create a `.env` file in the root directory and set the required variables:

```
NEW_RELIC_USER_KEY=YOUR_NEW_RELIC_USER_API_KEY
```

## Logging
The application uses Python's logging library for logging purposes. Logs will be written to a file named `app.log` in the root directory. You can check this log file for detailed information about the program's execution.
