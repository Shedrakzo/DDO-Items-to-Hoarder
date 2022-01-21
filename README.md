# DDO-Items-to-Hoarder
Some Python scripts to transfer online DDO item data to The Hoarder.

# DDOWikiItems.py
(Uses a table scraping tutorial as a base)
This script will convert tables from any "Update X named items" titled DDOWiki page into a CSV file. Best results if there's only one table on the page, and follows the "Item, Type, Enhancements, ML, Bind, Quests" convention.

-u
For setting the page URL

Example:
    -u https://ddowiki.com/page/Update_48_named_items

-p
For setting the filepath/name to save to. No need to set the ".csv" file extention as well.

Example:
    -p newcsv

# autohoard.py
An automation script for use while The Hoarder is at full resolution. It will take CSV files created by the previous script and input the data there to create new custom items. Tested only using a 1920x1080 monitor.

-p
For finding the csv file for automation. No need to set the ".csv" file extention as well.

Example:
    -p newcsv
