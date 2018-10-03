import requests
import csv
import logging
import tqdm
import os
import errno

# Logging basic date/time config
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')

# Create the output logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class TravisMiner:

    def __init__(self, input_path, output_path):
        self.base_url = 'https://api.travis-ci.org/repos/'
        self.input_path = input_path
        self.output_path = output_path

    def collect_projects(self):

        # Create the output dir if not existent
        try:
            os.makedirs(self.output_path)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise

        with open(self.output_path + '/' + 'travis-projects.csv', 'w', newline='') as my_file:
            projects_list = csv.writer(my_file,quoting=csv.QUOTE_ALL)
            projects_list.writerow(['id', 'url', 'owner_id', 'name', 'description', 'language', 'created_at',
                                    'forked_from', 'deleted', 'updated_at', 'repo_id', 'count_users', 'last_build_id'])

            with open(self.input_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                for row in tqdm.tqdm(reader):
                    logger.info('Requesting....' + row['url'].split('/')[5])
                    url = (self.base_url + row['url'].split("/")[4] + '/' + row['url'].split("/")[5])
                    response = requests.get(url)
                    if response.status_code == 200 and response.json()['last_build_id'] != None:
                        results = []
                        for k, v in row.items():
                            results.append(v)
                        results.append(response.json()['last_build_id'])
                        projects_list.writerow(results)