import requests
import argparse
from time import sleep
import whois
import datetime


def load_urls4check(path):
    try:
        with open(path, 'r') as file:
            urls = file.read().split()
    except FileNotFoundError:
        urls = None
    return urls


def is_server_respond_with_200(urls):
    answer_from_code = []
    for url in urls:
        try:
            requests.get(url)
        except requests.exceptions.MissingSchema:
            url = 'http://{0}'.format(url)
        except requests.exceptions.ConnectionError:
            return None
        answer_from_code.append(
            requests.get(url).status_code == 200
        )
    return answer_from_code


def get_domain_expiration_date(domain_name):
    status_of_pay = []
    for url in domain_name:
        if url.startswith('http://'):
            url = url.replace(url, url.partition('http://')[2])
        exp_date = whois.query(url).expiration_date - \
            datetime.timedelta(days=31)
        status_of_pay.append(
            exp_date.month >= 1
        )
    return status_of_pay


def main():
    parser = argparse.ArgumentParser(
        description='Parse web site and responde code and paid status'
    )
    parser.add_argument('file',
                        help='Input filename with list of urls')
    args = parser.parse_args()
    urls = load_urls4check(args.file)
    if urls:
        list_with_code_answer = is_server_respond_with_200(urls)
        list_with_pay_status = get_domain_expiration_date(urls)
        for urls_code_and_status_pay in zip(
            urls, list_with_code_answer, list_with_pay_status
        ):
            print('Web site: {0}, is answer 200: {1}, paid status: {2}'.format(
                urls_code_and_status_pay[0], urls_code_and_status_pay[1],
                urls_code_and_status_pay[2]))
    else:
        print('Perhaps you did not input file with url or file empty')


if __name__ == '__main__':
    main()
