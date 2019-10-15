# The CrackDown

## Introduction
The Crackdown is basically a repository on GitHub which hosts tool VRV, our very own created tool to detect whether a given site is a phishing site or not. VRV integrates two models. The first model follows the approach of using open source tools followed  by a second model which incorporates Machine Learning.

## VRV
VRV is a tool that will be used to tell whether the URL under consideration is a Phishing or a Non- Phishing one.
The tool will be working two models.
The first model follows the approach of using open source tools followed  by a second model which incorporates Machine Learning.
Machine learning model incorporates various classifiers that will be later used to enhance the probability and accuracy of the tool.
Later, both the models will be combined to generate the final output to tell whether the URL under consideration is a Phishing URL or a Genuine one.

## Overall System Architecture

<img width="718" alt="architecture" src="https://user-images.githubusercontent.com/54947999/66774467-3c66d280-eedf-11e9-9ca5-29e81361f7ab.png">

## Tools Used
### Whois
A whois Kali linux command is a utility as a part of the information gathering used in all of the Linux-based operating systems. this tool is part of information security assessment, and one of information gathering techniques.
### NSLookup
NSLookup is a network administr.ation command-line tool available in many computer operating systems for querying the Domain Name System (DNS) to obtain domain name or IP address mapping, or other DNS records
### Sublist3R
Sublist3r is a python tool designed to enumerate subdomains of websites using OSINT. It helps penetration testers and bug hunters collect and gather subdomains for the domain they are targeting. Sublist3r enumerates subdomains using many search engines such as Google, Yahoo, Bing, Baidu, and Ask. Sublist3r also enumerates subdomains using Netcraft, Virustotal, ThreatCrowd, DNSdumpster, and ReverseDNS.
Subbrute was integrated with Sublist3r to increase the possibility of finding more subdomains using bruteforce with an improved wordlist. The credit goes to TheRook who is the author of subbrute.
### XSS
XSStrike is a Cross Site Scripting detection suite equipped with four hand written parsers, an intelligent payload generator, a powerful fuzzing engine and an incredibly fast crawler.
Instead of injecting payloads and checking it works like all the other tools do, XSStrike analyses the response with multiple parsers and then crafts payloads that are guaranteed to work by context analysis integrated with a fuzzing engine.
### The Harvester
The Harvester is a very simple, yet effective tool designed to be used in the early
stages of a penetration test. Use it for open source intelligence gathering and
helping to determine a company's external threat landscape on the internet.
### Metagoofil
Metagoofil is a tool for extracting metadata of public documents (pdf,doc,xls,ppt,etc) availables in the target websites.This information could be useful because you can get valid usernames, people names, for using later in bruteforce password attacks (vpn, ftp, webapps), the tool will also extracts interesting "paths" of the documents, where we can get shared resources names, server names, etc.
### DNSRecon
DNSRecon is a Python port of a Ruby script that I wrote to learn the language and about DNS in early 2007. This time I wanted to learn about Python and extend the functionality of the original tool and in the process re-learn how DNS works and how could it be used in the process of a security assessment and network troubleshooting.
### Shodan
Shodan is a search engine for Internet-connected devices. Google lets you search for websites, Shodan lets you search for devices. This library provides developers easy access to all of the data stored in Shodan in order to automate tasks and integrate into existing tools.
### WPScan
WPScan is a black box WordPress vulnerability scanner that can be used to scan remote WordPress installations to find security issues.

## Working Of The Tool

![flowchart](https://user-images.githubusercontent.com/54947999/66774657-b5fec080-eedf-11e9-866d-b4dfbbfacf35.png)
