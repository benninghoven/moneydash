# MoneyDash

MoneyDash is a finance scraper that uses APIs from Robinhood, Coinbase, and Bank of America to track investments, bank accounts, and transactions. It then displays this information into a database for easy analysis and visualization.

# Features
Tracks investment portfolio on Robinhood
Tracks cryptocurrency portfolio on Coinbase
Tracks bank account transactions from Bank of America
Displays information in an organized and easy-to-read database
Installation
Clone the repository using the command:

Copy code

```bash
git clone https://github.com/benninghoven/moneydash.git
```
Fill in your own API credentials in the ```example.credentials.json``` and name it to ```credentials.json```
  
Run the docker container to start

```bash
docker-compose up
```

# Usage
MoneyDash is designed to be easy to use. Simply run the docker container start the scraper, and it will begin pulling data from Robinhood, Coinbase, and Bank of America every 6 hours, or whatever the crontab is specified for.

The data is then stored in a SQLite database, which can be accessed and analyzed using SQL or a tool such as SQLite Browser.

# Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

Fork the repository.

Make your changes and test them thoroughly.

Create a pull request with a clear description of your changes.

Wait for your changes to be reviewed and merged into the main branch.

License
This project is licensed under the MIT License. Feel free to use and modify it as you see fit.
