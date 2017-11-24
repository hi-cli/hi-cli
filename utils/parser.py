#!/usr/bin/env python

# cluster_name=$(python parse-yaml.py example.yaml app cluster-name)                                                                       

import sys
import os.path
import yaml
import json

def parse(data):
    try:
        key = list()

        # get the key
        for i in range(3, len(sys.argv)):
            key.append(sys.argv[i])

        # print(key)    

        ret_val = data
        for k in key:
            ret_val = ret_val[k]
            
        print(ret_val)
    except yaml.YAMLError as exc:
        print(exc)
    except KeyError:
        print('')   

def main():
    input_type = sys.argv[1]
    source = sys.argv[2]
    # print(source) 
    if input_type == 'file':
        if os.path.isfile(source):
            with open(source, 'r') as stream:
                if source.endswith('.yml') or source.endswith('.yaml'):
                    data = yaml.load(stream)
                elif source.endswith('.json'):
                    data = json.load(stream)
                else:
                    # print('File ' + source + ' is not support yet!')
                    print('')
                    exit()

                parse(data)
        else:
            # print('File ' + source + ' does not exist!')
            print('')
    elif input_type == 'json':       
        parse(json.loads(source))
    elif input_type == 'yaml':        
        parse(yaml.load(source))
    else:
        print('')    

if __name__ == '__main__':
    main()
