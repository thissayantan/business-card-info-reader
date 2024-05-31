def get_business_card_analysis_prompt():
    return """
    First, determine if the image provided is likely a business card. If it is, analyze the image and extract the information. Return the data in a structured JSON format. Field names should be in camel case, including fields for:
    - Full name
    - Job title
    - Company name
    - Email
    - Phone number
    - Website
    - Address (street, city, state, zip code, country)
    - Social media (LinkedIn, Twitter, Facebook)
    - Additional notes and tags.
    If it is not a business card, return a response indicating that no business card data was detected.
    """
