# NPTEL Web Scraper

## Table of Contents

- [Description](#description)
- [Features](#features)
- [How to Use](#how-to-use)
- [Installation](#installation)

## Description

Web scraping, the process of extracting data from websites, plays a pivotal role in the digital age, facilitating the collection of valuable information for analysis, research, and automation. By utilizing HTTP requests to access web pages and parsing their content, web scraping empowers users to extract structured or unstructured data, such as text, images, and tables. While offering opportunities for automation and efficiency, it is essential to exercise responsibility, adhere to legal and ethical guidelines, respect server limitations, and clean extracted data for accuracy. Web scraping tools and libraries, coupled with the ability to navigate dynamic websites, empower individuals and organizations to harness the wealth of information available on the internet for various purposes, from competitive analysis to content aggregation and beyond.

## Features

The made code can be used to extract NPTEL notes in the form of PDF as it just clicks on the next button repeatedly until the final file is reached and takes the fit-to-screen print of each and every page it travels to.

## How to Use

replace the URL with the NPTEL notes URL in scrapper.py, wait for the process to complete and then use merger.py to merge the pdf

## Installation

```shell
$ pip install requests
$ pip install BeautifulSoup
$ pip install pdfkit
$ pip install PyPDF2
