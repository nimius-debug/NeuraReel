template_categ = """
    Determine the category of the YouTube video using the provided title and transcription. 
    The categories are:

    1. Educational Content: Characterized by content primarily intended to provide knowledge or skill enhancement. Includes academic lectures, detailed how-to guides, science and technology discussions, tutorials, informational podcasts, and in-depth documentary-style videos.
    2. Entertainment Content: Filled with content primarily intended to entertain, engage, or amuse viewers. Encompasses comedy sketches, clips or full-length videos of movies or TV series, music videos, gaming content, vlogs, and reality TV content.
    3. News and Current Affairs: Features content that keeps viewers informed about the world around them. Includes regular news updates, in-depth discussions or debates on current issues, political commentary and analysis, interviews with public figures or experts, and documentaries covering current affairs.
    4. Lifestyle and Personal Content: Encapsulates content focusing on personal experiences,hobbies, interests, or lifestyle elements. Includes fitness routines, travel vlogs,food content, fashion and beauty content, home and garden content, personal vlogs, and product reviews.

    Title: ```{title}``` \
    Transcript: ```{transcript}``` \
"""

#######################Router Template#######################
educational_content_template = """You are an AI model trained to understand educational content. \
Your task is to identify the segment in the video transcript where a complete and crucial educational point or concept is explained, taking no longer than 30 seconds. \
Focus on extracting a complete idea that can be understood independently of the rest of the content.

Here is the transcript:
{input}"""

entertainment_content_template = """You are an AI model trained to analyze entertainment content. \
Your task is to identify the segment in the video transcript that delivers a complete and impactful entertainment value, taking no longer than 30 seconds. \
Identify a standalone moment that represents the entertainment value of the content.

Here is the transcript:
{input}"""

news_and_current_affairs_template = """You are an AI model trained to comprehend news and current affairs. \
Your task is to identify the segment in the video transcript where a significant news update or the core point of the current event is presented completely, taking no longer than 30 seconds. \
Find a segment that encapsulates a key point of the news story or event.

Here is the transcript:
{input}"""

lifestyle_and_personal_content_template = """You are an AI model trained to interpret lifestyle and personal content. \
Your task is to identify the segment in the video transcript that provides a full and valuable insight into the lifestyle or personal experience being shared, taking no longer than 30 seconds. \
Find a standalone moment that gives a clear insight into the content's main theme.

Here is the transcript:
{input}"""


MULTI_PROMPT_ROUTER_TEMPLATE = """Given a raw video transcript input, select the model prompt best suited for the input. \
You will be given the names of the available prompts and a description of what the prompt is best suited for. \
You may also revise the original input if you think that revising it will ultimately lead to a better response \
from the language model.

<< FORMATTING >>
Return a markdown code snippet with a JSON object formatted to look like:
```json
{{{{
    "destination": string,  // name of the prompt to use or "DEFAULT"
    "next_inputs": string  // a potentially modified version of the original input
}}}}
"""

#######################Router info#######################
prompt_infos = [
    {
        "name": "Educational Content", 
        "description": "Good for identifying key educational points from the video transcript", 
        "prompt_template": educational_content_template
    },
    {
        "name": "Entertainment Content", 
        "description": "Good for identifying entertaining segments from the video transcript", 
        "prompt_template": entertainment_content_template
    },
    {
        "name": "News and Current Affairs", 
        "description": "Good for identifying significant news updates or the core points of current events from the video transcript", 
        "prompt_template": news_and_current_affairs_template
    },
    {
        "name": "Lifestyle and Personal Content", 
        "description": "Good for identifying key insights into lifestyle or personal experiences from the video transcript", 
        "prompt_template": lifestyle_and_personal_content_template
    }
]

