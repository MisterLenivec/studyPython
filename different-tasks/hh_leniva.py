#!/usr/bin/env python3
import requests
import csv
from bs4 import BeautifulSoup as bs
from datetime import datetime


headers = {'Accept': '*/*',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'}

base_url = 'https://hh.ru/search/vacancy?search_period=3&clusters=true&area=1&text=junior+python&experience=noExperience&enable_snippets=true&page=0'

def hh_parse(base_url, headers):
    jobs = []
    urls = []
    urls.append(base_url)
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'lxml')
        try:
            pagination = soup.find_all('a', attrs={'data-qa': 'pager-page'})
            count = int(pagination[-1].text)
            for i in range(count):
                url = f'https://hh.ru/search/vacancy?search_period=3&clusters=true&area=1&text=junior+python&experience=noExperience&enable_snippets=true&page={i}'
                if url not in urls:
                    urls.append(url)
        except:
            pass

        for url in urls:
            request = session.get(url, headers=headers)
            soup = bs(request.content, 'lxml')
            divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
            for div in divs:
                try:
                    title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
                    href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
                    company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
                    responsibility = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
                    requirement = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
                    pub_date = div.find('span', attrs={'class': 'vacancy-serp-item__publication-date'}).text
                    jobs.append({
                        'title': title,
                        'href': href,
                        'company': company,
                        'responsibility': responsibility,
                        'requirement': requirement,
                        'pub_date': pub_date
                    })
                except:
                    pass
    else:
        print('Status ' + str(request.status_code))
    return jobs


def files_printer(jobs):
    # with open('parsed_jobs.csv', 'w') as file:
    #     a_pen = csv.writer(file)
    #     a_pen.writerow(('Publication date', 'Job title', 'URL', 'Company name', 'Responsibility', 'Requirement'))
    #     for job in jobs:
    #         a_pen.writerow((job['pub_date'], job['title'], job['href'], job['company'], job['responsibility'], job['requirement']))
    print('Number of vacancies ' + str(len(jobs)))
    print('Today ' + datetime.today().strftime('%d/%m/%Y'), end='\n\n')
    for job in jobs:
        print(job['pub_date'], end=' ')
        print(job['company'], end='\n')
        print(job['title'], end='\n')
        print(job['href'], end='\n')
        print(job['responsibility'], end='\n')
        print(job['requirement'], end='\n\n\n')


jobs = hh_parse(base_url, headers)
files_printer(jobs)
