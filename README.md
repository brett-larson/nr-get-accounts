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


## Requirements
- Python 3.x
- The following Python libraries:
  - requests
  - os
  - logging
  - dotenv

You can install these packages using the requirements.txt file, as shown above.
