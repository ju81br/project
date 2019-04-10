""" Webservice utils """

import json
import logging as log
import yaml
import requests
from database import INSERTY_CITY, INSERT_TEMPERATURE, INSERTY_RAIN, QUERY_MAX_TEMP \
    , QUERY_AVG_PRECIPITATION, connect, DB_DEFAULT_ERR, DB_INTEGRITY_ERR, dictfetchall


api_url = ''
api_token = ''


def yaml_loader(filepath):
    """ Read config file (docstring) """
    global api_url, api_token
    with open(filepath, 'r') as stream:
        try:
            data = yaml.load(stream)
            api_url = data['climatempo-api-url']
            api_token = data['climatempo-api-token']
        except yaml.YAMLError as err:
            log.error(err)


def get_city(id):
    """ Save city info (docstring) """
    default_api_url = api_url.format(id, api_token)
    r = make_request(default_api_url)

    conn = connect()
    cur = conn.cursor()

    try:
        try:
            cur.execute(INSERTY_CITY, (r['id'], r['name'], r['state'], r['country']))
        except DB_INTEGRITY_ERR as err:
            log.warn('city already exists - %s', err)

        try:
            for data in r['data']:
                cur.execute(INSERT_TEMPERATURE, (data['date'], data['temperature']['min'], data['temperature']['max'], r['id']))
                cur.execute(INSERTY_RAIN, (data['date'], data['rain']['probability'], data['rain']['precipitation'], r['id']))
        except DB_INTEGRITY_ERR as err:
            log.warn('day already exists for this city - %s', err)

        conn.commit()
    except KeyError as err:
        log.error(err)
        return False, err
    finally:
        conn.close()

    return True, {}


def get_average(date_initial, date_final):
    """ Get average of precipitation and Max temp. (docstring) """
    conn = connect()
    cur = conn.cursor()

    try:
        result = cur.execute(QUERY_MAX_TEMP, (date_initial, date_final))
        rows = dictfetchall(result)
        city = rows[0]['city']
        temp = rows[0]['max_temp']

        result = cur.execute(QUERY_AVG_PRECIPITATION)
        rows = dictfetchall(result)
        avg = list()

        for r in rows:
            avg.append({'city': r['city'], 'avg': r['average']})

    except KeyError as err:
        log.error(err)
        return False, err
    except DB_DEFAULT_ERR as err:
        log.error(err)
        return False, err
    finally:
        conn.close()

    return True, {'max_temp': {'city': city, 'max': temp}, 'avg': avg}


def make_request(url):
    """ Make a simple request (docstring) """
    try:
        resp = requests.get(url)
        content = resp.content.decode('utf-8')
        return json.loads(content)
    except requests.HTTPError as err:
        log.error(err)
    except ValueError as err:
        log.error(err)

    return {}
