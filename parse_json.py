import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"}, ' \
            '{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

json_text_parsed = json.loads(json_text)

print(json_text_parsed["messages"][1])
