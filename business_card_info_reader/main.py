from business_card_info_reader.api import fetch_image_analysis, parse_response


def main():
    image_url = "https://img.freepik.com/free-vector/modern-black-white-business-card-design_1017-14939.jpg?w=1380&t=st=1716968119~exp=1716968719~hmac=ff1d76f73142fe59b8e6eb273beeb6803b1e402ab68c07c38febbdddfd526b27"
    response = fetch_image_analysis(image_url)
    result = parse_response(response)
    print(result)


if __name__ == "__main__":
    main()
