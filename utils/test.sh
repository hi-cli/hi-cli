
source "${HI_CLI_HOME}/bin/colors"
source "${HI_CLI_HOME}/bin/logging"

parser="${HI_CLI_HOME}/utils/parser.py"

function parse_json()
{
    json_str=$(cat example.json)
    value=$(python ${parser} json "$json_str" $@)

    echo "$value"
}

function parse_yaml()
{

    yaml_str=$(cat example.yaml)
    value=$(python ${parser} yaml "$yaml_str" $@)

    echo "$value"
}

echo parsed json value: $(parse_json $@)

echo parsed yaml value: $(parse_yaml $@)

