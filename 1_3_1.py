# -*- coding: utf-8 -*-
import logging

import requests
import json
import tqdm
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url_mask = 'https://hh.ru/search/vacancy?search_field=name&search_field=description&text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&items_on_page=15&hhtmFrom=vacancy_search_list&page='
    max_pages = 150

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    res = {
        'data': [],
    }

    for page in range(0, max_pages):
        page_url = url_mask + str(page)
        page_resp = requests.get(page_url, headers=headers)
        print(f'{page+1} - {page_resp.status_code}')
        if page_resp.status_code == 200:
            page_soup = BeautifulSoup(page_resp.text, 'lxml')
            tags = page_soup.find_all(attrs={'data-qa': 'serp-item__title'})
            for tag in tqdm.tqdm(tags):
                vacancy_url = tag.attrs['href']
                vacancy_resp = requests.get(vacancy_url, headers=headers)
                # print(f'{vacancy_url} - {vacancy_resp.status_code}')
                if vacancy_resp.status_code == 200:
                    vacancy_soup = BeautifulSoup(vacancy_resp.text, 'lxml')
                    title = vacancy_soup.find(attrs={'data-qa': 'vacancy-title'})
                    if title:
                        title_text = vacancy_soup.find(attrs={'data-qa': 'vacancy-title'}).text
                        salary_text = None
                        salary = vacancy_soup.find(attrs={'data-qa': 'vacancy-salary'})
                        if salary:
                            salary_text = vacancy_soup.find(attrs={'data-qa': 'vacancy-salary'}).text
                        expirience_text = None
                        expirience = vacancy_soup.find(attrs={'data-qa': 'vacancy-experience'})
                        if expirience:
                            expirience_text = vacancy_soup.find(attrs={'data-qa': 'vacancy-experience'}).text

                        region_text = None
                        region = vacancy_soup.find(attrs={'data-qa': 'vacancy-view-raw-address'})
                        if region:
                            region_text = region.text.split(',')[0]
                        else:
                            region = vacancy_soup.find(attrs={'data-qa': 'vacancy-view-location'})
                            if region:
                                region_text = vacancy_soup.find(attrs={'data-qa': 'vacancy-view-location'}).text

                        res['data'].append({
                            'title': title_text,
                            'work expirience': expirience_text,
                            'salary': salary_text,
                            'region': region_text,
                        })
                        with open('1_3_1_hh.json', 'w') as outfile:
                            json.dump(res, outfile, ensure_ascii=False, indent=4)
        else:
            print(f'Error: HTTP {page_resp.status_code}')
            break




