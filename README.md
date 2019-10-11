# Facebook Crawler

Crawler that crawls own Facebook and exports name of all the friends and all the online friends into _txt_ files.

## Table of Contents
- [Requirements](#requirements)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Requirements

The crawler is written in Python 3, and uses selenium, so, make sure [selenium](https://selenium-python.readthedocs.io/installation.html) and [chrome webdriver](https://selenium-python.readthedocs.io/installation.html#drivers) is installed.

## Usage

There are two different independent methods for the FacebookCrawler class in the file [facebook_crawler.py](facebook_crawler.py).

1. *get_friends*
Exports all the friends of one's Facebook account in the file export/all_friends.txt.

2. *get_online_friends*
Exports all the friends online on the moment in the file export/online_friends.txt

Both the methods can be run by executing the file [facebook_crawler.py](facebook_crawler.py).

```
python3 facebook_crawler.py
```

_The exported files will be in the folder, [exports](exports)._

## Maintainers

[@Suraj1127](https://github.com/Suraj1127).

## Contributing

Feel free to dive in! [Open an issue](https://github.com/Suraj1127/facebook-crawler/issues/new) or submit PRs.


## License

[MIT](LICENSE) © Suraj Regmi

## Disclaimer
The author is acquainted on the crawlers and spiders Facebook policy. Thereby, this repository is intended for educational purpose and use of any code here on crawling Facebook against its policy is strictly discouraged. The author takes no responsibility on such actions, and such actions are on their own.