import json
from helper_functions import llm

theme_n_film_name = {'Family Friendly': ['The King of Musang King', 
                                         'Ajoomma', 
                                         'Reunion Dinner',
                                         'Tiong Bahru Social Club',
                                         'Number 1',
                                         'The Diam Diam Era 2',
                                         'The Diam Diam Era', 
                                         'Long Long Time Ago',
                                         '7 Letters',
                                         'Ilo Ilo',
                                         'Ah Boys To Men 4',
                                         'Ah Boys To Men 3 Frogmen',
                                         'Ah Boys To Men 2',
                                         'Ah Boys To Men',
                                         '881',
                                         'Homerun'],
                    'World Cinema':     ['Geylang',
                                         'Precious Is The Night',
                                         'Wet Season',
                                         'A Land Imagined',
                                         'Apprentice',
                                         'A Yellow Bird',
                                         'Sandcastle',
                                         'Singapore Dreaming',
                                         'Forever Fever',
                                         '12 Storeys'],
                    'Southeast Asian Cinema': ['Autobiography',
                                               'Arnold Is A Model Student',
                                               'Anatomy of Time',
                                               'Yuni',
                                               'Pop Aye']}

# Load the JSON file
filepath = './data/film_programming.json'
with open(filepath, 'r', errors='ignore') as file:
    json_string = file.read()
    dict_of_films = json.loads(json_string)


def identify_theme_and_film(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with customer service queries. \
    The customer service query will be enclosed in
    the pair of {delimiter}.

    You are familiar with the media ratings, whereby
    'G' is General - suitable for all ages, 
    'PG' is Parental Guidance - Suitable for all but parents should guide their young,
    'PG 13' is Parental Guidance 13 - Suitable for persons aged 13 and above but parental guidance is advised for children below 13,
    'NC 16' is No Children under 16 - Restricted to persons aged 16 and above, 
    'M 18' is Mature 18 - Restricted to persons aged 18 and above, and
    'R 21' is Restricted 21 - Restricted to adults aged 21 and above.

    Decide if the query is relevant to any specific film
    in the Python dictionary below, which each key is a `theme` 
    and the value is a list of `films`.

    If there are any relevant film(s) found, output the pair(s) of a) `film` the relevant films and b) the associated `theme`  into a
    list of dictionary object, where each item in the list is a relevant course
    and each course is a dictionary that contains two keys:
    1) theme
    2) film_name

    {theme_n_film_name}

    If are no relevant films are found, output an empty list.

    Ensure your response contains only the list of dictionary objects or an empty list, \
    without any enclosing tags or delimiters.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    category_and_product_response_str = llm.get_completion_by_messages(messages)
    category_and_product_response_str = category_and_product_response_str.replace("'", "\"")
    category_and_product_response = json.loads(category_and_product_response_str)
    return category_and_product_response
    

def get_film_details(list_of_relevant_theme_n_film: list[dict]):
    film_names_list = []
    for x in list_of_relevant_theme_n_film:
        film_names_list.append(x.get('film_name')) # x["film_name"]

    list_of_film_details = []
    for film_name in film_names_list:
        list_of_film_details.append(dict_of_films.get(film_name))
    return list_of_film_details


def generate_response_based_on_film_details(user_message, product_details):
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the customer queries.
    The customer query will be delimited with a pair {delimiter}.

    Step 1:{delimiter} If the user is asking about what are the films available to be programmed, \
    understand the relevant film(s) from the following list.
    All available films shown in the json data below:
    {product_details}

    Step 2:{delimiter} Use the information about the film to \
    generate the answer for the customer's query.
    You must only rely on the facts or information in the film information.
    Your response should be as detail as possible and \
    include information that is useful for customer to better understand the film.

    Step 3:{delimiter}: Answer the customer in a friendly tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    the customers to make their decision, highlighting a maximum of 5 titles from the list. 
    Complete with details such as synopsis, accolades, rating, links to trailers.
    Use Neural Linguistic Programming to construct your response.

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to customer>

    Make sure to include {delimiter} to separate every step.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_to_customer = llm.get_completion_by_messages(messages)
    response_to_customer = response_to_customer.split(delimiter)[-1]
    return response_to_customer


def process_user_message(user_input):
    delimiter = "```"

    # Process 1: If films are found, look them up
    theme_n_film_name = identify_theme_and_film(user_input)
    print("theme_n_film_name : ", theme_n_film_name)

    # Process 2: Get the Film Details
    film_details = get_film_details(theme_n_film_name)

    # Process 3: Generate Response based on Film Details
    reply = generate_response_based_on_film_details(user_input, film_details)


    return reply, film_details